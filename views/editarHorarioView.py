import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.horarioService import horarioService

class EditarHorarioView:

    def editar_horario(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- EDITAR HORÁRIO EXISTENTE ---\n{CORES['RESET']}")

        horarios_banco = horarioService.horario_repo.Mostrar_Horario()

        if not horarios_banco:
            print(f"{CORES['VERMELHO']}Nenhum horário cadastrado no sistema para editar!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_horarios = []
        for inicio, fim, descricao in horarios_banco:
            periodo = f"{str(inicio)} - {str(fim)}"
            linha_opcao = f"{descricao} ({periodo})"
            opcoes_horarios.append(linha_opcao)

        opcoes_horarios.append("Cancelar")

        opcao_selecionada = questionary.select(
            "Selecione qual horário você deseja editar:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_horarios
        ).ask()

        if opcao_selecionada == "Cancelar" or not opcao_selecionada:
            return

        desc_alvo = opcao_selecionada.split(" (")[0]

        id_horario = horarioService.horario_repo.descobrirIdPorDescricao(desc_alvo)

        if not id_horario:
            print(f"{CORES['VERMELHO']}Erro: Não foi possível localizar o ID deste horário no banco.{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- NOVOS DADOS PARA: {desc_alvo} ---\n{CORES['RESET']}")

        novo_inicio = questionary.text(
            "Digite a nova hora de início (ex: 08:30):",
            style=minhas_cores,
            qmark=" ",
        ).ask()

        if not novo_inicio or novo_inicio.strip() == "":
            print(f"{CORES['VERMELHO']}Hora de início inválida!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        novo_fim = questionary.text(
            "Digite a nova hora de término (ex: 17:30):",
            style=minhas_cores,
            qmark=" ",
        ).ask()

        if not novo_fim or novo_fim.strip() == "":
            print(f"{CORES['VERMELHO']}Hora de término inválida!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- ATUALIZANDO ---\n{CORES['RESET']}")
        
        resultado = horarioService.editarIntervalo(id_horario, desc_alvo, novo_inicio, novo_fim)

        limpar_tela()
        print(f"\n{resultado}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")