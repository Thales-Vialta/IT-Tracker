from dbConnector.Database import DatabaseConnector
class AlocacaoRepository:

    def inserir_Alocacao(self, alocacao):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Alocacao
                (idUsuario, id_Aparelho, idSala, DataAlocacao, DataDevolucao)
                VALUES (%s, %s, %s, %s, %s)
            """,
            (
                alocacao.idUsuario,
                alocacao.id_Aparelho,
                alocacao.idSala,
                alocacao.DataAlocacao,
                alocacao.DataDevolucao
            ))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def Aparelhos_menos_Alocados(self): 
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()

            cursor.execute("""
                SELECT id_Aparelho, COUNT(idAlocacao) as total_alocacoes
                FROM Alocacao 
                GROUP BY id_Aparelho
                ORDER BY total_alocacoes ASC;
            """)
            resultado = cursor.fetchall()
            return resultado
        finally: 
            cursor.close()
            conn.close()

    def Editar_Alocacao(self, alocacao): 
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Alocacao 
                SET idUsuario = %s, id_Aparelho = %s, idSala = %s, DataAlocacao = %s, DataDevolucao = %s 
                WHERE idAlocacao = %s
            """, 
            (
                alocacao.idUsuario,
                alocacao.id_Aparelho,
                alocacao.idSala,
                alocacao.DataAlocacao,
                alocacao.DataDevolucao,
                alocacao.idAlocacao
            ))
            conn.commit() 
        finally: 
            cursor.close()
            conn.close()

    def Deletar_Alocacao(self, alocacao): 
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM Alocacao
                WHERE idAlocacao = %s
            """, (alocacao.idAlocacao,))
            conn.commit() 
        finally: 
            cursor.close()
            conn.close()