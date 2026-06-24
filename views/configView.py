import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

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
                from views.gerenciarUsuariosView import gerenciarUsuariosView  
                gerenciarUsuariosView().gerenciar_usuarios()
            elif opcao == "Gerenciar Salas":
                from views.gerenciarSalaView import gerenciarSalaView  
                gerenciarSalaView().gerenciar_sala()
            elif opcao == "Gerenciar Horário de Funcionamento": 
                from views.gerenciarHoraView import gerenciarHoraView  
                gerenciarHoraView().gerenciar_horario()
            elif opcao == "Backup de Dados":
                from views.backupView import backupView  
                backupView().backup()
            elif opcao == "Formatar Dados":
                from views.formatarDadosView import formatarDadosView  
                formatarDadosView().formatar_dados()
            elif opcao == "Voltar":
                break