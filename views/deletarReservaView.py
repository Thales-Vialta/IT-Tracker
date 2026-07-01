import questionary
from views.cores import CORES
from views.limparTela import limpar_tela

from services.alocacaoService import alocacaoService


class deletarReservaView:

    def deletar_Reserva(self):
        limpar_tela()
        print(
            f"{CORES['VERMELHO']}{CORES['NEGRITO']}--- DELETAR RESERVA ---\n{CORES['RESET']}"
        )
        id_alocacao = (
            questionary.text("Digite o ID da Reserva que deseja deletar: ",validate=lambda text: text.isdigit()
                or "Por favor, insira um número válido.",
            ).ask())

        if not id_alocacao:
            return
        id_alocacao = int(id_alocacao)
        resumo = alocacaoService.buscarAlocacao(id_alocacao, "Atual")
        limpar_tela()
        print(resumo)

        if "Nenhuma alocação encontrada" in resumo:
            questionary.press_any_key_to_continue(
                "Pressione qualquer tecla para voltar..."
            ).ask()
            return

        confirmar = questionary.confirm(
            f"{CORES['VERMELHO']}⚠️  Tem certeza absoluta que deseja DELETAR a reserva #{id_alocacao}?{CORES['RESET']}",
            default=False,  # Por segurança, o padrão vem como "Não" (False)
        ).ask()

        # 4. Executa a ação no Service baseado na resposta
        if confirmar:
            try:

                alocacaoService.removerAlocacao(id_alocacao)
                print(
                    f"\n{CORES['VERDE']}✔ Reserva #{id_alocacao} deletada com sucesso!{CORES['RESET']}\n"
                )
            except Exception as e:
                print(
                    f"\n{CORES['VERMELHO']}❌ Erro ao deletar reserva: {e}{CORES['RESET']}\n"
                )
        else:
            print(
                f"\n{CORES['AMARELO']}Operação cancelada. A reserva não foi alterada.{CORES['RESET']}\n"
            )

        questionary.press_any_key_to_continue(
            "Pressione qualquer tecla para continuar..."
        ).ask()