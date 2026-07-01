import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

from views.gerenciarModelosView import gerenciarModelosView
from views.criarNovoDispositivo import criarNovoDispositivoView 
from views.editarDispositivosView import editarDispositivosView
from services.AparelhoService import aparelhoService

class gerenciarDispositivosView:

    def gerenciar_dispositivos(self):
        while True:
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}---- GERENCIAR DISPOSITIVOS ----\n{CORES['RESET']}")

            opcao = questionary.select(
                "Selecione uma opção:",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=[
                    "Gerenciar Modelos",
                    "Mudar Status do Dispositivo",
                    "Ver Dispositivos Cadastrados",
                    "Criar Novo Dispositivo",
                    "Editar Dispositivos",
                    "Deletar Dispositivos",
                    "Voltar"                
                ]
            ).ask()

            if opcao == "Gerenciar Modelos":
                gerenciarModelosView().gerenciar_modelos()
            elif opcao == "Mudar Status do Dispositivo":
                print("Gerenciar aparelhos em desenvolvimento")
                input("enter")
            elif opcao == "Ver Dispositivos Cadastrados":
                print(aparelhoService.listar_aparelhos())    
                input(f"{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            elif opcao == "Criar Novo Dispositivo":
                criarNovoDispositivoView().criar_dispositivo()
            elif opcao == "Editar Dispositivos":             
                editarDispositivosView().editar_dispositivo()
            elif opcao == "Deletar Dispositivos":
                print("Manutenção em desenvolvimento")
                input("enter")
            elif opcao == "Voltar":
                break