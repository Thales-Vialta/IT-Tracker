from dbConnector.Database import DatabaseConnector


class ManutencaoRepository:

    def Listar_Defeituosos(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT a.id_Aparelho,a.patrimonio, m.Modelo
                FROM Aparelho a
                INNER JOIN Modelo_Aparelho m
                ON a.idModelo = m.idModelo
                WHERE a.idStatus = 3
                        """
            )
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conn.close()

    def retorna_Total(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM Aparelho WHERE idStatus = 3")
            resultado = cursor.fetchone()
            return resultado
        finally:
            cursor.close()
            conn.close()

    def Tirar_da_Manutencao(self, id_aparelho):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE Aparelho 
            SET idStatus = 1 
            WHERE id_Aparelho = %s AND idStatus = 3""",
                (id_aparelho,),
            )
            conn.commit()
        except ValueError:
            print("Erro! Nome vazio")
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            conn.close()
