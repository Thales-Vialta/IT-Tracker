import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores
from services.AparelhoService import aparelhoService

from services.modeloService import modeloServ

class EditarDispositivosView:

    def editar_dispositivo(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- EDITAR DISPOSITIVO ---\n{CORES['RESET']}")

        modelos_banco = modeloServ.modeloReposit.buscar_Modelo("%")

        if not modelos_banco:
            print(f"{CORES['VERMELHO']}Nenhum modelo cadastrado no sistema para filtrar!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_modelos = []
        for id_mod, marca, nome_modelo in modelos_banco:
            opcoes_modelos.append(f"{nome_modelo} ({marca}) [ID: {id_mod}]")
        
        opcoes_modelos.append("Cancelar")

        modelo_selecionado = questionary.select(
            "Selecione o modelo do dispositivo que deseja encontrar:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_modelos
        ).ask()

        if modelo_selecionado == "Cancelar" or not modelo_selecionado:
            return

        id_modelo_filtro = int(modelo_selecionado.split("[ID: ")[1].replace("]", ""))

        todos_aparelhos = aparelhoService.aparelho_repo.Listar_Todos_Aparelhos()
        
        nome_modelo_puro = modelo_selecionado.split(" (")[0] 

        aparelhos_filtrados = [
            ap for ap in todos_aparelhos if ap[3].strip().lower() == nome_modelo_puro.strip().lower()
        ]

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- DISPOSITIVOS DO MODELO: {nome_modelo_puro} ---\n{CORES['RESET']}")

        if not aparelhos_filtrados:
            print(f"{CORES['VERMELHO']}Nenhum aparelho deste modelo cadastrado no sistema!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_aparelhos = []
        for id_aparelho, patrimonio, marca, modelo in aparelhos_filtrados:
            opcoes_aparelhos.append(f"Patrimônio: {patrimonio} [ID Disp: {id_aparelho}]")
        
        opcoes_aparelhos.append("Cancelar")

        aparelho_selecionado = questionary.select(
            "Selecione o dispositivo específico que deseja editar:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_aparelhos
        ).ask()

        if aparelho_selecionado == "Cancelar" or not aparelho_selecionado:
            return

        id_aparelho_alvo = int(aparelho_selecionado.split("[ID Disp: ")[1].replace("]", ""))

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- O QUE DESEJA ALTERAR? ---\n{CORES['RESET']}")
        print(f"Dispositivo: {CORES['AMARELO']}{aparelho_selecionado}{CORES['RESET']}\n")

        opcao_campo = questionary.select(
            "Selecione o campo:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=["Patrimônio (Serial)", "Mudar o Modelo do Dispositivo", "Cancelar"]
        ).ask()

        if opcao_campo == "Cancelar" or not opcao_campo:
            return

        limpar_tela()

        if opcao_campo == "Patrimônio (Serial)":
            atributo = "Patrimonio"
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- ALTERAR PATRIMÔNIO ---\n{CORES['RESET']}")
            
            novo_valor = questionary.text(
                "Digite o novo número de Patrimônio/Serial:",
                style=minhas_cores,
                qmark=" ",
            ).ask()

            if not novo_valor or not novo_valor.strip():
                print(f"{CORES['VERMELHO']}Patrimônio inválido! Operação cancelada.{CORES['RESET']}")
                input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
                return
            
            novo_valor = novo_valor.strip()
            
            if aparelhoService.serial_ja_cadastrado(novo_valor):
                print(f"\n{CORES['VERMELHO']}Erro: Já existe um aparelho cadastrado com o patrimônio '{novo_valor}'!{CORES['RESET']}")
                input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
                return

        elif opcao_campo == "Mudar o Modelo do Dispositivo":
            atributo = "idModelo"
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- SELECIONE O NOVO MODELO ---\n{CORES['RESET']}")
            
            opcoes_novos_modelos = [opt for opt in opcoes_modelos if opt != "Cancelar"]
            
            novo_modelo_escolhido = questionary.select(
                "Escolha o novo modelo para este dispositivo:",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=opcoes_novos_modelos
            ).ask()

            if not novo_modelo_escolhido:
                return

            novo_valor = int(novo_modelo_escolhido.split("[ID: ")[1].replace("]", ""))

        limpar_tela()
        try:
            aparelhoService.atualizar_aparelho(atributo, novo_valor, id_aparelho_alvo)
            print(f"\n{CORES['VERDE']}Dispositivo atualizado com sucesso!{CORES['RESET']}")
        except Exception as e:
            print(f"\n{CORES['VERMELHO']}Erro ao salvar alterações: {e}{CORES['RESET']}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")