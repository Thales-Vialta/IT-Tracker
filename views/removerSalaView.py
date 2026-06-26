import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.salaService import salaService

class removerSalaView:
    
    def remover_sala(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- REMOVER SALA ---\n{CORES['RESET']}")

        nome_sala = questionary.text(
            "Digite o nome da sala que deseja remover:",
            style=minhas_cores,
            qmark=" "
        ).ask()

        if not nome_sala or nome_sala.strip() == "":
            print(f"{CORES['VERMELHO']}Nome não pode ser vazio!{CORES['RESET']}")
            input("\nVoltar...")
            return

        if salaService.existeSala(nome_sala):
            print(f"\n{CORES['VERMELHO']}Sala não encontrada!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        confirmar = questionary.select(
            f"\nDeseja remover {nome_sala}?",
            instruction=" ",
            style=minhas_cores,
            qmark=" ",
            choices=["Sim", "Não"]
        ).ask()

        if confirmar == "Sim":
            validacao = salaService.removerSalas(nome_sala)
            limpar_tela()
            print(f"\n{CORES['NEGRITO']}{nome_sala}{CORES['RESET']} {CORES['VERDE']}{validacao}{CORES['RESET']}")
        else:
            limpar_tela()
            print(f"\n{CORES['AMARELO']}Operação cancelada pelo usuário.{CORES['RESET']}")
        
        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")