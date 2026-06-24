import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

class gerenciarSalaView:

    def gerenciar_sala(self):
        while True:
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- GERENCIAR SALAS ---\n{CORES['RESET']}")

            opcao = questionary.select(
                "Selecione uma opção:",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=[
                    "Ver Salas Cadastradas",
                    "Criar Nova Sala",
                    "Editar Salas",
                    "Deletar Salas",
                    "Voltar"                
                ]
            ).ask()

            if opcao == "Ver Salas Cadastradas":
                print("Visualizar Reservas em desenvolvimento")
                input("enter")
            elif opcao == "Criar Nova Sala":
                print(" Gerenciar reservas em desenvolvimento")
                input("enter")
            elif opcao == "Editar Salas": 
                print("Gerenciar aparelhos em desenvolvimento")
                input("enter")
            elif opcao == "Deletar Salas":
                print("Manutenção em desenvolvimento")
                input("enter")
            elif opcao == "Voltar":
                break