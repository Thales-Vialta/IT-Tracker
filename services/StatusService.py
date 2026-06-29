from repositories.statusRepository import repo

class StatusService:

    def __init__(self, repo):
        self.status_repo = repo

    def MudarStatus(self, idStatus: int, idAparelho: int):
        if idStatus not in [1, 2, 3]:
            raise ValueError("Status inválido.")
        self.status_repo.editar_status(idAparelho, idStatus)

        modelo, status = self.status_repo.Mostrar_Novo_Status(idAparelho,)
        return f"Status do Aparelho '{modelo}' alterado com sucesso Para '{status}'."


    def listar_manutencao(self):
        aparelhos = self.status_repo.Listar_Defeituosos()

        if not aparelhos:
            return "Não há aparelhos em manutenção."

        return aparelhos