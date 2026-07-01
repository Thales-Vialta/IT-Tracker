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
                mo.Modelo
            FROM Modelo_Aparelho mo
            INNER JOIN Marca ma
                ON mo.idMarca = ma.idMarca
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
            WHERE mo.Modelo LIKE %s
            ORDER BY mo.Modelo;""", (modelo,))
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

    def Deletar_Modelo(self, idModelo: int):
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM Modelo_Aparelho WHERE idModelo = %s""", (idModelo,))
            conn.commit()
            return cursor.rowcount
            
        except Exception as e:
            erro_msg = str(e).lower()
            if "foreign key" in erro_msg or "constraint" in erro_msg or "1451" in erro_msg:
                return "vinculado"
            
            print(f"Erro no repositório ao remover modelo: {e}")
            return "erro"
            
        finally: 
            cursor.close()
            conn.close()

modeloRepo = ModeloRepository()