import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

from views.gerenciarMarcaView import gerenciarMarcaView
from views.editarModeloView import editarModelosView

from services.modeloService import modeloServ

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
                    "Gerenciar Marca dos Modelos",
                    "Ver Modelos Cadastrados",
                    "Criar Novo Modelo",
                    "Editar Modelos",
                    "Deletar Modelos",
                    "Voltar"                
                ]
            ).ask()

            if opcao == "Gerenciar Marca dos Modelos":
                gerenciarMarcaView().gerenciar_marca()
            elif opcao == "Ver Modelos Cadastrados":
                print(modeloServ.listarModelos())
                input(f"{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            elif opcao == "Criar Novo Modelo":
                print(" Gerenciar reservas em desenvolvimento")
                input("enter")    
            elif opcao == "Editar Modelos":
               editarModelosView().editar_modelo()
            elif opcao == "Ver Modelos Cadastrados": 
                print("Gerenciar aparelhos em desenvolvimento")
                input("enter")
            elif opcao == "Deletar Modelos":
                print("Manutenção em desenvolvimento")
                input("enter")
            elif opcao == "Voltar":
                break