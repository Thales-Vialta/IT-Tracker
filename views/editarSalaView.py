import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.salaService import salaService

class editarSalaView:
    
    def editar_sala(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- EDITAR SALA ---\n{CORES['RESET']}")

        nome_sala = questionary.text(
            "Digite o nome da sala que deseja editar:",
            style=minhas_cores,
            qmark=" "
        ).ask()

        if not nome_sala or nome_sala == "":
            print(f"{CORES['VERMELHO']}Nome inválido!{CORES['RESET']}")
            input(f"{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return
        
        if salaService.existeSala(nome_sala):
            print(f"\n{CORES['VERMELHO']}Sala não encontrada no sistema!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        atributo = questionary.select(
            "\nO que você deseja alterar?",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=["Nome", "Endereço", "Cancelar"]
        ).ask()

        if atributo == "Cancelar":
            return
        
        if atributo == "Nome":
            atributo_banco = "NomeSala"
            novo_valor = questionary.text(
                "Digite o novo nome para a sala:",
                style=minhas_cores,
                qmark=" "
            ).ask()
        else:
            atributo_banco = "EnderecoSala"
            novo_valor = questionary.text(
                "Digite o novo endereço para a sala:",
                style=minhas_cores,
                qmark=" "
            ).ask()

        if not novo_valor or novo_valor == "":
            print(f"{CORES['VERMELHO']}Valor inválido!{CORES['RESET']}")
            input(f"{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return
        
        if atributo_banco == "NomeSala" and not salaService.existeSala(novo_valor):
            print(f"\n{CORES['VERMELHO']}Já existe uma sala cadastrada com o nome '{novo_valor}'!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return


        resultado = salaService.editarSalas(nome_sala, atributo_banco, novo_valor)
        
        limpar_tela()
        print(f"\n{CORES['VERDE']}Sala atualizada com sucesso!{CORES['RESET']}")
        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")