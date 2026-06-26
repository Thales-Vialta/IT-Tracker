import questionary
from views.limparTela import limpar_tela
from views.cores import CORES
from views.cores import minhas_cores

from services.userService import usuarioService
from repositories.usuariosRepository import userRepo
from services.cargoService import cargoService
from views.criarNovoUsuarioView import CriarNovoUsuarioView
from views.editarUsuarioView import editarUsuarioView
from views.removerUsuarioView import removerUsuarioView

class gerenciarUsuariosView:

    def gerenciar_usuarios(self):
        while True:
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- GERENCIAR USUÁRIOS ---\n{CORES['RESET']}")

            opcao = questionary.select(
                "Selecione uma opção:",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=[
                    "Ver Usuários Cadastrados",
                    "Criar Novo Usuário",
                    "Editar Usuários",
                    "Deletar Usuários",
                    "Voltar"                
                ]
            ).ask()

            if opcao == "Ver Usuários Cadastrados":
                print(usuarioService(userRepo, cargoService).listarUsuarios())
                input(f"{CORES['AMARELO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            elif opcao == "Criar Novo Usuário":
               CriarNovoUsuarioView().criar_usuario()
            elif opcao == "Editar Usuários": 
                editarUsuarioView().editar_usuario()
            elif opcao == "Deletar Usuários":
                removerUsuarioView().remover_usuario()
            elif opcao == "Voltar":
                break