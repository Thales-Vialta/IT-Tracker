import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

from services.horarioService import horarioService
from views.criarNovoHorarioView import criarHorarioView
from views.editarHorarioView import EditarHorarioView
from views.removerHorarioView import RemoverHorarioView

class gerenciarHoraView:

    def gerenciar_horario(self):
        while True:
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- GERENCIAR HORÁRIOS DE FUNCIONAMENTO ---\n{CORES['RESET']}")

            opcao = questionary.select(
                "Selecione uma opção:",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=[
                    "Ver Horários",
                    "Criar Novo Horário",
                    "Editar Horário",
                    "Deletar Horário",
                    "Voltar"                
                ]
            ).ask()

            if opcao == "Ver Horários":
                print(horarioService.listarHorarios())
                input(f"{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            elif opcao == "Criar Novo Horário":
                criarHorarioView().criar_horario()
            elif opcao == "Editar Horário": 
                EditarHorarioView().editar_horario()
            elif opcao == "Deletar Horário":
                RemoverHorarioView().remover_horario()
            elif opcao == "Voltar":
                break