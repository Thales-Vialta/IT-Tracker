from repositories.alocacaoRepository import repoAlocacao
from services.userService import userService
from services.salaService import salaService

class AlocacacaoService: 
    def __init__(self, repoAlocacao, salaService, userService):
        self.repoAloc = repoAlocacao
        self.salaServ = salaService
        self.userServ = userService

    def cadastrarAlocacao(self, data_hora_inicio, data_hora_fim, listIDs_aparelho: list, user, sala):
        usuario = self.userServ.buscaUsuario(user)
        salaFinal = self.salaServ.buscarSalas(sala)
        
        id_gerado = self.repoAloc.inserir_alocacao(usuario, listIDs_aparelho, salaFinal, data_hora_inicio, data_hora_fim)
        
        return f"Sucesso! Alocação #{id_gerado} gerada com {len(listIDs_aparelho)} dispositivo(s)."
        
   

    def listarAlocacao(self):
        alocacoes = self.repoAloc.listar_alocacoes()

        print("\n======================= RELATÓRIO DE ALOCAÇÕES =======================")

        for registro in alocacoes:
            # CORREÇÃO: Variáveis na ordem EXATA das colunas do seu SELECT
            id_alocacao, usuario, sala, dt_alocacao, dt_devolucao, patrimonios, aparelhos = registro
            
            # Formata o relatório organizando os dados agrupados pelo GROUP_CONCAT
            print(f"Alocação ID: #{id_alocacao} | Usuário: {usuario}")
            print(f"  ├─ Local: {sala}")
            print(f"  ├─ Patrimônio(s): [{patrimonios}]")
            print(f"  ├─ Aparelho(s):   {aparelhos}")
            print(f"  └─ Período:       {dt_alocacao} até {dt_devolucao}")
            print("-" * 70) 

        print("======================================================================")


    def buscarAlocacao(self, id_alocacao, usuario):
        validacao = self.repoAloc.buscar_alocacao(id_alocacao)
        texto_retorno = f"=================== RESULTADO DA BUSCA (ID: {id_alocacao}) ===================\n"

        if not validacao:
            texto_retorno = "Nenhuma alocação encontrada com este ID.\n"
        else:
            
            id_alocacao, id_aparelho, id_usuario, id_sala, data_alocacao, data_devolucao = validacao
            
            texto_retorno += f"Alocação: {usuario}\n"
            texto_retorno += f"  ├─ ID do Usuário:  {id_usuario}\n"
            texto_retorno += f"  ├─ ID do Aparelho: {id_aparelho}\n"
            texto_retorno += f"  ├─ ID da Sala:     {id_sala}\n"
            texto_retorno += f"  ├─ Data Início:    {data_alocacao}\n"
            texto_retorno += f"  └─ Data Devolução: {data_devolucao}\n"
            texto_retorno += "-" * 60 + "\n"
            texto_retorno += "===================================================================="
            
        return texto_retorno

    def editarAlocacao(self, id, atributo, valor, qtd=None):
        if atributo == "Aparelho":
            for i in range(qtd):
                self.repoAloc.editar_alocacao(atributo, valor[i], id)
        else:
            self.repoAloc.editar_alocacao(atributo, valor, id)

    def removerAlocacao(self, id_alocacao):
        self.repoAloc.deletar_alocacao(id_alocacao)
    
