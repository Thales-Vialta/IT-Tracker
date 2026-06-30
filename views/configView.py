import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

from views.gerenciarUsuariosView import gerenciarUsuariosView  
from views.gerenciarSalaView import gerenciarSalaView 
from views.gerenciarHoraView import gerenciarHoraView

class configView:
    def config(self):
        while True:
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- CONFIGURAÇÕES ---\n{CORES['RESET']}")

            opcao = questionary.select(
                "Selecione uma opção:",
                instruction=" ",
                qmark="",
                style=minhas_cores,
                choices=[
                    "Gerenciar Usuários",
                    "Gerenciar Salas",
                    "Gerenciar Horários",
                    "Voltar"                
                ]
            ).ask()

            if opcao == "Gerenciar Usuários":
                gerenciarUsuariosView().gerenciar_usuarios()
            elif opcao == "Gerenciar Salas":                 
                gerenciarSalaView().gerenciar_sala()
            elif opcao == "Gerenciar Horários": 
                gerenciarHoraView().gerenciar_horario()
            elif opcao == "Voltar":
                break