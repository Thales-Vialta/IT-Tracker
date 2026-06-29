from models.aparelhos import Aparelhos 
from repositories.statusRepository import repo
class StatusService: 

    def __init__(self, repo):
        self.status_repo = repo
    def MudarStatus(self, idStatus:int,idAparelho:int): 
        self.status_repo.MudarStatus(idStatus,idAparelho)
        if idStatus not in [1, 2, 3]:
            return ValueError("Status inválido.")
        else:
            self.status_repo.MudarStatus(idStatus, idAparelho)
            return f"Status do Aparelho ID:{idAparelho} mudou o resultado"
StatusService = StatusService(repo)
    