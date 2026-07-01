import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.marcaService import marcaServ

class removerMarcaView:

    def remover_marca(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- REMOVER MARCA ---\n{CORES['RESET']}")

        marcas_banco = marcaServ.marcaReposit.listar_Marcas()

        if not marcas_banco:
            print(f"{CORES['VERMELHO']}Nenhuma marca cadastrada!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_marcas = []
        for id_marca, nome_marca in marcas_banco:
            linha_opcao = f"{nome_marca} (ID: {id_marca})"
            opcoes_marcas.append(linha_opcao)

        opcoes_marcas.append("Cancelar")

        marca_selecionada = questionary.select(
            "Selecione qual marca você deseja remover:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_marcas
        ).ask()

        if marca_selecionada == "Cancelar" or not marca_selecionada:
            return

        marca_alvo = marca_selecionada.split(" (ID:")[0]

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- CONFIRMAÇÃO DE EXCLUSÃO ---\n{CORES['RESET']}")
        print(f"Você selecionou a marca: {CORES['AMARELO']}{marca_alvo}{CORES['RESET']}\n")

        confirmar = questionary.select(
            f"Tem certeza de que deseja excluir permanentemente a marca?",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=["Sim", "Não"]
        ).ask()

        if confirmar == "Sim":
            limpar_tela()
            
            resultado = marcaServ.removerMarca(marca_alvo)
            
            limpar_tela()
            
            if "sucesso" in resultado:
                print(f"\n{CORES['VERDE']}Marca '{marca_alvo}'{resultado}{CORES['RESET']}")
            elif "vinculada" in resultado:
                print(f"\n{CORES['AMARELO']}Aviso: Marca '{marca_alvo}'{resultado}{CORES['RESET']}")
            else:
                print(f"\n{CORES['VERMELHO']}Erro: Marca '{marca_alvo}'{resultado}{CORES['RESET']}")
        else:
            limpar_tela()
            print(f"{CORES['AMARELO']}Operação de exclusão cancelada pelo usuário.{CORES['RESET']}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")