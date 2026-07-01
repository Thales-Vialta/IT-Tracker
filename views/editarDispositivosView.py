import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores
from services.AparelhoService import aparelhoService

# Importamos o modeloService para buscar os modelos cadastrados no banco
from services.modeloService import modeloServ

class EditarDispositivosView:

    def editar_dispositivo(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- EDITAR DISPOSITIVO ---\n{CORES['RESET']}")

        # 1. PASSO: Selecionar o Modelo para filtrar a busca posterior
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

        # Extrai o ID do modelo escolhido
        id_modelo_filtro = int(modelo_selecionado.split("[ID: ")[1].replace("]", ""))

        # 2. PASSO: Listar os aparelhos e filtrar apenas os que batem com o ID do Modelo selecionado
        todos_aparelhos = aparelhoService.aparelho_repo.Listar_Todos_Aparelhos()
        
        # Filtramos a lista vinda do repositório em tempo de execução
        # Procuramos o nome do modelo na tupla ou alteramos para buscar pelo ID se a query trouxer.
        # Como o seu Listar_Todos_Aparelhos retorna (id_Aparelho, patrimonio, Marca, Modelo),
        # vamos filtrar comparando o nome do modelo/marca ou buscando compatibilidade.
        nome_modelo_puro = modelo_selecionado.split(" (")[0] # Pega "Galaxy S23" por exemplo

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

        # Extrai o ID do aparelho (dispositivo)
        id_aparelho_alvo = int(aparelho_selecionado.split("[ID Disp: ")[1].replace("]", ""))

        # 3. PASSO: Escolher o campo que será editado (Sem a opção de Status)
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

        # 4. PASSO: Processamento das alterações via Service
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
            
            # Validação usando a regra do Service
            if aparelhoService.serial_ja_cadastrado(novo_valor):
                print(f"\n{CORES['VERMELHO']}Erro: Já existe um aparelho cadastrado com o patrimônio '{novo_valor}'!{CORES['RESET']}")
                input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
                return

        elif opcao_campo == "Mudar o Modelo do Dispositivo":
            atributo = "idModelo"
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- SELECIONE O NOVO MODELO ---\n{CORES['RESET']}")
            
            # Exibe novamente a lista de modelos do banco para ele escolher o novo destino
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

        # Execução final no banco de dados usando o Service
        limpar_tela()
        try:
            aparelhoService.atualizar_aparelho(atributo, novo_valor, id_aparelho_alvo)
            print(f"\n{CORES['VERDE']}Dispositivo atualizado com sucesso!{CORES['RESET']}")
        except Exception as e:
            print(f"\n{CORES['VERMELHO']}Erro ao salvar alterações: {e}{CORES['RESET']}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")