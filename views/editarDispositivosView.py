import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.AparelhoService import aparelhoService
from services.modeloService import modeloServ

class editarDispositivosView:

    def editar_dispositivo(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- EDITAR DISPOSITIVO ---\n{CORES['RESET']}")

        modelos_banco = modeloServ.modeloReposit.buscar_Modelo("%")
        if not modelos_banco:
            print(f"{CORES['VERMELHO']}Nenhum modelo cadastrado no sistema!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        modelos_ordenados = sorted(modelos_banco, key=lambda x: x[2])
        opcoes_modelos = [f"{mod[2]} (ID: {mod[0]})" for mod in modelos_ordenados]
        opcoes_modelos.append("Cancelar")

        modelo_filtro = questionary.select(
            "Primeiro, selecione de qual modelo é o dispositivo que você deseja editar:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_modelos
        ).ask()

        if modelo_filtro == "Cancelar" or not modelo_filtro:
            return

        id_modelo_filtro = int(modelo_filtro.split(" (ID: ")[1].replace(")", ""))
        nome_modelo_filtro = modelo_filtro.split(" (ID:")[0]

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- DISPOSITIVOS DO MODELO: {nome_modelo_filtro} ---\n{CORES['RESET']}")

        todos_aparelhos = aparelhoService.aparelho_repo.Listar_Todos_Aparelhos()
        
        aparelhos_filtrados = [ap for ap in todos_aparelhos if ap[3] == nome_modelo_filtro]

        if not aparelhos_filtrados:
            print(f"{CORES['VERMELHO']}Nenhum dispositivo encontrado para o modelo '{nome_modelo_filtro}'!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_aparelhos = []
        for id_ap, patrimonio, marca, modelo in aparelhos_filtrados:
            linha_opcao = f"Patrimônio: {patrimonio} (ID: {id_ap})"
            opcoes_aparelhos.append(linha_opcao)

        opcoes_aparelhos.append("Cancelar")

        aparelho_selecionado = questionary.select(
            "Selecione qual dispositivo você deseja editar:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_aparelhos
        ).ask()

        if aparelho_selecionado == "Cancelar" or not aparelho_selecionado:
            return

        id_aparelho_alvo = int(aparelho_selecionado.split(" (ID: ")[1].replace(")", ""))
        
        serial_atual = aparelho_selecionado.split("Patrimônio: ")[1].split(" (ID:")[0]

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- O QUE VOCÊ DESEJA EDITAR? ---\n{CORES['RESET']}")

        campo_editar = questionary.select(
            "Selecione o atributo que deseja alterar:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=["Número de Patrimônio (Serial)", "Modelo do Dispositivo", "Cancelar"]
        ).ask()

        if campo_editar == "Cancelar" or not campo_editar:
            return

        serial_final = serial_atual
        id_modelo_final = id_modelo_filtro

        limpar_tela()

        if campo_editar == "Número de Patrimônio (Serial)":
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- ALTERAR PATRIMÔNIO ---\n{CORES['RESET']}")
            novo_serial = questionary.text(
                f"Digite o novo número de patrimônio (Atual: {serial_atual}):",
                style=minhas_cores,
                qmark=" ",
            ).ask()

            if not novo_serial or novo_serial.strip() == "":
                print(f"{CORES['VERMELHO']}Operação cancelada. Patrimônio inválido!{CORES['RESET']}")
                input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
                return
            
            serial_final = novo_serial.strip()

        elif campo_editar == "Modelo do Dispositivo":
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- ALTERAR MODELO DO DISPOSITIVO ---\n{CORES['RESET']}")
            
            opcoes_novos_modelos = [f"{mod[2]} (ID: {mod[0]})" for mod in modelos_ordenados]
            opcoes_novos_modelos.append("Cancelar")

            novo_modelo_sel = questionary.select(
                f"Selecione o novo modelo para este aparelho (Atual: {nome_modelo_filtro}):",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=opcoes_novos_modelos
            ).ask()

            if novo_modelo_sel == "Cancelar" or not novo_modelo_sel:
                return

            id_modelo_final = int(novo_modelo_sel.split(" (ID: ")[1].replace(")", ""))

        limpar_tela()
        
        
        resultado = aparelhoService.atualizar_aparelho(id_aparelho_alvo, serial_final, id_modelo_final)

        if "Erro" in resultado:
            print(f"\n{CORES['VERMELHO']}{resultado}{CORES['RESET']}")
        else:
            print(f"\n{CORES['VERDE']}{resultado}{CORES['RESET']}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")