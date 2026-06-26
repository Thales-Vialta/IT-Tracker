import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

from services.horarioService import horarioService

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
                    "Ver Horários de Funcionamento",
                    "Criar Novo Horário de Funcionamento",
                    "Editar Horário de Funcionamento",
                    "Deletar Horário de Funcionamento",
                    "Voltar"                
                ]
            ).ask()

            if opcao == "Ver Horários de Funcionamento":
                print(horarioService.listarHorarios())
                input(f"{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            elif opcao == "Criar Novo Horário de Funcionamento":
                print(" Gerenciar reservas em desenvolvimento")
                input("enter")
            elif opcao == "Editar Horário de Funcionamento": 
                print("Gerenciar aparelhos em desenvolvimento")
                input("enter")
            elif opcao == "Deletar Horário de Funcionamento":
                print("Manutenção em desenvolvimento")
                input("enter")
            elif opcao == "Voltar":
                break