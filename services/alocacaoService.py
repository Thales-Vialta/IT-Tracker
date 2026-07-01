from views.limparTela import limpar_tela
from views.cores import CORES

from repositories.alocacaoRepository import repoAlocacao
from services.userService import userService
from services.salaService import salaService

class AlocacacaoService: 
    def __init__(self, repoAlocacao, salaService, userService):
        self.repoAloc = repoAlocacao
        self.salaServ = salaService
        self.userServ = userService

    def cadastrarAlocacao(self, data_hora_inicio, data_hora_fim, listIDs_aparelho: list, user, sala):
            
            usuario_busca = self.userServ.buscaUsuario(user)
            usuario = usuario_busca[0][0]

            sala_busca = self.salaServ.buscarSalas(sala)
            salaTratada = sala_busca[0][0]
            
            if not usuario_busca:
                raise Exception(f"Usuário '{usuario}' não foi encontrado no banco!")
            if not sala_busca:
                raise Exception(f"Sala '{salaTratada}' não foi encontrada no banco!")


            # ETAPA 1: Salva a alocação global UMA ÚNICA VEZ e pega o ID gerado
            id_nova_alocacao = self.repoAloc.inserir_Alocacao_Principal(
                idUsuario=int(usuario),
                idSala=int(salaTratada),
                DataAlocacao=str(data_hora_inicio),
                DataDevolucao=str(data_hora_fim)
            )
            
            if not id_nova_alocacao:
                raise Exception("Erro técnico: Não foi possível gerar o ID da nova alocação.")

            # ETAPA 2: Agora sim, faz o loop para salvar os aparelhos na tabela ponte
            for id_aparelho in listIDs_aparelho:
                self.repoAloc.inserir_Item_Alocacao(
                    idAlocacao=id_nova_alocacao, 
                    idAparelho=int(id_aparelho)
                )
                
            return f"Sucesso! Reserva #{id_nova_alocacao} criada com {len(listIDs_aparelho)} aparelho(s) vinculado(s)."
        
        
   

    def listarAlocacao(self):
            limpar_tela()

            alocacoes = self.repoAloc.listar_alocacoes()

            # Inicializa a variável acumuladora com o cabeçalho azul e negrito
            texto_retorno = f"{CORES['AZUL']}{CORES['NEGRITO']}--- RESERVAS ---\n\n{CORES['RESET']}"

            if not alocacoes:
                texto_retorno += "Nenhuma reserva encontrada.\n"
                return texto_retorno

            for registro in alocacoes:
                # Variáveis na ordem EXATA das colunas do seu SELECT
                id_alocacao, usuario, sala, dt_alocacao, dt_devolucao, patrimonios, aparelhos = registro
                
                # Vai concatenando cada bloco de informação na string utilizando += e \n
                texto_retorno += f"Alocação ID: #{id_alocacao} | Usuário: {usuario}\n"
                texto_retorno += f"  ├─ Local: {sala}\n"
                texto_retorno += f"  ├─ Patrimônio(s): [{patrimonios}]\n"
                texto_retorno += f"  ├─ Aparelho(s):   {aparelhos}\n"
                texto_retorno += f"  └─ Período:       {dt_alocacao} até {dt_devolucao}\n"
                texto_retorno += "-" * 70 + "\n"

            return texto_retorno


        


    def buscarAlocacao(self, id_alocacao: int) -> str:
            # Busca a alocação de forma segura no repositório
            validacao = self.repoAloc.buscar_alocacao(int(id_alocacao))
            
            texto_retorno = f"=================== RESULTADO DA BUSCA (ID: {id_alocacao}) ===================\n"

            # 🌟 Correção do Erro 1: Se for None, sai antes de tentar desempacotar dados que não existem
            if not validacao:
                return f"=================== RESULTADO DA BUSCA (ID: {id_alocacao}) ===================\nNenhuma alocação encontrada com este ID.\n===================================================================="

            # 🌟 Correção do Erro 2: Desempacota na ordem exata das colunas do SELECT customizado
            id_aloc, data_alocacao, data_devolucao, nome_sala, nome_usuario, patrimonios_agrupados = validacao
            
            # Monta o texto final de maneira limpa e profissional
            texto_retorno += f"Usuário Responsável: {nome_usuario}\n"
            texto_retorno += f"  ├─ Local/Sala:      {nome_sala}\n"
            texto_retorno += f"  ├─ Patrimônio(s):   [{patrimonios_agrupados}]\n"
            texto_retorno += f"  ├─ Data Início:     {data_alocacao}\n"
            texto_retorno += f"  └─ Data Devolução:  {data_devolucao}\n"
            texto_retorno += "-" * 60 + "\n"
            texto_retorno += "===================================================================="
            
            return texto_retorno

    def editarAlocacao(self, id_alocacao: int, atributo: str, valor):
            # Converte o ID para inteiro garantindo a segurança
            id_alocacao = int(id_alocacao)

            # 🌟 CASO 1: O usuário quer mudar os APARELHOS da reserva
            if atributo.lower() in ["aparelho", "id_aparelho", "aparelhos"]:
                if not isinstance(valor, list):
                    raise Exception("Para editar aparelhos, o valor precisa ser uma lista de IDs!")

                # 1. Limpa todos os aparelhos antigos que pertenciam a essa alocação
                self.repoAloc.limpar_itens_alocacao(id_alocacao)

                # 2. Insere a nova lista de aparelhos um por um na tabela ponte
                for id_aparelho in valor:
                    self.repoAloc.inserir_Item_Alocacao(id_alocacao, int(id_aparelho))

                return f"Sucesso! Os aparelhos da alocação #{id_alocacao} foram atualizados."

            # 🌟 CASO 2: O usuário quer mudar Sala, Usuário ou Datas (Campos nativos)
            # 🌟 CASO 2: O usuário quer mudar Sala, Usuário ou Datas (Campos nativos)
            else:
                colunas_validas = {
                    "usuario": "idUsuario",
                    "sala": "idSala",
                    "inicio": "DataAlocacao",
                    "fim": "DataDevolucao"
                }

                coluna_mysql = colunas_validas.get(atributo.lower())
                if not coluna_mysql:
                    raise Exception(f"Atributo '{atributo}' inválido para edição.")

                # --- NOVO: Tratamento para converter Nome de Sala em ID ---
                if atributo.lower() == "sala":
                    sala_busca = self.salaServ.buscarSalas(valor)
                    if not sala_busca:
                        raise Exception(f"Sala '{valor}' não foi encontrada no banco!")
                    # Desembrulha o ID daquela estrutura [(id, nome...)]
                    valor = sala_busca[0][0]

                # --- NOVO: Tratamento para converter Nome de Usuário em ID ---
                elif atributo.lower() == "usuario":
                    usuario_busca = self.userServ.buscaUsuario(valor)
                    if not usuario_busca:
                        raise Exception(f"Usuário '{valor}' não foi encontrado no banco!")
                    # Desembrulha o ID daquela estrutura [(id, nome...)]
                    valor = usuario_busca[0][0]

                # Agora o 'valor' já virou o número inteiro correto (ID) antes de ir para o banco!
                self.repoAloc.editar_alocacao_principal(coluna_mysql, valor, id_alocacao)
                return f"Sucesso! O campo '{atributo}' da alocação #{id_alocacao} foi atualizado para o ID {valor}."     

    def removerAlocacao(self, id_alocacao):
        self.repoAloc.deletar_alocacao(id_alocacao)

    
alocacaoService = AlocacacaoService(repoAlocacao, salaService, userService)
    
    
    