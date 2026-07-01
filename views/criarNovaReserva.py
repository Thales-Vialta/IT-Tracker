import questionary
import datetime
import calendar
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

# Serviços necessários
from services.alocacaoService import alocacaoService
from services.salaService import salaService
from services.AparelhoService import aparelhoService
from services.horarioService import horarioService # Importando o seu service de horários

class criarNovaReservaView:

    def criar_reserva(self):
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- CRIAR NOVA RESERVA ---\n{CORES['RESET']}")

        usuario_final = questionary.text(
            "Digite o nome do usuário que está reservando:",
            style=minhas_cores,
            qmark=" "
        ).ask()
        
        if not usuario_final or not usuario_final.strip():
            print(f"\n{CORES['VERMELHO']}Operação cancelada: Usuário não pode ser vazio.{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return
        
        usuario_final = usuario_final.strip()

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- SELECIONE A SALA ---\n{CORES['RESET']}")
        
        salas_banco = salaService.sala_repo.listarSalas()

        if not salas_banco:
            print(f"{CORES['VERMELHO']}Erro: Nenhuma sala cadastrada no sistema!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_salas = []
        for sala in salas_banco:
            opcoes_salas.append(sala[0])
        
        opcoes_salas.append("Cancelar")
        
        sala_final = questionary.select(
            "Selecione a Sala para a alocação:",
            style=minhas_cores,
            choices=opcoes_salas,
            instruction=" ",
            qmark=" "
        ).ask()
        
        if sala_final == "Cancelar" or not sala_final:
            return

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- SELECIONE OS APARELHOS ---\n{CORES['RESET']}")
        
        aparelhos_disponiveis = aparelhoService.aparelho_repo.Listar_Aparelhos_Disponiveis()

        if not aparelhos_disponiveis:
            print(f"{CORES['VERMELHO']}Não há nenhum aparelho disponível para alocação no momento!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        opcoes_aparelhos = []
        for aparelho in aparelhos_disponiveis:
            id_ap = aparelho[0]
            patrimonio = aparelho[1]
            detalhes = " | ".join([str(item) for item in aparelho[2:]]) if len(aparelho) > 2 else ""
            opcoes_aparelhos.append(
                questionary.Choice(title=f"Pat: {patrimonio} {f'({detalhes})' if detalhes else ''}", value=id_ap)
            )

        aparelhos_escolhidos = questionary.checkbox(
            "Selecione os aparelhos (Use ESPAÇO para marcar/desmarcar e ENTER para confirmar):",
            style=minhas_cores,
            choices=opcoes_aparelhos,
            instruction=" ",
            qmark=" "
        ).ask()

        if not aparelhos_escolhidos:
            print(f"{CORES['VERMELHO']}Nenhum aparelho selecionado. Operação cancelada.{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- PERÍODO DA RESERVA ---\n{CORES['RESET']}")
        
        agora = datetime.datetime.now()
        ano_atual = agora.year
        mes_atual = agora.month

        _, qtd_dias_mes = calendar.monthrange(ano_atual, mes_atual)

        opcoes_dias = []
        for dia in range(1, qtd_dias_mes + 1):
            opcoes_dias.append(f"{str(dia).zfill(2)}/{str(mes_atual).zfill(2)}/{ano_atual}")

        dia_selecionado = questionary.select(
            "Selecione o DIA para a reserva e devolução:",
            choices=opcoes_dias,
            style=minhas_cores,
            instruction=" ",
            qmark=" "
        ).ask()

        if not dia_selecionado: return

        partes_data = dia_selecionado.split("/")
        data_base_banco = f"{partes_data[2]}-{partes_data[1]}-{partes_data[0]}"

        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- DEFINIR HORÁRIOS PARA O DIA {dia_selecionado} ---\n{CORES['RESET']}")
        
        hora_inicio_str = questionary.text(
            "Digite o horário de INÍCIO (HH:MM):",
            style=minhas_cores,
            qmark=" "
        ).ask()

        if not hora_inicio_str: return

        hora_fim_str = questionary.text(
            "Digite o horário de DEVOLUÇÃO/FIM (HH:MM):",
            style=minhas_cores,
            qmark=" "
        ).ask()

        if not hora_fim_str: return

        if not horarioService.intervaloValido(hora_inicio_str, hora_fim_str):
            print(f"\n{CORES['VERMELHO']}Erro: O horário solicitado está fora do limite de funcionamento da empresa!{CORES['RESET']}")
            input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
            return

        formato = "%H:%M"
        reserva_inicio = datetime.datetime.strptime(hora_inicio_str, formato).time()
        reserva_fim = datetime.datetime.strptime(hora_fim_str, formato).time()

        todos_horarios = horarioService.horario_repo.Mostrar_Horario()
        for h_inicio, h_fim, descricao in todos_horarios:
            if descricao != 'Horario de Funcionamento':
                # Convertendo os intervalos vindos do banco para objetos time
                # Convertendo via string para remover segundos/microssegundos residuais do timedelta do banco
                inter_inicio_str = str(h_inicio).zfill(8)[:5]
                inter_fim_str = str(h_fim).zfill(8)[:5]
                
                intervalo_inicio = datetime.datetime.strptime(inter_inicio_str, formato).time()
                intervalo_fim = datetime.datetime.strptime(inter_fim_str, formato).time()

                # Verifica se há qualquer sobreposição/interseção entre a reserva e o intervalo
                if not (reserva_fim <= intervalo_inicio or reserva_inicio >= intervalo_fim):
                    print(f"\n{CORES['VERMELHO']}Erro: O horário coincide com o intervalo cadastrado: '{descricao}' ({inter_inicio_str} - {inter_fim_str})!{CORES['RESET']}")
                    input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
                    return
        # ---------------------------------------------------------------------

        # Adiciona os segundos para manter o padrão AAAA-MM-DD HH:MM:SS exigido pela alocação
        data_inicio = f"{data_base_banco} {hora_inicio_str.strip()}:00"
        data_fim = f"{data_base_banco} {hora_fim_str.strip()}:00"

        # 5. CONFIRMAÇÃO E ENVIO AO SERVICE
        limpar_tela()
        print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- CONFIRMAR DADOS ---{CORES['RESET']}\n")
        print(f"Usuário:       {CORES['VERDE']}{usuario_final}{CORES['RESET']}")
        print(f"Sala:          {CORES['VERDE']}{sala_final}{CORES['RESET']}")
        print(f"Qtd Aparelhos: {CORES['VERDE']}{len(aparelhos_escolhidos)}{CORES['RESET']}")
        print(f"Período:       {data_inicio} até {data_fim}\n")

        confirmar = questionary.select(
            "Deseja gerar esta alocação?", 
            instruction=" ", 
            style=minhas_cores, 
            qmark=" ",
            choices=["Sim", "Não"]
        ).ask()

        if confirmar == "Sim":
            limpar_tela()
            try:
                resultado = alocacaoService.cadastrarAlocacao(
                    data_hora_inicio=data_inicio,
                    data_hora_fim=data_fim,
                    listIDs_aparelho=aparelhos_escolhidos,
                    user=usuario_final,
                    sala=sala_final
                )
                print(f"\n{CORES['VERDE']}{resultado}{CORES['RESET']}")
            except Exception as e:
                print(f"\n{CORES['VERMELHO']}Erro ao cadastrar: {e}{CORES['RESET']}")
        else:
            print(f"\n{CORES['VERMELHO']}Operação cancelada.{CORES['RESET']}")

        input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")