import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

from services.salaService import salaService
from views.criarNovaSalaView import criarNovaSalaView
from views.editarSalaView import editarSalaView
from views.removerSalaView import removerSalaView

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
                print(salaService.listarSalas())
                input(f"{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            elif opcao == "Criar Nova Sala":
                criarNovaSalaView().criar_sala()
            elif opcao == "Editar Salas": 
                editarSalaView().editar_sala()
            elif opcao == "Deletar Salas":
                removerSalaView().remover_sala()
            elif opcao == "Voltar":
                break