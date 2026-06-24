import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

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
                    "Deletar Usuários",
                    "Voltar"                
                ]
            ).ask()

            if opcao == "Ver Reservas (por ID)":
                print("Visualizar Reservas em desenvolvimento")
                input("enter")
            elif opcao == "Criar Nova Reserva":
                print(" Gerenciar reservas em desenvolvimento")
                input("enter")
            elif opcao == "Editar Reservas": 
                print("Gerenciar aparelhos em desenvolvimento")
                input("enter")
            elif opcao == "Deletar Reservas":
                print("Manutenção em desenvolvimento")
                input("enter")
            elif opcao == "Voltar":
                break