import questionary
from os import system
from views.cores import CORES
from views.cores import minhas_cores
from services.alocacaoService import alocacaoService

class visualizarReservasView:
    def visualizarReservas(self):
        print(alocacaoService.listarAlocacao())
        input(f"{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")