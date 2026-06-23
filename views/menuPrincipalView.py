import questionary
from os import system

class menuPrincipalView:
    def limpar_tela (self):
        system('cls')

    def titulo(self):
        it_tracker_logo = """
        ██  ███████     ████████  ███████   ██████    ███████  ██   ██  ████████  ███████  
        ██     ██          ██     ██   ██  ██    ██  ██        ██  ██   ██        ██   ██  
        ██     ██          ██     ███████  ████████  ██        █████    ██████    ███████  
        ██     ██          ██     ██  ██   ██    ██  ██        ██  ██   ██        ██  ██   
        ██     ██          ██     ██   ██  ██    ██   ██████   ██   ██  ████████  ██   ██  
        """
        print(it_tracker_logo)

    def menu_principal(self):
        while True:
            self.limpar_tela()
            self.titulo()

            opcao = questionary.select(
                "Selecione uma opção:",
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
                print("Visualizar Reservas em desenvolvimento")
                input("enter")
            elif opcao == "Gerenciar Reservas":
                print(" Gerenciar reservas em desenvolvimento")
                input("enter")
            elif opcao == "Gerenciar Dispositivos":
                print("Gerenciar aparelhos em desenvolvimento")
                input("enter")
            elif opcao == "Manutenção":
                print("Manutenção em desenvolvimento")
                input("enter")
            elif opcao == "Configurações":
                print("Configurações em desenvolvimento")
                input("enter")
            elif opcao == "Sair":
                print("Saindo")
                break

