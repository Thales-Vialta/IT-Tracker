from dbConnector.Database import DatabaseConnector
from models.usuarios import *

class ModeloRepository:

    def inserir_Modelo(self, Modelo):
        conn = DatabaseConnector().get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Modelo
                (Marca, Modelo)
                VALUES (%s, %s)
            """,
            (
                Modelo.Marca,
                Modelo.Modelo_do_Aparelho
            ))

            conn.commit()

        finally:
            cursor.close()
            conn.close()

    def Aparelhos_menos_Alocados(self): 
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()

            cursor.execute("""Select a.patrimonio, m.Marca, m.Modelo, COUNT(al.idAlocacao) as Aparelhos_menos_Alocados
            from Aparelho a INNER JOIN Modelo_Aparelho m 
            ON a.idModelo = m.idModelo 
            LEFT JOIN Alocacao al on a.id_Aparelho = al.id_Aparelho 
            group by a.id_Aparelho
            ORDER BY Aparelhos_menos_Alocados;""")
            resultado = cursor.fetchall()
            return resultado
            
        finally: 
            cursor.close()
            conn.close()
    
    def Editar_Modelo(self,Modelo): 
            conn = DatabaseConnector().get_connection()
            try: 
                cursor = conn.cursor()
                cursor.execute("""UPDATE Modelo_Aparelho 
                               SET Marca = %s, Modelo = %s 
                               WHERE idModelo = %s""",(Modelo.Marca,Modelo.Modelo_do_Aparelho,Modelo.idModelo))
                resultado = cursor.fetchall()
                return resultado 
            finally: 
                cursor.close()
                conn.close()

    def Deletar_Aparelho(self,Modelo): 
                conn = DatabaseConnector().get_connection()
                try: 
                    cursor = conn.cursor()
                    cursor.execute("""Delete from Modelo_Aparelho
                                   WHERE id_Aparelho = %s""",(Modelo.idModelo))
                    resultado = cursor.fetchall()
                    return resultado 
                finally: 
                    cursor.close()
                    conn.close()