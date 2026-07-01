import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.modeloService import modeloServ

class removerModelosView:

    def remover_modelo(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- REMOVER MODELO EXISTENTE ---\n{CORES['RESET']}")

        modelos_banco = modeloServ.modeloReposit.buscar_Modelo("%")

        if not modelos_banco:
            print(f"{CORES['VERMELHO']}Nenhum modelo cadastrado!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_modelos = []
        for id_mod, marca, nome_modelo in modelos_banco:
            linha_opcao = f"{nome_modelo} (ID: {id_mod})"
            opcoes_modelos.append(linha_opcao)

        opcoes_modelos.append("Cancelar")

        modelo_selecionado = questionary.select(
            "Selecione qual modelo você deseja remover:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_modelos
        ).ask()

        if modelo_selecionado == "Cancelar" or not modelo_selecionado:
            return

        id_modelo_alvo = int(modelo_selecionado.split(" (ID: ")[1].replace(")", ""))
        modelo_exibicao = modelo_selecionado.split(" (ID:")[0]

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- CONFIRMAÇÃO DE EXCLUSÃO ---\n{CORES['RESET']}")
        print(f"Você selecionou o modelo: {CORES['AMARELO']}{modelo_exibicao}{CORES['RESET']}\n")

        confirmar = questionary.select(
            f"Tem certeza de que deseja excluir permanentemente o modelo?",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=["Sim", "Não"]
        ).ask()

        if confirmar == "Sim":
            limpar_tela()
            
            resultado = modeloServ.removerModelo(id_modelo_alvo)
            
            limpar_tela()
            
            if "sucesso" in resultado:
                print(f"\n{CORES['VERDE']}Modelo '{modelo_exibicao}'{resultado}{CORES['RESET']}")
            elif "vinculado" in resultado:
                print(f"\n{CORES['AMARELO']}Aviso: Modelo '{modelo_exibicao}'{resultado}{CORES['RESET']}")
            else:
                print(f"\n{CORES['VERMELHO']}Erro: Modelo '{modelo_exibicao}'{resultado}{CORES['RESET']}")
        else:
            limpar_tela()
            print(f"{CORES['AMARELO']}Operação de exclusão cancelada pelo usuário.{CORES['RESET']}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")