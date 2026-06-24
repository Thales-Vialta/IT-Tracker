import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

from views.gerenciarUsuariosView import gerenciarUsuariosView  
from views.gerenciarSalaView import gerenciarSalaView 
from views.gerenciarHoraView import gerenciarHoraView
from views.backupView import backupView  
from views.formatarDadosView import formatarDadosView

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
                    "Gerenciar Horário de Funcionamento",
                    "Backup de Dados",
                    "Formatar Dados",
                    "Voltar"                
                ]
            ).ask()

            if opcao == "Gerenciar Usuários":
                gerenciarUsuariosView().gerenciar_usuarios()
            elif opcao == "Gerenciar Salas":                 
                gerenciarSalaView().gerenciar_sala()
            elif opcao == "Gerenciar Horário de Funcionamento": 
                gerenciarHoraView().gerenciar_horario()
            elif opcao == "Backup de Dados":
                backupView().backup()
            elif opcao == "Formatar Dados":
                formatarDadosView().formatar_dados()
            elif opcao == "Voltar":
                break