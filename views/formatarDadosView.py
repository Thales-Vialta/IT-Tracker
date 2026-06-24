import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

class formatarDadosView:

    def formatar_dados(self):
        while True:
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- FORMATAR DADOS ---\n{CORES['RESET']}")

            opcao = questionary.select(
                "Deseja formatar todos os seus dados?",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=[
                    "Sim",
                    "Não",                
                ]
            ).ask()

            if opcao == "Sim":
                opcao = questionary.select(
                    "\nESSA AÇÃO NÃO PODERÁ SER DESFEITA. \nTEM CERTEZA QUE QUER FORMATAR SEUS DADOS?",
                    instruction=" ",
                    qmark=" ",
                    choices=[
                        "Sim, quero formatar meus dados",
                        "Não, não quero formatar meus dados",                
                    ]
                ).ask()

                if opcao == "Sim, quero formatar meus dados":
                    print("Formatando seus dados...")
                    input()
                
                elif opcao == "Não, não quero formatar meus dados":
                    break

            elif opcao == "Não":
                break