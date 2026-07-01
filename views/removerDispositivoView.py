import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.AparelhoService import aparelhoService
from services.modeloService import modeloServ

class removerDispositivosView:

    def remover_dispositivo(self):
        limpar_tela()
        print(f"{CORES['VERMELHO']}{CORES['NEGRITO']}--- REMOVER DISPOSITIVO DO SISTEMA ---\n{CORES['RESET']}")

        modelos_banco = modeloServ.modeloReposit.buscar_Modelo("%")
        if not modelos_banco:
            print(f"{CORES['VERMELHO']}Nenhum modelo cadastrado no sistema!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        modelos_ordenados = sorted(modelos_banco, key=lambda x: x[2])
        opcoes_modelos = [f"{mod[2]} (ID: {mod[0]})" for mod in modelos_ordenados]
        opcoes_modelos.append("Cancelar")

        modelo_filtro = questionary.select(
            "Selecione o modelo do dispositivo que deseja remover:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_modelos
        ).ask()

        if modelo_filtro == "Cancelar" or not modelo_filtro:
            return

        nome_modelo_filtro = modelo_filtro.split(" (ID:")[0]

        limpar_tela()
        print(f"{CORES['VERMELHO']}{CORES['NEGRITO']}--- EXCLUIR APARELHO: {nome_modelo_filtro} ---\n{CORES['RESET']}")

        # 2. Busca todos e filtra pelo nome do modelo escolhido
        todos_aparelhos = aparelhoService.aparelho_repo.Listar_Todos_Aparelhos()
        aparelhos_filtrados = [ap for ap in todos_aparelhos if ap[3] == nome_modelo_filtro]

        if not aparelhos_filtrados:
            print(f"{CORES['VERMELHO']}Nenhum dispositivo encontrado para o modelo '{nome_modelo_filtro}'!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_aparelhos = []
        for ap in aparelhos_filtrados:
            # Forçamos o índice [0] que é o id_Aparelho e [1] que é o patrimonio
            id_real = ap[0]
            patrimonio_real = ap[1]
            
            linha_opcao = f"Patrimônio: {patrimonio_real} | ID Interno: {id_real}"
            opcoes_aparelhos.append(linha_opcao)

        opcoes_aparelhos.append("Cancelar")

        aparelho_selecionado = questionary.select(
            "CRÍTICO: Escolha qual dispositivo será DELETADO permanentemente:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_aparelhos
        ).ask()

        if aparelho_selecionado == "Cancelar" or not aparelho_selecionado:
            return

        # Extração garantida: pegamos tudo o que vem depois de "ID Interno: "
        id_aparelho_alvo = int(aparelho_selecionado.split("| ID Interno: ")[1])

        limpar_tela()

        confirmar = questionary.confirm(
            f"Tem certeza absoluta que deseja remover o dispositivo de ID {id_aparelho_alvo}?",
            default=False,
            style=minhas_cores,
            qmark=" "
        ).ask()

        if not confirmar:
            print(f"\n{CORES['AMARELO']}Operação cancelada pelo usuário.{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        limpar_tela()

        resultado = aparelhoService.remover_aparelho(id_aparelho_alvo)

        if "Erro" in resultado:
            print(f"\n{CORES['VERMELHO']}{resultado}{CORES['RESET']}")
        else:
            print(f"\n{CORES['VERDE']}{resultado}{CORES['RESET']}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")