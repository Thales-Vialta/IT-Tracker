import questionary
from views.limparTela import limpar_tela
from views.cores import CORES

from services.alocacaoService import alocacaoService
from services.salaService import salaService
from services.AparelhoService import aparelhoService

class editarReservaView: 

    def editar_Reserva(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- EDITAR RESERVA ---\n{CORES['RESET']}")
        id_alocacao = questionary.text("Digite o ID da Reserva que queira editar: ", validate=lambda text:text.isdigit()or "Por favor, insira um número válido.").ask()

        if not id_alocacao: 
            return
        id_alocacao = int(id_alocacao)

        resumo = alocacaoService.buscarAlocacao(id_alocacao,"Atual")
        limpar_tela()
        print(resumo)

        if "Nenhuma alocação encontrada" in resumo:
            questionary.press_any_key_to_continue("Pressione qualquer tecla para voltar...").ask()
            return
        
        opcao = questionary.select("O que quer alterar desta reserva?", 
            choices=[
                "Data de Alocação (Início)",
                "Data de Devolução (Fim)",
                "ID da Sala",
                "ID do Usuário",
                "Sair / Cancelar"
            ]).ask()
        if opcao == "Sair / Cancelar" or not opcao:
            print(f"\n{CORES['AMARELO']}Operação cancelada.{CORES['RESET']}\n")
            return

        mapa_atributos = {
            "Data de Alocação (Início)": "DataAlocacao",
            "Data de Devolução (Fim)": "DataDevolucao",
            "ID da Sala": "idSala",
            "ID do Usuário": "idUsuario"
        }
        
        atributo_db = mapa_atributos[opcao]

        if "Data" in atributo_db:
            novo_valor = questionary.text(
                f"Digite a nova {opcao} (Formato: YYYY-MM-DD HH:MM:SS):"
            ).ask()
        else:
            novo_valor = questionary.text(
                f"Digite o novo {opcao}:",
                validate=lambda text: text.isdigit() or "O ID deve ser um número inteiro."
            ).ask()
            if novo_valor:
                novo_valor = int(novo_valor)

        if not novo_valor:
            print(f"\n{CORES['AMARELO']}Alteração vazia. Operação cancelada.{CORES['RESET']}\n")
            return

        confirmar = questionary.confirm(
            f"Tem certeza que deseja alterar '{opcao}' para '{novo_valor}'?",
            default=True
        ).ask()

        if confirmar:
            try:

                alocacaoService.editarAlocacao(id_alocacao, atributo_db, novo_valor)
                print(f"\n{CORES['VERDE']}✔ Reserva #{id_alocacao} atualizada com sucesso!{CORES['RESET']}\n")
            except Exception as e:
                print(f"\n{CORES['VERMELHO']}❌ Erro ao atualizar reserva: {e}{CORES['RESET']}\n")
        else:
            print(f"\n{CORES['AMARELO']}Alteração descartada.{CORES['RESET']}\n")

        questionary.press_any_key_to_continue("Pressione qualquer tecla para continuar...").ask()