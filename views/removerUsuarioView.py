import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.userService import usuarioService
from repositories.usuariosRepository import userRepo
from services.cargoService import cargoService

class removerUsuarioView:
    
    def remover_usuario(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- REMOVER USUÁRIO ---\n{CORES['RESET']}")

        nome_usuario = questionary.text(
            "Digite o nome do usuário que deseja remover:",
            style=minhas_cores,
            qmark=" "
        ).ask()

        if not nome_usuario or nome_usuario.strip() == "":
            print(f"{CORES['VERMELHO']}Nome inválido!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        if usuarioService(userRepo, cargoService).validarUsuario(nome_usuario):
            limpar_tela()
            print(f"\n{CORES['VERMELHO']}Usuário não encontrado!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return
        # ------------------------

        validacao = usuarioService(userRepo, cargoService).removerUsuario(nome_usuario)
        
        limpar_tela()
        print(f"\n{CORES['NEGRITO']}{nome_usuario}{CORES['RESET']}{CORES['VERDE']}{validacao}{CORES['RESET']}")
        
        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")