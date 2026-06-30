import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.ModeloService import modeloServ

class editarModelosView:

    def editar_modelo(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- EDITAR MODELO ---\n{CORES['RESET']}")

        modelos_banco = modeloServ.modeloReposit.buscar_Modelo("%")

        if not modelos_banco:
            print(f"{CORES['VERMELHO']}Nenhum modelo cadastrado no sistema!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_modelos = []
        for id_mod, marca, nome_modelo in modelos_banco:
            linha_opcao = f"{marca} {nome_modelo} (ID: {id_mod})"
            opcoes_modelos.append(linha_opcao)

        opcoes_modelos.append("Cancelar")

        modelo_selecionado = questionary.select(
            "Selecione qual modelo você deseja editar:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_modelos
        ).ask()

        if modelo_selecionado == "Cancelar" or not modelo_selecionado:
            return

        modelo_antigo = modelo_selecionado.split(" (ID:")[0]
        modelo_puro_antigo = modelo_selecionado.split(" ")[1].split(" (ID:")[0]

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- NOVO NOME PARA: {modelo_antigo} ---\n{CORES['RESET']}")

        novo_nome = questionary.text(
            "Digite o novo nome para este modelo:",
            style=minhas_cores,
            qmark=" ",
        ).ask()

        if not novo_nome or novo_nome.strip() == "":
            print(f"{CORES['VERMELHO']}Nome inválido! Operação cancelada.{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        modelo_tratado = novo_nome.strip()

        if modeloServ.buscarModelo(modelo_tratado):
            print(f"\n{CORES['VERMELHO']}Erro: Já existe um modelo cadastrado com o nome '{modelo_tratado}'!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- ATUALIZANDO NO BANCO ---\n{CORES['RESET']}")
        
        resultado = modeloServ.editarModelo(modelo_puro_antigo, "Modelo", modelo_tratado)

        limpar_tela()
        print(f"\n{resultado}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")