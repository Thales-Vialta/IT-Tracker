from dbConnector.Database import DatabaseConnector

class StatusRepository:

    def Inserir_Novo_Status(self, Descricao:str): 
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()     
            cursor.execute("""
                        INSERT INTO StatusAparelho
                        (Descricao)
                        VALUES (%s)
                    """, (Descricao))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def Listar_Aparelhos_Status(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()     
            cursor.execute("""
                        SELECT * FROM StatusAparelho
                    """)
            conn.commit()
        finally:
            cursor.close()
            conn.close()
    def editar_status(self, id_Aparelho, idStatus):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute("""UPDATE Aparelho SET idStatus = %s WHERE id_Aparelho = %s """, (idStatus, id_Aparelho))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def Editar_Aparelho(self,IdStatus:int,Descricao:str,idAparelho:int): 
            conn = DatabaseConnector().get_connection()
            try: 
                cursor = conn.cursor()
                cursor.execute("""UPDATE Aparelhos 
                               SET Descricao = %s, idModelo = %s 
                               WHERE id_Aparelho = %s""",(IdStatus,Descricao,idAparelho))
                resultado = cursor.fetchall()
                return resultado 
            finally: 
                cursor.close()
                conn.close()

    def Listar_Defeituosos(self):
            conn = DatabaseConnector().get_connection()
            try:
                cursor = conn.cursor()     
                cursor.execute("""
                    SELECT Status.Descricao 
                    FROM Aparelho
                    INNER JOIN Status ON Aparelho.IDStatus = Status.ID
                    WHERE Aparelho.IDStatus = 3
                        """)
                conn.commit()
            finally:
                cursor.close()
                conn.close()
repo = StatusRepository()