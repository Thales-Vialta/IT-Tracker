import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.userService import usuarioService  
from repositories.usuariosRepository import userRepo
from services.cargoService import cargoService

class CriarNovoUsuarioView:

    def criar_usuario(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- CADASTRAR NOVO USUÁRIO ---\n{CORES['RESET']}")

        nome_usuario = questionary.text(
            "Digite o nome do novo usuário:",
            style=minhas_cores,
            qmark=" ",
        ).ask()

        if not nome_usuario or nome_usuario == "":
            print(f"{CORES['VERMELHO']}Nome não pode ser vazio!{CORES['RESET']}")
            input("\nVoltar...")
            return

        cargos_banco = cargoService.capturarCargos()
        
        if not cargos_banco:
            print(f"{CORES['VERMELHO']}Nenhum cargo cadastrado no sistema!{CORES['RESET']}")
            input("\nVoltar...")
            return

        opcoes_cargos = [cargo[1] for cargo in cargos_banco]
        opcoes_cargos.append("Cancelar")

        cargo_selecionado = questionary.select(
            "\nSelecione o cargo do usuário:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_cargos
        ).ask()

        if cargo_selecionado == "Cancelar":
            return

        validacao = usuarioService(userRepo, cargoService).cadastrarUsuario(nome_usuario, cargo_selecionado)
         
        if "sucesso" in validacao.lower():
            limpar_tela()
            print(f"\n{CORES['VERDE']}{CORES['NEGRITO']}{nome_usuario}{CORES['RESET']}{validacao}{CORES['RESET']}")
        else:
            limpar_tela()
            print(f"\n{CORES['VERMELHO']}{validacao}{CORES['RESET']}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")