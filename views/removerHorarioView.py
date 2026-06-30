import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.horarioService import horarioService

class RemoverHorarioView:

    def remover_horario(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- REMOVER HORÁRIO EXISTENTE ---\n{CORES['RESET']}")

        horarios_banco = horarioService.horario_repo.Mostrar_Horario()

        if not horarios_banco:
            print(f"{CORES['VERMELHO']}Nenhum horário cadastrado no sistema para remover!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_horarios = []
        for inicio, fim, descricao in horarios_banco:
            periodo = f"{str(inicio)} - {str(fim)}"
            linha_opcao = f"{descricao} ({periodo})"
            opcoes_horarios.append(linha_opcao)

        opcoes_horarios.append("Cancelar")

        opcao_selecionada = questionary.select(
            "Selecione qual horário você deseja remover:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_horarios
        ).ask()

        if opcao_selecionada == "Cancelar" or not opcao_selecionada:
            return

        desc_alvo = opcao_selecionada.split(" (")[0]

        limpar_tela()

        if desc_alvo.strip() == 'Horario de Funcionamento':
            print(f"{CORES['VERMELHO']}{CORES['NEGRITO']}⚠️ ATENÇÃO: Você selecionou o Horário de Funcionamento!{CORES['RESET']}\n")
            
            confirmar = questionary.select(
                "Tem certeza que deseja remover o Horário de Funcionamento?",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=["Sim", "Não"]
            ).ask()
        else:
            print(f"Intervalo selecionado: {CORES['AMARELO']}{opcao_selecionada}{CORES['RESET']}\n")
            
            confirmar = questionary.select(
                "Deseja mesmo excluir este intervalo?",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=["Sim", "Não"]
            ).ask()

        if confirmar =="Sim":
            limpar_tela()
            
            resultado = horarioService.removerIntervalo(desc_alvo)
            
            limpar_tela()
            print(f"\n{resultado}")
        else:
            limpar_tela()
            print(f"{CORES['AMARELO']}Operação cancelada pelo usuário.{CORES['RESET']}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")