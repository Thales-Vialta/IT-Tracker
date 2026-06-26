import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.userService import usuarioService
from repositories.usuariosRepository import userRepo
from services.cargoService import cargoService

class editarUsuarioView:
    
    def editar_usuario(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- EDITAR USUÁRIO ---\n{CORES['RESET']}")

        nome_usuario = questionary.text(
            "\nDigite o nome do usuário que deseja editar:",
            style=minhas_cores,
            qmark=" "
        ).ask()

        if not nome_usuario:
            print(f"{CORES['VERMELHO']}Nome inválido!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return
        
        if usuarioService(userRepo, cargoService).validarUsuario(nome_usuario):
            print(f"\n{CORES['VERMELHO']}Usuário não encontrado!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return
        
        atributo = questionary.select(
            "\nO que voce deseja alterar?",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=["Nome", "Cargo", "Cancelar"]
        ).ask()

        if atributo == "Cancelar":
            return
        
        if atributo == "Cargo":
            cargos = cargoService.capturarCargos()
            opcoes_cargos = [cargo[1] for cargo in cargos]
            opcoes_cargos.append("Cancelar")

            novo_valor = questionary.select(
                "Selecione o novo cargo:",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=opcoes_cargos
            ).ask()

            if novo_valor == "Cancelar":
                return
        
        else:
            novo_valor = questionary.text(
                "Digite o novo nome para o usuário:",
                style=minhas_cores,
                qmark=" "
            ).ask()

            if not novo_valor:
                print(f"{CORES['VERMELHO']}Nome inválido!{CORES['RESET']}")
                input("\nVoltar...")
                return
        
        atributo_banco = "Nome_Usuario" if atributo == "Nome" else atributo
        
        validacao = usuarioService(userRepo, cargoService).atualizaUsuario(nome_usuario, atributo_banco, novo_valor)
        limpar_tela()
        if "atualizado" in validacao.lower():
            print(f"\n{CORES['VERDE']}{CORES['NEGRITO']}{nome_usuario}{CORES['RESET']}{validacao}{CORES['RESET']}")
        else:
            print(f"\n{CORES['VERMELHO']}{validacao}{CORES['RESET']}")
        
        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")


        
