from models.horario import Horario
from repositories.horarioRepository import HorarioRepository

class horarioService:

    def __init__(self, horario_repository):
        self.horario_repo = horario_repository

    def listarHorarios(self):
        hora = self.horario_repo.Listar_Horario()
        resultado = "+==========Lista de Horários==========+\n"

        # Agora sim, fazemos o laço FOR de verdade para rodar cada registro do banco
        for HoraInicio, HoraFim, Descricao in hora:
        # Usamos uma f-string para encaixar as variáveis no texto
            resultado += f"{Descricao} | {HoraInicio} - {HoraFim}\n"

        return resultado