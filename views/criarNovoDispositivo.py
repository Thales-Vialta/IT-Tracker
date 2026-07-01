import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.AparelhoService import aparelhoService
from services.modeloService import modeloServ  # Precisamos listar os modelos existentes

class criarNovoDispositivoView:

    def criar_dispositivo(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- CADASTRAR NOVO DISPOSITIVO ---\n{CORES['RESET']}")

        modelos_banco = modeloServ.modeloReposit.buscar_Modelo("%")

        if not modelos_banco:
            print(f"{CORES['VERMELHO']}Nenhum modelo cadastrado no sistema! Cadastre um modelo primeiro.{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_modelos = []
        for id_mod, marca, nome_modelo in modelos_banco:
            linha_opcao = f"{nome_modelo} (ID: {id_mod})"
            opcoes_modelos.append(linha_opcao)

        opcoes_modelos.append("Cancelar")

        modelo_selecionado = questionary.select(
            "Selecione o modelo do novo dispositivo:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_modelos
        ).ask()

        if modelo_selecionado == "Cancelar" or not modelo_selecionado:
            return

        id_modelo_escolhido = int(modelo_selecionado.split(" (ID: ")[1].replace(")", ""))

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- CADASTRAR NOVO DISPOSITIVO ---\n{CORES['RESET']}")

        serial_dispositivo = questionary.text(
            "Digite o número de patrimônio (Serial) do dispositivo:",
            style=minhas_cores,
            qmark=" ",
        ).ask()

        if not serial_dispositivo or serial_dispositivo.strip() == "":
            print(f"{CORES['VERMELHO']}Número de patrimônio inválido!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        serial_tratado = serial_dispositivo.strip()

        limpar_tela()

        resultado = aparelhoService.cadastrar_aparelho(serial_tratado, 1, id_modelo_escolhido)

        if "Erro" in resultado:
            print(f"\n{CORES['VERMELHO']}{resultado}{CORES['RESET']}")
        else:
            print(f"\n{CORES['VERDE']}{resultado}{CORES['RESET']}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")