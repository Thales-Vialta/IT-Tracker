from dbConnector.Database import DatabaseConnector
from models.aparelhos import *


class AparelhoRepository:

    def inserir_aparelho(self, serial: str, statusAparelho: str, idModelo: int):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO Aparelho
                (Patrimonio,IDStatus,idModelo)
                VALUES (%s,%s,%s)
            """,
                (serial, statusAparelho, idModelo),
            )

            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def Listar_Todos_Aparelhos(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            # trocar essa consulta pra por o modelo dela, fica mais legível no sistema
            cursor.execute(
                """SELECT a.id_Aparelho,a.patrimonio,m.Marca,m.Modelo FROM Aparelho a
            JOIN Modelo_Aparelho m
            ON a.idModelo=m.idModelo 
            ORDER BY id_Aparelho"""
            )
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conn.close()

    def Buscar_Aparelho(self, idAparelho: int):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """Select * from Aparelho where id_Aparelho like %s""", (idAparelho,)
            )
            resultado = cursor.fetchall()
            return resultado
        except ValueError:
            print("Erro! Nome vazio")
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            conn.close()

    def Aparelho_mais_utilizado(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT patrimonio AS Aparelho_mais_utilizado from Aparelho
            WHERE id_Aparelho = (
            SELECT id_Aparelho
            FROM Alocacao
            GROUP BY id_Aparelho
            ORDER BY COUNT(*) DESC
            LIMIT 1)"""
            )
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conn.close()

    def Editar_Aparelho(self, serial: str, idModelo: int, statusAparelho: str):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE Aparelhos 
                           SET patrimonio = %s, idModelo = %s 
                           WHERE id = %s""",
                (serial, idModelo, statusAparelho),
            )
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conn.close()

    def Deletar_Aparelho(self, statusAparelho: str):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """Delete from Aparelhos 
                               WHERE id_Aparelho = %s""",
                (statusAparelho),
            )
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conn.close()


repo = AparelhoRepository()
for serial in repo.Aparelho_mais_utilizado():
    print(f"{serial}")
