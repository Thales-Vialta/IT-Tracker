import questionary
from views.limparTela import limpar_tela
from views.cores import CORES, minhas_cores

from services.ManutencaoService import manutencaoServe

class ManutencaoView:

    def manutencao(self):
        while True:
            limpar_tela()
            print(f"{CORES['AZUL']}{CORES['NEGRITO']}---- MANUTENÇÃO ----\n{CORES['RESET']}")

            total_tupla = manutencaoServe.obter_quantidade_em_manutencao()
            total = total_tupla[0] if total_tupla else 0

            print(f"Dispositivos atualmente em manutenção: {CORES['AMARELO']}{CORES['NEGRITO']}{total}{CORES['RESET']}\n")

            opcao = questionary.select(
                "Selecione uma opção:",
                instruction=" ",
                qmark=" ",
                style=minhas_cores,
                choices=[
                    "Listar Aparelhos Defeituosos",
                    "Adicionar Aparelho na Manutenção",
                    "Liberar Aparelho da Manutenção",
                    "Voltar"
                ]
            ).ask()

            if opcao == "Voltar" or not opcao:
                break

            elif opcao == "Listar Aparelhos Defeituosos":
                limpar_tela()
                print(f"{CORES['AZUL']}{CORES['NEGRITO']}---- DISPOSITIVOS COM DEFEITO ----\n{CORES['RESET']}")

                aparelhos = manutencaoServe.obter_aparelhos_defeituosos()

                if not aparelhos:
                    print(f"{CORES['VERDE']}Nenhum aparelho em manutenção no momento.{CORES['RESET']}\n")
                else:
                    for numero, ap in enumerate(aparelhos, start=1):
                        id_ap, patrimonio, modelo = ap
                        num_format = f"{numero}.".ljust(4)
                        patrimonio_format = patrimonio.ljust(20)
                        
                        print(
                            f"{CORES['AMARELO']}{CORES['NEGRITO']}{num_format}{CORES['RESET']} "
                            f"ID: {str(id_ap).ljust(4)} | "
                            f"Aparelho: {modelo.ljust(25)} | "
                            f"Patrimônio: {patrimonio_format}"
                        )

                input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}\nVoltar{CORES['RESET']}")
            
            elif opcao == "Adicionar Aparelho na Manutenção":
                limpar_tela()
                print(f"{CORES['AZUL']}{CORES['NEGRITO']}---- ADICIONAR DISPOSTIVO ----\n{CORES['RESET']}")
                input(f"{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")


            elif opcao == "Liberar Aparelho da Manutenção":
                limpar_tela()
                print(f"{CORES['AZUL']}{CORES['NEGRITO']}--- LIBERAR APARELHO ---\n{CORES['RESET']}")

                aparelhos = manutencaoServe.obter_aparelhos_defeituosos()

                if not aparelhos:
                    print(f"{CORES['AMARELO']}Não há aparelhos em manutenção para serem liberados!{CORES['RESET']}\n")
                    input(f"{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")
                    continue

                opcoes_selecao = []
                mapa_ids = {}

                for id_ap, patrimonio, modelo in aparelhos:
                    texto_opcao = f"ID: {id_ap} | {modelo} ({patrimonio})"
                    opcoes_selecao.append(texto_opcao)
                    mapa_ids[texto_opcao] = id_ap

                opcoes_selecao.append("Cancelar")

                escolha = questionary.select(
                    "Selecione qual aparelho deseja liberar para uso:",
                    instruction=" ",
                    qmark=" ",
                    style=minhas_cores,
                    choices=opcoes_selecao
                ).ask()

                if escolha == "Cancelar" or not escolha:
                    continue

                id_alvo = mapa_ids[escolha]

                confirmar = questionary.select(
                    f"Confirmar que o aparelho ID {id_alvo} foi consertado e está pronto para uso?",
                    instruction=" ",
                    qmark=" ",
                    style=minhas_cores,
                    choices=["Sim", "Não"]
                ).ask()

                if confirmar == "Sim":
                    limpar_tela()
                    
                    try:
                        resultado = manutencaoServe.liberar_aparelho_da_manutencao(id_alvo)
                        print(f"\n{CORES['VERDE']}{resultado}{CORES['RESET']}")
                    except Exception as e:
                        print(f"\n{CORES['VERMELHO']}Erro: {e}{CORES['RESET']}")
                else:
                    print(f"\n{CORES['AMARELO']}Operação cancelada.{CORES['RESET']}")

                input(f"\n{CORES['VERMELHO']}{CORES['NEGRITO']}Voltar{CORES['RESET']}")