import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

from views.criarNovaReserva import criarNovaReservaView
from services.alocacaoService import alocacaoService
from views.editarReservaView import editarReservaView
from views.deletarReservaView import deletarReservaView
class gerenciarReservasView:

    def gerenciar_reservas(self):
        while True:
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- GERENCIAR RESERVAS ---\n{CORES['RESET']}")

            opcao = questionary.select(
                "Selecione uma opção:",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=[
                    "Ver Reservas (por ID)",
                    "Criar Nova Reserva",
                    "Editar Reservas",
                    "Deletar Reservas",
                    "Voltar"                
                ]
            ).ask()

            if opcao == "Ver Reservas (por ID)":
                print(alocacaoService.listarAlocacao())
                input(f"{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            elif opcao == "Criar Nova Reserva":
                criarNovaReservaView().criar_reserva()
            elif opcao == "Editar Reservas": 
                editarReservaView().editar_Reserva()
            elif opcao == "Deletar Reservas":
                deletarReservaView().deletar_Reserva()
            elif opcao == "Voltar":
                break