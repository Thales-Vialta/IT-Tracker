import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

class gerenciarDispositivosView:

    def gerenciar_dispositivos(self):
        while True:
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- GERENCIAR DISPOSITIVOS ---\n{CORES['RESET']}")

            opcao = questionary.select(
                "Selecione uma opção:",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=[
                    "Ver Dispositivos Cadastrados",
                    "Criar Novo Dispositivo",
                    "Editar Dispositivos",
                    "Deletar Dispositivos",
                    "Voltar"                
                ]
            ).ask()

            if opcao == "Ver Dispositivos Cadastrados":
                print("Visualizar Reservas em desenvolvimento")
                input("enter")
            elif opcao == "Criar Novo Dispositivo":
                print(" Gerenciar reservas em desenvolvimento")
                input("enter")
            elif opcao == "Editar Dispositivos": 
                print("Gerenciar aparelhos em desenvolvimento")
                input("enter")
            elif opcao == "Deletar Dispositivos":
                print("Manutenção em desenvolvimento")
                input("enter")
            elif opcao == "Voltar":
                break