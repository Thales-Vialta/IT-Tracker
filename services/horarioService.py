from repositories.horarioRepository import horarioRepo
from models.horario import HorarioFuncionamento
from datetime import datetime
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
    
    def HorarioFuncExiste(self):
        horarios_cadastrados = self.horario_repo.Mostrar_Horario()
    
        for HoraInicio, HoraFim, Descricao in horarios_cadastrados:
            if Descricao.strip() == 'Horario de Funcionamento':
                return True
                
        return False
    
    def tratarHorario(self, valor):
        resultado = "" 
        
        for linha in valor:
            HoraInicio = linha[1]  
            HoraFim = linha[2]
            Descricao = linha[3]

            inicio_str = str(HoraInicio).zfill(8)[:5]
            fim_str = str(HoraFim).zfill(8)[:5]
           
            
            return Descricao, inicio_str, fim_str
    
    def buscarHorario(self,valor):
        horario = self.horario_repo.buscar_Horario(valor)
        return horario
    
    def intervaloValido(self, inicio, fim):
        horario_funcionamento = self.buscarHorario('Horario de Funcionamento')

        horario_tratado = self.tratarHorario(horario_funcionamento)

        _, func_inicio, func_fim = horario_tratado
        try:
            formato = "%H:%M"
        
            limite_inicios = datetime.strptime(func_inicio, formato).time()
            limite_fim = datetime.strptime(func_fim, formato).time()
        
            usuario_inicio = datetime.strptime(inicio, formato).time()
            usuario_fim = datetime.strptime(fim, formato).time()
        
        except ValueError:
            return False
        

        if usuario_inicio >= limite_inicios and usuario_fim <= limite_fim:
            return True
        else:
            return False
        
    def intervaloExiste(self, inicio, fim):
        total = self.horario_repo.contarConfrontos(inicio,fim)

        totalPuro = total[0][0]
        print(totalPuro)

        if totalPuro == 0:
            return "Nenhum intervalo com essas horas"
        
        if totalPuro == 1:
            return "Continue"
        
        if totalPuro == 2:
            return 'O sistema quebrou, pois isso não deveria ser possivel'
        
    def criarIntervalo(self, desc, inicio, fim):
        try:
            formato = "%H:%M"
            obj_inicio = datetime.strptime(inicio, formato).time()
            obj_fim = datetime.strptime(fim, formato).time()
        except ValueError:
            return f"{CORES['VERMELHO']}Erro: Formato de hora inválido! Use HH:MM.{CORES['RESET']}"
        
        if obj_inicio >= obj_fim:
            return f"{CORES['VERMELHO']}Erro: O horário de início não pode ser maior ou igual ao término.{CORES['RESET']}"
        
        if desc != 'Horario de Funcionamento':
            if not self.intervaloValido(inicio, fim):
                return f"{CORES['VERMELHO']}Erro: O horário solicitado está fora do limite de funcionamento da empresa.{CORES['RESET']}"

        status_confronto = self.intervaloExiste(inicio, fim)
        
        if status_confronto == "Continue":
            return f"{CORES['AMARELO']}Aviso: Esse intervalo de horário já está cadastrado no sistema.{CORES['RESET']}"
        
        if status_confronto == 'O sistema quebrou, pois isso não deveria ser possivel':
            return f"{CORES['VERMELHO']}Erro Crítico: Duplicidade inconsistente encontrada no banco de dados.{CORES['RESET']}"

        try:
            novoIntervalo = HorarioFuncionamento(inicio, fim,desc)
            inicio = novoIntervalo.horaAbertura
            fim = novoIntervalo.horaFechamento
            desc = novoIntervalo.descricao

            self.horario_repo.Cadastrar_Horario(desc, inicio, fim) 
            return f"{CORES['NEGRITO']}Intervalo ({inicio} - {fim}){CORES['RESET']} {CORES['VERDE']}criado com sucesso!{CORES['RESET']}"
        except Exception as e:
            return f"{CORES['VERMELHO']}Erro ao salvar o horário no banco de dados: {e}{CORES['RESET']}"        
    
    def editarIntervalo(self, id_horario, nova_desc, novo_inicio, novo_fim):
        """Edita um intervalo existente no banco validando as regras de negócio."""
        
        try:
            formato = "%H:%M"
            obj_inicio = datetime.strptime(novo_inicio, formato).time()
            obj_fim = datetime.strptime(novo_fim, formato).time()
        except ValueError:
            return f"{CORES['VERMELHO']}Erro: Formato de hora inválido! Use HH:MM.{CORES['RESET']}"

        if obj_inicio >= obj_fim:
            return f"{CORES['VERMELHO']}Erro: O horário de início não pode ser maior ou igual ao término.{CORES['RESET']}"

        if nova_desc != 'Horario de Funcionamento':
            if not self.intervaloValido(novo_inicio, novo_fim):
                return f"{CORES['VERMELHO']}Erro: Os novos horários estão fora do limite de funcionamento da empresa.{CORES['RESET']}"

        horarios_banco = self.horario_repo.Mostrar_Horario()
        horario_atual = None
        for inicio, fim, desc in horarios_banco:
            if desc == nova_desc and self.horario_repo.descobrirIdPorDescricao(desc) == id_horario:
                horario_atual = (str(inicio)[:5], str(fim)[:5])
                break

        if horario_atual != (novo_inicio, novo_fim):
            status_confronto = self.intervaloExiste(novo_inicio, novo_fim)
            if status_confronto == "Continue":
                return f"{CORES['AMARELO']}Aviso: Esse intervalo de horário já está cadastrado no sistema para outro registro.{CORES['RESET']}"
            if status_confronto == 'O sistema quebrou, pois isso não deveria ser possivel':
                return f"{CORES['VERMELHO']}Erro Crítico: Inconsistência gravíssima detectada no banco.{CORES['RESET']}"

        try:
            self.horario_repo.Editar_Horario_Por_Id(id_horario, novo_inicio, novo_fim)
            
            return f"{CORES['VERDE']}Horário atualizado com sucesso para{CORES['RESET']} {novo_inicio} - {novo_fim}!"
        except Exception as e:
            return f"{CORES['VERMELHO']}Erro ao atualizar o horário no banco de dados: {e}{CORES['RESET']}"

    def removerIntervalo(self, desc):
            
            id = self.horario_repo.descobrirIdPorDescricao(desc)

            if not id:
                return f"{CORES['VERMELHO']}Erro: É necessário informar um ID válido para exclusão.{CORES['RESET']}"

            try:

                linhas_afetadas = self.horario_repo.remover_Horario(id)
                
                if linhas_afetadas == 0:
                    return f"{CORES['AMARELO']}Aviso: Nenhum intervalo foi encontrado com o ID {id}.{CORES['RESET']}"
                    
                return f"{CORES['VERDE']}Intervalo removido com sucesso do sistema!{CORES['RESET']}"
                
            except Exception as e:
                return f"{CORES['VERMELHO']}Erro ao remover o horário do banco de dados: {e}{CORES['RESET']}"


horarioService = horarioService(horarioRepo)

