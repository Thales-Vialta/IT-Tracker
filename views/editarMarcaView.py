import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.marcaService import marcaServ

class editarMarcaView:

    def editar_marca(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- EDITAR MARCA EXISTENTE ---\n{CORES['RESET']}")

        marcas_banco = marcaServ.marcaReposit.listar_Marcas()

        if not marcas_banco:
            print(f"{CORES['VERMELHO']}Nenhuma marca cadastrada no sistema para editar!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_marcas = []
        for id_marca, nome_marca in marcas_banco:
            linha_opcao = f"{nome_marca} (ID: {id_marca})"
            opcoes_marcas.append(linha_opcao)

        opcoes_marcas.append("Cancelar")

        marca_selecionada = questionary.select(
            "Selecione qual marca você deseja editar:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_marcas
        ).ask()

        if marca_selecionada == "Cancelar" or not marca_selecionada:
            return

        marca_antiga = marca_selecionada.split(" (ID:")[0]

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- NOVO NOME PARA: {marca_antiga} ---\n{CORES['RESET']}")

        novo_nome = questionary.text(
            "Digite o novo nome para esta marca:",
            style=minhas_cores,
            qmark=" ",
        ).ask()

        if not novo_nome or novo_nome.strip() == "":
            print(f"{CORES['VERMELHO']}Nome inválido!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        marca_tratada = novo_nome.strip()

        if marcaServ.buscarMarca(marca_tratada):
            print(f"\n{CORES['VERMELHO']}Erro: Já existe uma marca cadastrada com o nome '{marca_tratada}'!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return
        
        resultado = marcaServ.editarMarca(marca_antiga, "NomeMarca", marca_tratada)

        limpar_tela()

        print(f"\n{CORES['VERDE']}{resultado}{CORES['RESET']}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")