from repositories.alocacaoRepository import repoAlocacao
from services.userService import userService
from services.salaService import salaService
class AlocacacaoService: 
    def __init__(self, repoAlocacao, userService, salaService):
        self.repoAloc = repoAlocacao
        self.userServ = userService
        self.salaServ = salaService

    def cadastrarAlocacao(self,data_hora_inicio, data_hora_fim, qtd_ap, listIDs_aparelho:list, user, sala):

        usuario = self.userServ.buscaUsuario(user)
        salaFinal = sala.buscabuscarSalas(sala)

        for i in range(qtd_ap-1):
            self.repoAloc.inserir_Alocacao(usuario,listIDs_aparelho[i],usuario,salaFinal)
        
        pass

    def listarAlocacao(self):
        alocacoes = self.repoAloc.Listar_Alocacao()

        print("\n======================= RELATÓRIO DE ALOCAÇÕES =======================")

        for registro in alocacoes:
            # Desempacota cada coluna na ordem exata do seu SELECT
            id_alocacao, usuario, patrimonio, marca, modelo, sala, dt_alocacao, dt_devolucao = registro
            
            # Formata uma linha única e organizada para cada registro
            print(f"Alocação #{id_alocacao} | {usuario} | Sala: {sala}")
            print(f"  └─ Disp: [{patrimonio}] {marca} {modelo}")
            print(f"  └─ Período: {dt_alocacao} até {dt_devolucao}")
            print("-" * 70) # Linha separadora discreta entre uma alocação e outra

        print("======================================================================")

        pass

    def buscarAlocacao(self, id):
        validacao = self.repoAloc.Buscar_Alocacao(id)
        if not validacao:
            return "ID inválido!"
        
        else:
            return

    def editarAlocacao(self):
        pass

    def removerAlocacao(self):
        pass


        


        
    
        
alocacaoServ = AlocacacaoService(repoAlocacao)
        