import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

from views.criarNovaMarcaView import criarMarcaView
from views.editarMarcaView import editarMarcaView
from views.removerMarcaView import removerMarcaView

from services.marcaService import marcaServ

class gerenciarMarcaView:

    def gerenciar_marca(self):
        while True:
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- GERENCIAR MARCAS ---\n{CORES['RESET']}")

            opcao = questionary.select(
                "Selecione uma opção:",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=[                    
                    "Ver Marcas Cadastradas",
                    "Criar Nova Marca",
                    "Editar Marcas",
                    "Deletar Marcas",
                    "Voltar"                
                ]
            ).ask()

            if opcao == "Ver Marcas Cadastradas":
                print(marcaServ.listarMarcas())
                input(f"{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            elif opcao == "Criar Nova Marca":
                criarMarcaView().criar_marca()
            elif opcao == "Editar Marcas":
                editarMarcaView().editar_marca()
            elif opcao == "Deletar Marcas": 
                removerMarcaView().remover_marca()
            elif opcao == "Voltar":
                break