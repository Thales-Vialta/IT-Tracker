from dbConnector.Database import DatabaseConnector
from models.usuarios import *

class ModeloRepository:

    def inserir_Modelo(self, idMarca: int, modelo: str):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute("""INSERT INTO Modelo_Aparelho(IDMarca, Modelo)VALUES (%s, %s)
        """, (idMarca, modelo))
            conn.commit()
        finally:
            cursor.close()
            conn.close()


    def listar_Modelos(self):
        conn = DatabaseConnector().get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute("""
            SELECT
                ma.Marca,
                mo.Modelo,
                COUNT(a.id_Aparelho) AS Quantidade_Disponivel
            FROM Modelo_Aparelho mo
            INNER JOIN Marca ma
                ON mo.idMarca = ma.idMarca
            LEFT JOIN Aparelho a
                ON mo.idModelo = a.idModelo
            LEFT JOIN Alocacao al
                ON a.id_Aparelho = al.id_Aparelho
                AND al.DataDevolucao >= NOW()
            WHERE al.idAlocacao IS NULL
            GROUP BY ma.Marca, mo.Modelo
            ORDER BY ma.Marca, mo.Modelo;""")

            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

    def buscar_Modelo(self, modelo):
        conn = DatabaseConnector().get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute("""SELECT mo.idModelo, ma.Marca, mo.Modelo
            FROM Modelo_Aparelho mo
            INNER JOIN Marca ma
            ON mo.idMarca = ma.idMarca
            WHERE mo.Modelo LIKE %s""", (modelo,))
            return cursor.fetchall()

        finally:
            cursor.close()
            conn.close()

    def Editar_Modelo(self, id, atributo, valor):
            conn = DatabaseConnector().get_connection()
            try: 
                cursor = conn.cursor()
                
                query = f"UPDATE Modelo_Aparelho SET {atributo} = %s WHERE idModelo = %s"
                
                cursor.execute(query, (valor, id))
                conn.commit()
                
            finally: 
                cursor.close()
                conn.close()

    def Deletar_Modelo(self,idModelo:int):
                conn = DatabaseConnector().get_connection()
                try: 
                    cursor = conn.cursor()
                    cursor.execute("""Delete from Modelo_Aparelho
                                   WHERE idModelo = %s""",(idModelo,))
                    conn.commit()
                    return cursor.rowcount
                except Exception as e:
                    print(f"Erro no serviço ao remover modelo: {e}")
                finally: 
                    cursor.close()
                    conn.close()

modeloRepo = ModeloRepository()