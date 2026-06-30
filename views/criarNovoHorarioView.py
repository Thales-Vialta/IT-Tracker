import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.horarioService import horarioService

class criarHorarioView:

    def criar_horario(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- CADASTRAR NOVO HORÁRIO ---\n{CORES['RESET']}")

        hora_existe = horarioService.HorarioFuncExiste()

        if hora_existe:
            opcoes_tipo = ["Intervalo", "Cancelar"]
            print(f"{CORES['AMARELO']}Nota: O 'Horario de Funcionamento' já existe. Você só pode adicionar Intervalos.\n{CORES['RESET']}")
        else:
            opcoes_tipo = ["Horário de Funcionamento", "Intervalo", "Cancelar"]
        
        desc_horario = questionary.select(
            "Selecione o tipo de horário que deseja criar:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_tipo
        ).ask()

        if desc_horario == "Cancelar" or not desc_horario:
            return
        
        hora_inicio = questionary.text(
            "Digite a hora de início (ex: 08:00):",
            style=minhas_cores,
            qmark=" ",
        ).ask()

        if not hora_inicio or hora_inicio.strip() == "":
            print(f"{CORES['VERMELHO']}Hora de início inválida!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return
        
        hora_fim = questionary.text(
            "Digite a hora de término (ex: 12:00):",
            style=minhas_cores,
            qmark=" ",
        ).ask()

        if not hora_fim or hora_fim.strip() == "":
            print(f"{CORES['VERMELHO']}Hora de término inválida!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return
        
        limpar_tela()

        resultado = horarioService.criarIntervalo(desc_horario, hora_inicio, hora_fim)
         
        limpar_tela()
        print(f"\n{resultado}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")