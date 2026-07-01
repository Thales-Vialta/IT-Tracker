from repositories.statusRepository import statusRepo

class StatusService:

    def __init__(self, statusRepo):
        self.status_repo = statusRepo

    def MudarStatus(self, idStatus: int, idAparelho: int):
            if idStatus not in [1, 2, 3]:
                raise ValueError("Status inválido.")
                
            self.status_repo.editar_status(idAparelho, idStatus)

            # Removida a vírgula sobressalente depois de idAparelho
            modelo, status = self.status_repo.Mostrar_Novo_Status(idAparelho)
            return f"Status do Aparelho '{modelo}' alterado com sucesso Para '{status}'."


    def listar_manutencao(self):
        aparelhos = self.status_repo.Listar_Defeituosos()

        if not aparelhos:
            return "Não há aparelhos em manutenção."

        return aparelhos
    
    def listar_status(self):
        return self.status_repo.Listar_Aparelhos_Status()
    
    def valideIntervaloAlocacao(self, data_inicio: str, data_fim: str):
            # 1. Busca os aparelhos que estão dentro de algum Item_Alocacao nesse período
            aparelhos_conflitantes = self.status_repo.buscar_aparelhos_alocados_no_intervalo(data_inicio, data_fim)
            
            if not aparelhos_conflitantes:
                return "Nenhum aparelho alocado neste intervalo de tempo."
                
            # 2. Transforma a lista de tuplas [(1,), (5,)] em uma lista limpa [1, 5]
            ids_para_atualizar = [reg[0] for reg in aparelhos_conflitantes]
            
            # 3. Atualiza o idStatus de todos para 2 (Ocupado) na tabela Aparelho
            self.status_repo.atualizar_status_em_lote(ids_para_atualizar, 2)
            
            return f"Validação concluída! {len(ids_para_atualizar)} aparelho(s) detectado(s) em uso e alterado(s) para o status ocupado."
             
statusServ = StatusService(statusRepo)