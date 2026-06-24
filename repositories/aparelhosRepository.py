from dbConnector.Database import DatabaseConnector
from models.aparelhos import *

class AparelhoRepository:

    def inserir_aparelho(self, Aparelhos):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Aparelho
                (Patrimonio,IDStatus,idModelo)
                VALUES (%s,%s,%s)
            """,
            (
                Aparelhos.serial,Aparelhos.statusAparelho,Aparelhos.idModelo
            ))

            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def Aparelho_mais_utilizado(self): 
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
#trocar essa consulta pra por o modelo dela, fica mais legível no sistema
            cursor.execute("""SELECT patrimonio AS Aparelho_mais_utilizado from Aparelho
            WHERE id_Aparelho = (
            SELECT id_Aparelho
            FROM Alocacao
            GROUP BY id_Aparelho
            ORDER BY COUNT(*) DESC
            LIMIT 1)""")
            resultado = cursor.fetchall()
            return resultado
        finally: 
            cursor.close()
            conn.close()

    def Editar_Aparelho(self): 
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
            cursor.execute("""UPDATE Aparelhos 
                           SET patrimonio = %s, idModelo = %s 
                           WHERE id = %s""",(Aparelhos.serial,Aparelhos.idModelo,Aparelhos.statusAparelho))
            resultado = cursor.fetchall()
            return resultado 
        finally: 
            cursor.close()
            conn.close()
            
    def Deletar_Aparelho(self): 
            conn = DatabaseConnector().get_connection()
            try: 
                cursor = conn.cursor()
                cursor.execute("""Delete from Aparelhos 
                               WHERE id_Aparelho = %s""",(Aparelhos.statusAparelho))
                resultado = cursor.fetchall()
                return resultado 
            finally: 
                cursor.close()
                conn.close()

repo = AparelhoRepository()
for serial in repo.Aparelho_mais_utilizado():
    print(f"{serial}")