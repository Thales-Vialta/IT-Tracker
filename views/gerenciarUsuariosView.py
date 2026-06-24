import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

class gerenciarUsuariosView:

    def gerenciar_usuarios(self):
        while True:
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- GERENCIAR USUÁRIOS ---\n{CORES['RESET']}")

            opcao = questionary.select(
                "Selecione uma opção:",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=[
                    "Ver Usuários Cadastrados",
                    "Criar Novo Usuário",
                    "Editar Usuários",
                    "Deletar Usuários",
                    "Voltar"                
                ]
            ).ask()

            if opcao == "Ver Usuários Cadastrados":
                print("Visualizar Reservas em desenvolvimento")
                input("enter")
            elif opcao == "Criar Novo Usuário":
                print(" Gerenciar reservas em desenvolvimento")
                input("enter")
            elif opcao == "Editar Usuários": 
                print("Gerenciar aparelhos em desenvolvimento")
                input("enter")
            elif opcao == "Deletar Usuários":
                print("Manutenção em desenvolvimento")
                input("enter")
            elif opcao == "Voltar":
                break