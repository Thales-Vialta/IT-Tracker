from dbConnector.Database import DatabaseConnector
import time

class StatusRepository:

    def Listar_Aparelhos_Status(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()     
            cursor.execute("""
                        SELECT * FROM StatusAparelho
                    """)
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conn.close()


    def editar_status(self, idAparelho:int, idStatus:int):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute("""UPDATE Aparelho SET idStatus = %s WHERE id_Aparelho = %s """, (idStatus, idAparelho))
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conn.close()

    def Mostrar_Novo_Status(self,idAparelho: int): 
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""SELECT m.Modelo, s.Descricao FROM Aparelho a
            INNER JOIN Modelo_Aparelho m
            ON a.idModelo = m.idModelo
            INNER JOIN StatusAparelho s
            ON a.idStatus = s.idStatus
            WHERE a.id_Aparelho = %s;""", (idAparelho,))
            resultado = cursor.fetchone()
            return resultado 
        except ValueError: 
                print("Erro! Nome vazio")
        except Exception as e:
                print(f"Erro ao inserir usuário: {e}")
                
        finally:
            cursor.close()
            conn.close()


    def checaDisponibilidade(self):
            # Conecta ao banco usando a sua classe exata
            conn = DatabaseConnector().get_connection()
            try:
                cursor = conn.cursor()
                
                # 1. Captura a data e hora atual do computador no formato do MySQL (AAAA-MM-DD HH:MM:SS)
                agora = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                
                # 2. Atualiza para Indisponível (idStatus = 2) apenas se NÃO estiver em manutenção (idStatus <> 3)
                query_indisponiveis = """
                    UPDATE Aparelho 
                    SET idStatus = 2
                    WHERE idStatus <> 3 
                    AND id_Aparelho IN (
                        SELECT id_Aparelho 
                        FROM Alocacao 
                        WHERE %s BETWEEN DataAlocacao AND DataDevolucao
                    );
                """
                cursor.execute(query_indisponiveis, (agora,))
                
                # 3. Atualiza para Disponível (idStatus = 1) apenas se NÃO estiver em manutenção (idStatus <> 3)
                query_disponiveis = """
                    UPDATE Aparelho 
                    SET idStatus = 1
                    WHERE idStatus <> 3 
                    AND id_Aparelho NOT IN (
                        SELECT id_Aparelho 
                        FROM Alocacao 
                        WHERE %s BETWEEN DataAlocacao AND DataDevolucao
                    );
                """
                cursor.execute(query_disponiveis, (agora,))
                
                # Confirma as alterações em lote no banco de dados
                conn.commit()
                return "Funcionou"
                
            except Exception as e:
                # Desfaz qualquer alteração em caso de falha antes de fechar
                conn.rollback()
                print(f"Erro ao atualizar disponibilidade por horário: {e}")
                return "Deu erro"
                
            finally:
                cursor.close()
                conn.close()


  

statusRepo = StatusRepository()