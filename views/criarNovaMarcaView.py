import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.marcaService import marcaServ

class criarMarcaView:

    def criar_marca(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- CADASTRAR NOVA MARCA ---\n{CORES['RESET']}")

        nome_marca = questionary.text(
            "Digite o nome da marca que deseja cadastrar (ex: Dell, Apple):",
            style=minhas_cores,
            qmark=" ",
        ).ask()

        if not nome_marca or nome_marca.strip() == "":
            print(f"\n{CORES['VERMELHO']}Operação cancelada: O nome da marca não pode ser vazio!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        marca_tratada = nome_marca.strip()

        if marcaServ.buscarMarca(marca_tratada):
            print(f"\n{CORES['VERMELHO']}Erro: A marca '{marca_tratada}' já está cadastrada no sistema!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        limpar_tela()

        resultado = marcaServ.cadastrarMarca(marca_tratada)
        
        if "sucesso" in resultado:
            print(f"\n{CORES['VERDE']}Marca '{marca_tratada}'{resultado}{CORES['RESET']}")
        else:
            print(f"\n{CORES['VERMELHO']}Erro: Marca '{marca_tratada}'{resultado}{CORES['RESET']}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")