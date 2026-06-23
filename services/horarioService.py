from models.horario import Horario
from repositories.horarioRepository import HorarioRepository

class horarioService:

    def __init__(self, horario_repository):
        self.horario_repo = horario_repository

    def listarHorarios(self):
        return self.horario_repo.Listar_Horario()