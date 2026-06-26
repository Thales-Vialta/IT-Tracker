import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.salaService import salaService

class criarNovaSalaView:

    def criar_sala(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- CADASTRAR NOVA SALA ---\n{CORES['RESET']}")

        nome_sala = questionary.text(
            "Digite o nome da nova sala:",
            style=minhas_cores,
            qmark=" ",
        ).ask()

        if not nome_sala or nome_sala == "":
            print(f"{CORES['VERMELHO']}Nome da sala inválido{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return
        
        if not salaService.existeSala(nome_sala):
            print(f"\n{CORES['NEGRITO']}{nome_sala}{CORES['RESET']}{CORES['VERMELHO']} já está cadastrado no sistema!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return
        
        endereco_sala = questionary.text(
            "Digite o endereço da sala (ex: Bloco A - 2º Andar):",
            style=minhas_cores,
            qmark=" ",
        ).ask()

        if not endereco_sala or endereco_sala == "":
            print(f"{CORES['VERMELHO']}Endereço inválido!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return
        
        resultado = salaService.cadastrarSalas(nome_sala, endereco_sala)
         
        limpar_tela()
        print(f"\n{CORES['NEGRITO']}{nome_sala}{CORES['RESET']} {CORES['VERDE']}cadastrada com sucesso!{CORES['RESET']}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")