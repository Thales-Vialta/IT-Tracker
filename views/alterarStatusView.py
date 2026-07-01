import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.AparelhoService import aparelhoService
from services.StatusService import statusServ

class AlterarStatusView:

    def alterar_status_dispositivo(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- ALTERAR STATUS DO DISPOSITIVO ---\n{CORES['RESET']}")

        aparelhos_banco = aparelhoService.aparelho_repo.Listar_Todos_Aparelhos()

        if not aparelhos_banco:
            print(f"{CORES['VERMELHO']}Nenhum aparelho cadastrado no sistema!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_aparelhos = []
        for id_aparelho, patrimonio, marca, modelo in aparelhos_banco:
            linha_opcao = f"Patrimônio: {patrimonio} - {modelo} ({marca}) [ID: {id_aparelho}]"
            opcoes_aparelhos.append(linha_opcao)

        opcoes_aparelhos.append("Cancelar")

        aparelho_selecionado = questionary.select(
            "Selecione qual dispositivo deseja alterar o status:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_aparelhos
        ).ask()

        if aparelho_selecionado == "Cancelar" or not aparelho_selecionado:
            return

        id_aparelho_alvo = int(aparelho_selecionado.split("[ID: ")[1].replace("]", ""))

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- SELECIONE O NOVO STATUS ---\n{CORES['RESET']}")
        print(f"Dispositivo: {CORES['AMARELO']}{aparelho_selecionado}{CORES['RESET']}\n")

        status_banco = statusServ.listar_status()

        if not status_banco:
            print(f"{CORES['VERMELHO']}Nenhum status encontrado no banco de dados!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_status = []
        for id_status, descricao in status_banco:
            opcoes_status.append(f"{descricao} [ID: {id_status}]")
        
        opcoes_status.append("Cancelar")

        status_selecionado = questionary.select(
            "Escolha o novo estado do dispositivo:",
            instruction=" ",
            qmark=" ",
            style=minhas_cores,
            choices=opcoes_status
        ).ask()

        if status_selecionado == "Cancelar" or not status_selecionado:
            return

        id_status_alvo = int(status_selecionado.split("[ID: ")[1].replace("]", ""))

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- CONFIRMAR ALTERAÇÃO ---{CORES['RESET']}\n")
        print(f"Aparelho:    {CORES['AMARELO']}{aparelho_selecionado.split(' [ID:')[0]}{CORES['RESET']}")
        print(f"Novo Status: {CORES['VERDE']}{status_selecionado.split(' [ID:')[0]}{CORES['RESET']}\n")

        confirmar = questionary.select(
            "Confirma a alteração de status?",
            choices=["Sim", "Não"],
            style=minhas_cores,
            instruction=" ",
            qmark=" "
        ).ask()

        if confirmar == "Sim":
            limpar_tela()
            try:
                resultado = statusServ.MudarStatus(idStatus=id_status_alvo, idAparelho=id_aparelho_alvo)
                print(f"\n{CORES['VERDE']}✔ {resultado}{CORES['RESET']}")
            except Exception as e:
                print(f"\n{CORES['VERMELHO']}❌ Erro ao alterar status: {e}{CORES['RESET']}")
        else:
            print(f"\n{CORES['AMARELO']}Operação cancelada.{CORES['RESET']}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")