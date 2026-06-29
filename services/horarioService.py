from repositories.horarioRepository import horarioRepo
from datetime import date, time
from views.limparTela import limpar_tela
from views.cores import CORES

class horarioService:

    def __init__(self, horario_repository):
        self.horario_repo = horario_repository

    def listarHorarios(self):

        hora = self.horario_repo.Mostrar_Horario()

        resultado = f"{CORES['AZUL']}{CORES['NEGRITO']}---- LISTA DE HOR├üRIOS ----\n\n{CORES['RESET']}"

        for HoraInicio, HoraFim, Descricao in hora:
            inicio_str = str(HoraInicio)
            fim_str = str(HoraFim)
            periodo = f"{inicio_str} - {fim_str}"

            desc_format = Descricao.ljust(30)

            resultado += f"{CORES['AMARELO']}{CORES['NEGRITO']}{desc_format} | {CORES['RESET']} {CORES['RESET']} {periodo}\n"

        return resultado
    
    def validarTipoHorario(self):
        horarios_cadastrados = self.horario_repo.Mostrar_Horario()
        
        for HoraInicio, HoraFim, Descricao in horarios_cadastrados:
            if Descricao.strip() == 'Horario de Funcionamento':
                return 'Deseja cadastrar um intervalo?'
                
        return 'Deseja cadastrar o horario de funcionamento?'
    
    
    def intervaloHora(self):
            horarios_cadastrados = self.horario_repo.Mostrar_Horario()
            
            for HoraInicio, HoraFim, Descricao in horarios_cadastrados:
                if Descricao.strip() == 'Horario de Funcionamento':
                    return HoraInicio, HoraFim                   
            
            return None
    
    def verificarHorarioPermitido(self, hora_I, hora_F):
            intervalo_funcionamento = self.intervaloHora()
            
            if not intervalo_funcionamento:
                return False
                
            func_inicio, func_fim = intervalo_funcionamento
            
            str_inicio = str(func_inicio).zfill(8)
            str_fim = str(func_fim).zfill(8)
            
            limite_inicio = str_inicio[:5]
            limite_fim = str_fim[:5]

            if hora_I >= limite_inicio and hora_F <= limite_fim:
                if hora_I < hora_F:
                    return True
                    
            return False
        
    def validarHorarioExistente(self, desc, hora_I, hora_F, id_atual=None):
                dados_banco = self.horario_repo.buscar_Horario(desc)
                
                if not dados_banco:
                    dados_banco = self.horario_repo.Mostrar_Horario() # Atualizado para bater com seu Mostrar_Horario()
                    
                    if not dados_banco:
                        return False

                for registro in dados_banco:
                    if len(registro) == 4:
                        id_banco, hora_inicio, hora_fim, descricao = registro
                        # Pula a verificação se o registro analisado for o mesmo que estamos editando
                        if id_atual and id_banco == id_atual:
                            continue
                    else:
                        hora_inicio, hora_fim, descricao = registro
                    
                    inicio_limpo = str(hora_inicio).zfill(8)[:5]
                    fim_limpo = str(hora_fim).zfill(8)[:5]
                    descricao_limpa = descricao.strip()

                    if descricao_limpa == desc.strip() and inicio_limpo == hora_I.strip() and fim_limpo == hora_F.strip():
                        return True
                        
                    if inicio_limpo == hora_I.strip() and fim_limpo == hora_F.strip():
                        return True
                        
                return False


    def criarIntervaloHora(self, desc, inicio, fim):
        desc_limpa = desc.strip()

        if self.validarHorarioExistente(desc_limpa, inicio, fim):
            return f"Erro: O horário ou a descrição '{desc_limpa}' ({inicio} às {fim}) já está em uso!"

        # CASO 1: Se for o horário principal, cadastra direto
        if desc_limpa == 'Horario de Funcionamento':
            self.horario_repo.Cadastrar_Horario(desc, inicio, fim)
            return 'Horário de Funcionamento cadastrado com sucesso!'

        # CASO 2: Se for um intervalo (Almoço, Café, etc), valida os limites
        else:
            if not self.intervaloHora():
                return 'Erro: Cadastre primeiro o Horário de Funcionamento do estabelecimento!'

            validacao = self.verificarHorarioPermitido(inicio, fim)

            if not validacao:
                return 'Intervalo inadequado! Deve estar dentro do horário de funcionamento.'
            
            self.horario_repo.Cadastrar_Horario(desc, inicio, fim)
            return 'Intervalo cadastrado com sucesso!'
        
    def buscarIdPorDescricao(self, desc: str):
        # 1. Busca os registros no banco usando a descrição
        dados_banco = self.horario_repo.buscar_Horario(desc)
        
        # 2. Se não encontrar nada, avisa a View
        if not dados_banco:
            return None
            
        # 3. Como o buscar_Horario retorna uma lista de tuplas,
        # pegamos o idHorarioFunc (primeira coluna) do primeiro registro encontrado
        # Ordem: (idHorarioFunc, HoraInicio, HoraFim, Descricao)
        id_horario = dados_banco[0][0]
        
        return id_horario
        
    def atualizarHorario(self, desc_antiga: str, atributo: str, valor: str):
        # 1. Validação de Existência (Igual ao seu "Usuário não encontrado!")
        horario_atual = self.horario_repo.buscar_Horario(desc_antiga)

        if not horario_atual:
            return "Horário não encontrado!"
        
        else:
            # Desempacota o estado atual vindo do banco (id, inicio, fim, descricao)
            id_horario, inicio_banco, fim_banco, desc_banco = horario_atual[0]
            
            # Traduz os timedeltas do MySQL para strings limpas "HH:MM"
            inicio_atual = str(inicio_banco).zfill(8)[:5]
            fim_atual = str(fim_banco).zfill(8)[:5]
            desc_atual = desc_banco.strip()

            # Padroniza o nome do atributo para o formato aceito pelas colunas do banco
            if atributo in ['inicio', 'HoraInicio']:
                atributo = 'HoraInicio'
            elif atributo in ['fim', 'HoraFim']:
                atributo = 'HoraFim'
            elif atributo in ['descricao', 'Descricao']:
                atributo = 'Descricao'

            # 2. Preparação do cenário futuro para validação
            # Se o atributo alterado não for este, ele mantém o valor atual do banco
            nova_desc = valor.strip() if atributo == 'Descricao' else desc_atual
            novo_inicio = valor.strip() if atributo == 'HoraInicio' else inicio_atual
            novo_fim = valor.strip() if atributo == 'HoraFim' else fim_atual

            # 3. BLOCO DE VALIDAÇÕES DE HORÁRIO
            
            # Validação A: Evitar duplicidade de nome ou choque de horários idênticos
            if self.validarHorarioExistente(nova_desc, novo_inicio, novo_fim, id_atual=id_horario):
                return "Erro: Esse horário ou descrição já está em uso por outro registro!"

            # Se o horário atual (ou o novo nome) não for o principal, valida as regras de limites
            if nova_desc != 'Horario de Funcionamento':
                # Validação B: Verificar se o horário pai de funcionamento existe
                if not self.intervaloHora():
                    return "Erro: Cadastre primeiro o Horário de Funcionamento!"
                
                # Validação C: Verificar se as novas horas cabem dentro do expediente principal
                if not self.verificarHorarioPermitido(novo_inicio, novo_fim):
                    return "Intervalo inadequado! Deve estar dentro do horário de funcionamento."

            # 4. SALVAMENTO DINÂMICO (Seguindo o molde do seu atualizaUsuario)
            self.horario_repo.Editar_Horario(atributo, valor, desc_antiga)
            return f"{atributo} atualizado!"
        
    def removerHorario(self, desc_horario: str):
        # Buscamos o horário para saber se ele realmente existe no banco
        validacao = self.horario_repo.buscar_Horario(desc_horario)

        if not validacao:
            return "Horário não encontrado!"
        
        else:
            self.horario_repo.remover_Horario(desc_horario)
            
           
            return "Horário removido com sucesso!"


horarioService = horarioService(horarioRepo)

