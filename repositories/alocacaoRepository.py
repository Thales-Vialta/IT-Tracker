from dbConnector.Database import DatabaseConnector


class AlocacaoRepository:

    def inserir_Alocacao(
        self,
        idUsuario: int,
        id_Aparelho: int,
        idSala: int,
        DataAlocacao: str,
        DataDevolucao: str,
    ):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO Alocacao
                (idUsuario, id_Aparelho, idSala, DataAlocacao, DataDevolucao)
                VALUES (%s, %s, %s, %s, %s)
            """,
                (idUsuario, id_Aparelho, idSala, DataAlocacao, DataDevolucao),
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def Aparelhos_menos_Alocados(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT id_Aparelho, COUNT(idAlocacao) as total_alocacoes
                FROM Alocacao 
                GROUP BY id_Aparelho
                ORDER BY total_alocacoes ASC;
            """
            )
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conn.close()

    def Listar_Alocacao(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
            SELECT
                al.idAlocacao,
                u.Nome_Usuario,
                a.Patrimonio,
                m.Marca,
                m.Modelo,
                sa.NomeSala,
                al.DataAlocacao,
                al.DataDevolucao
            FROM Alocacao al
            JOIN Usuario u ON al.idUsuario = u.idUsuario
            JOIN Aparelho a ON al.id_Aparelho = a.id_Aparelho
            JOIN Modelo_Aparelho m ON a.idModelo = m.idModelo
            JOIN Sala sa ON sa.idSala = al.idSala;
        """
            )
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            conn.close()



    def Buscar_Alocacao(self, idAlocacao: int):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT * FROM Alocacao WHERE idAlocacao LIKE %s""", (idAlocacao,)
            )
            resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            conn.close()

    def Editar_Alocacao(
        self,
        idUsuario: int,
        id_Aparelho: int,
        idSala: int,
        DataAlocacao: str,
        DataDevolucao: str,
        idAlocacao: int,
    ):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE Alocacao 
                SET idUsuario = %s, id_Aparelho = %s, idSala = %s, DataAlocacao = %s, DataDevolucao = %s 
                WHERE idAlocacao = %s
            """,
                (
                    idUsuario,
                    id_Aparelho,
                    idSala,
                    DataAlocacao,
                    DataDevolucao,
                    idAlocacao,
                ),
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def Deletar_Alocacao(self, idAlocacao: int):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                DELETE FROM Alocacao
                WHERE idAlocacao = %s
            """,
                (idAlocacao,),
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()
    def Listar_Alocacao_Gap_Data(self, data_inicio, data_fim):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
            """
            SELECT
                al.idAlocacao,
                u.Nome_Usuario,
                a.Patrimonio,
                m.Marca,
                m.Modelo,
                sa.NomeSala,
                al.DataAlocacao,
                al.DataDevolucao
            FROM Alocacao al
            JOIN Usuario u ON al.idUsuario = u.idUsuario
            JOIN Aparelho a ON al.id_Aparelho = a.id_Aparelho
            JOIN Modelo_Aparelho m ON a.idModelo = m.idModelo
            JOIN Sala sa ON sa.idSala = al.idSala
            WHERE al.DataAlocacao = %s AND al.Datadevolucao = %s; """,
            (data_inicio, data_fim)
        )
            return cursor.fetchall()

        except Exception as e:
            print(f"Erro ao listar alocações: {e}")

        finally:
            cursor.close()
            conn.close()

repoAlocacao = AlocacaoRepository()