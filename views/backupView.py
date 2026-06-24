import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

class backupView:

    def backup(self):
        while True:
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- BACKUP ---\n{CORES['RESET']}")

            opcao = questionary.select(
                "Deseja fazer um backup dos seus dados?",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=[
                    "Sim",
                    "Não",                
                ]
            ).ask()

            if opcao == "Sim":
                print("Fazendo backup de dados...")
                input("enter")
            elif opcao == "Não":
                break