import questionary
from views.cores import CORES, minhas_cores
from views.limparTela import limpar_tela

from services.alocacaoService import alocacaoService


class deletarReservaView:

    def deletar_Reserva(self):
        limpar_tela()
        print(
            f"{CORES['AZUL']}{CORES['NEGRITO']}--- DELETAR RESERVA ---\n{CORES['RESET']}"
        )

        alocacoes_banco = alocacaoService.repoAloc.listar_alocacoes()

        if not alocacoes_banco:
            print(f"{CORES['VERMELHO']}Nenhuma reserva cadastrada no sistema!{CORES['RESET']}")
            questionary.press_any_key_to_continue(
                "Pressione qualquer tecla para voltar...",
                style=minhas_cores
            ).ask()
            return

        opcoes_reservas = []
        for registro in alocacoes_banco:
            id_aloc, usuario, sala, dt_aloc, _, _, _ = registro
            linha = f"ID: #{id_aloc} | Usuário: {usuario} | Sala: {sala} | Data: {dt_aloc}"
            opcoes_reservas.append(linha)
        
        opcoes_reservas.append("Cancelar")

        reserva_selecionada = questionary.select(
            "Selecione qual reserva você deseja deletar:",
            choices=opcoes_reservas,
            style=minhas_cores,
            instruction=" ",
            qmark=" "
        ).ask()

        if reserva_selecionada == "Cancelar" or not reserva_selecionada:
            return

        id_alocacao = int(reserva_selecionada.split("ID: #")[1].split(" |")[0])

        limpar_tela()
        resumo = alocacaoService.buscarAlocacao(id_alocacao)
        print(resumo)

        confirmar = questionary.select(
            f"Tem certeza absoluta que deseja DELETAR a reserva #{id_alocacao}?",
            choices=["Sim", "Não"],
            style=minhas_cores,
            instruction=" ",
            qmark=" "
        ).ask()

        if confirmar == "Sim":
            try:
                alocacaoService.removerAlocacao(id_alocacao)
                print(
                    f"\n{CORES['VERDE']}✔ Reserva #{id_alocacao} deletada com sucesso!{CORES['RESET']}\n"
                )
            except Exception as e:
                print(
                    f"\n{CORES['VERMELHO']}Erro ao deletar reserva: {e}{CORES['RESET']}\n"
                )
        else:
            print(
                f"\n{CORES['AMARELO']}Operação cancelada. A reserva não foi alterada.{CORES['RESET']}\n"
            )

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")