from repositories.alocacaoRepository import repoAlocacao

class AlocacacaoService: 
    def __init__(self, repoAlocacao):
        self.repoAloc = repoAlocacao
        pass

    def cadastrarAlocacao(self):
        pass

    def listarAlocacao(self):
        pass

    def buscarAlocacao(self):
        pass

    def editarAlocacao(self):
        pass

    def removerAlocacao(self):
        pass

    def validarAlocacao(self,inicio,fim):
        validacao = self.repoAloc.Listar_Alocacao_Gap_Data(inicio,fim)

        if validacao:
            #não pode alocar
            return False
        
        else:
            #vai na fé
            return True
        
    
        
alocacaoServ = AlocacacaoService(repoAlocacao)
        