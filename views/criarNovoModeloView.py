import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.modeloService import modeloServ
from services.marcaService import marcaServ 

class criarNovoModeloView:

    def criar_modelo(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- CADASTRAR NOVO MODELO ---\n{CORES['RESET']}")

        marcas_banco = marcaServ.marcaReposit.listar_Marcas()

        if not marcas_banco:
            print(f"{CORES['VERMELHO']}Nenhuma marca cadastrada no sistema! Cadastre uma marca primeiro.{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_marcas = []
        for id_marca, nome_marca in marcas_banco:
            linha_opcao = f"{nome_marca} (ID: {id_marca})"
            opcoes_marcas.append(linha_opcao)

        opcoes_marcas.append("Cancelar")

        marca_selecionada = questionary.select(
            "Selecione a marca do modelo:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_marcas
        ).ask()

        if marca_selecionada == "Cancelar" or not marca_selecionada:
            return

        id_marca_escolhida = int(marca_selecionada.split(" (ID: ")[1].replace(")", ""))

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- CADASTRAR NOVO MODELO ---\n{CORES['RESET']}")

        nome_modelo = questionary.text(
            "Digite o nome do novo modelo:",
            style=minhas_cores,
            qmark=" ",
        ).ask()

        if not nome_modelo or nome_modelo.strip() == "":
            print(f"{CORES['VERMELHO']}Nome do modelo inválido!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        modelo_tratado = nome_modelo.strip()

        if modeloServ.buscarModelo(modelo_tratado):
            print(f"\n{CORES['NEGRITO']}{modelo_tratado}{CORES['RESET']}{CORES['VERMELHO']} já está cadastrado no sistema!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        resultado = modeloServ.cadastrarModelo(id_marca_escolhida, modelo_tratado)
         
        limpar_tela()
        print(f"\n{CORES['NEGRITO']}{modelo_tratado}{CORES['RESET']}{CORES['VERDE']}{resultado}{CORES['RESET']}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")