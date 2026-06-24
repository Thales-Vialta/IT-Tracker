import questionary
from os import system
from views.cores import CORES
from views.cores import minhas_cores
from views.limparTela import limpar_tela
from views.configView import configView
from views.visualReservasView import visualizarReservasView

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

            opcao = questionary.select(
                "Selecione uma opção:",
                instruction=" ",
                qmark="",
                style=minhas_cores,
                choices=[
                    "Visualizar Reservas",
                    "Gerenciar Reservas",
                    "Gerenciar Dispositivos",
                    "Manutenção",
                    "Configurações",
                    "Sair"                
                ]
            ).ask()

            if opcao == "Visualizar Reservas":
                from views.visualReservasView import visualizarReservasView 
                visualizarReservasView().visualizarReservas()
            elif opcao == "Gerenciar Reservas":
                from views.gerenciarReservasView import gerenciarReservasView 
                gerenciarReservasView().gerenciar_reservas()
            elif opcao == "Gerenciar Dispositivos":
                from views.gerenciarDispositivosView import gerenciarDispositivosView 
                gerenciarDispositivosView().gerenciar_dispositivos()
            elif opcao == "Manutenção":
                print("Manutenção em desenvolvimento")
                input("enter")
            elif opcao == "Configurações":
                from views.configView import configView  
                configView().config()
            elif opcao == "Sair":
                print("Saindo")
                break
