import questionary
from views.cores import CORES, minhas_cores
from views.limparTela import limpar_tela

from services.alocacaoService import alocacaoService
from services.salaService import salaService


class editarReservaView: 

    def editar_Reserva(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- EDITAR RESERVA ---\n{CORES['RESET']}")

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
            "Selecione qual reserva você deseja editar:",
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

        opcao = questionary.select(
            "O que quer alterar desta reserva?", 
            choices=[
                "Nome do Usuário",
                "Nome da Sala",
                "Data/Hora de Início",
                "Data/Hora de Fim",
                "Sair / Cancelar"
            ],
            style=minhas_cores,
            instruction=" ",
            qmark=" "
        ).ask()

        if opcao == "Sair / Cancelar" or not opcao:
            print(f"\n{CORES['AMARELO']}Operação cancelada.{CORES['RESET']}\n")
            return

        mapa_atributos = {
            "Nome do Usuário": "usuario",
            "Nome da Sala": "sala",
            "Data/Hora de Início": "inicio",
            "Data/Hora de Fim": "fim"
        }
        
        atributo_service = mapa_atributos[opcao]
        novo_valor = None

        if atributo_service == "sala":
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- SELECIONE A NOVA SALA ---\n{CORES['RESET']}")
            salas_banco = salaService.sala_repo.listarSalas()
            
            if salas_banco:
                opcoes_salas = [sala[0] for sala in salas_banco]
                opcoes_salas.append("Cancelar")
                
                escolha_sala = questionary.select(
                    "Selecione a nova sala:",
                    choices=opcoes_salas,
                    style=minhas_cores,
                    instruction=" ",
                    qmark=" "
                ).ask()
                
                if escolha_sala != "Cancelar" and escolha_sala:
                    novo_valor = escolha_sala
            else:
                print(f"{CORES['VERMELHO']}Nenhuma sala cadastrada no sistema para seleção.{CORES['RESET']}")

        elif atributo_service == "usuario":
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- ALTERAR USUÁRIO RESPONSÁVEL ---\n{CORES['RESET']}")
            novo_valor = questionary.text(
                "Digite o nome do novo usuário:",
                style=minhas_cores,
                qmark=" "
            ).ask()

        elif "inicio" in atributo_service or "fim" in atributo_service:
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- ALTERAR DATA E HORÁRIO ---\n{CORES['RESET']}")
            novo_valor = questionary.text(
                f"Digite o novo período para {opcao}\n(Formato: YYYY-MM-DD HH:MM:SS):",
                style=minhas_cores,
                qmark=" "
            ).ask()

        if not novo_valor or not str(novo_valor).strip():
            print(f"\n{CORES['AMARELO']}Alteração vazia ou cancelada. Operação abortada.{CORES['RESET']}\n")
            questionary.press_any_key_to_continue("Pressione qualquer tecla para voltar...", style=minhas_cores).ask()
            return

        novo_valor = str(novo_valor).strip()

        limpar_tela()
        confirmar = questionary.select(
            f"Tem certeza que deseja alterar '{opcao}' para '{novo_valor}'?",
            choices=["Sim", "Não"],
            style=minhas_cores,
            instruction=" ",
            qmark=" "
        ).ask()

        if confirmar == "Sim":
            try:
                resultado = alocacaoService.editarAlocacao(id_alocacao, atributo_service, novo_valor)
                print(f"\n{CORES['VERDE']}✔ {resultado}{CORES['RESET']}\n")
            except Exception as e:
                print(f"\n{CORES['VERMELHO']}Erro ao atualizar reserva: {e}{CORES['RESET']}\n")
        else:
            print(f"\n{CORES['AMARELO']}Alteração descartada.{CORES['RESET']}\n")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")