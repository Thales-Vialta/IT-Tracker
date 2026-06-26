from models.horario import Horario
from repositories.horarioRepository import horarioRepo

from views.limparTela import limpar_tela
from views.cores import CORES

class horarioService:

    def __init__(self, horario_repository):
        self.horario_repo = horario_repository

    def listarHorarios(self):
        limpar_tela()

        hora = self.horario_repo.Listar_Horario()

        resultado = f"{CORES['AZUL']}{CORES['NEGRITO']}---- LISTA DE HORÁRIOS ----\n\n{CORES['RESET']}"

        for HoraInicio, HoraFim, Descricao in hora:
            inicio_str = str(HoraInicio)
            fim_str = str(HoraFim)
            periodo = f"{inicio_str} - {fim_str}"

            desc_format = Descricao.ljust(30)

            resultado += f"{CORES['AMARELO']}{CORES['NEGRITO']}{desc_format} | {CORES['RESET']} {CORES['RESET']} {periodo}\n"

        return resultado

horarioService = horarioService(horarioRepo)