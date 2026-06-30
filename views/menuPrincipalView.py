import questionary
from os import system
from views.cores import CORES
from views.cores import minhas_cores
from views.limparTela import limpar_tela

from views.configView import configView
from views.visualReservasView import visualizarReservasView
from views.gerenciarReservasView import gerenciarReservasView 
from views.gerenciarDispositivosView import gerenciarDispositivosView
from views.manutencaoView import ManutencaoView

from services.ManutencaoService import manutencaoServe

class menuPrincipalView:
    def titulo(self):
        it_tracker_logo = """
        ██  ███████     ████████  ███████   ██████    ███████  ██   ██  ████████  ███████  
        ██     ██          ██     ██   ██  ██    ██  ██        ██  ██   ██        ██   ██  
        ██     ██          ██     ███████  ████████  ██        █████    ██████    ███████  
        ██     ██          ██     ██  ██   ██    ██  ██        ██  ██   ██        ██  ██   
        ██     ██          ██     ██   ██  ██    ██   ██████   ██   ██  ████████  ██   ██  
        """
        print(f"{CORES['AZUL']}{it_tracker_logo}{CORES['RESET']}")

    def menu_principal(self):
        while True:
            limpar_tela()
            self.titulo()

            total_tupla = manutencaoServe.obter_quantidade_em_manutencao()
            total = total_tupla[0] if total_tupla else 0
            texto_manutencao = f"Manutenção ({total})"

            opcao = questionary.select(
                "Selecione uma opção:",
                instruction=" ",
                qmark="",
                style=minhas_cores,
                choices=[
                    "Visualizar Reservas",
                    "Gerenciar Reservas",
                    "Gerenciar Dispositivos",
                    texto_manutencao,
                    "Configurações",
                    "Sair"                
                ]
            ).ask()

            if opcao == "Visualizar Reservas":
                visualizarReservasView().visualizarReservas()
            elif opcao == "Gerenciar Reservas":
                gerenciarReservasView().gerenciar_reservas()
            elif opcao == "Gerenciar Dispositivos":
                gerenciarDispositivosView().gerenciar_dispositivos()
            elif opcao and opcao.startswith("Manutenção"):
                ManutencaoView().manutencao()
            elif opcao == "Configurações":
                configView().config()
            elif opcao == "Sair":
                print("Saindo")
                break
