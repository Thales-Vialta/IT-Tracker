import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

class gerenciarModelosView:

    def gerenciar_modelos(self):
        while True:
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- GERENCIAR MODELOS ---\n{CORES['RESET']}")

            opcao = questionary.select(
                "Selecione uma opção:",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=[
                    "Ver Modelos Cadastrados",
                    "Criar Novo Modelo",
                    "Editar Modelos",
                    "Deletar Modelos",
                    "Voltar"                
                ]
            ).ask()

            if opcao == "Ver Modelos Cadastrados":
                print("Visualizar Reservas em desenvolvimento")
                input("enter")
            elif opcao == "Criar Novo Modelo":
                print(" Gerenciar reservas em desenvolvimento")
                input("enter")    
            elif opcao == "Editar Modelos":
                print(" Gerenciar reservas em desenvolvimento")
                input("enter")
            elif opcao == "Ver Modelos Cadastrados": 
                print("Gerenciar aparelhos em desenvolvimento")
                input("enter")
            elif opcao == "Deletar Modelos":
                print("Manutenção em desenvolvimento")
                input("enter")
            elif opcao == "Voltar":
                break