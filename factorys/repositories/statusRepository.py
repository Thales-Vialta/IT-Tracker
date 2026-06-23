from dbConnector.Database import DatabaseConnector

class HorarioRepository: 
    def Inserir_Horario(self, StatusAparelho): 
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()     
            cursor.execute("""
                        INSERT INTO StatusAparelho
                        (Descricao)
                        VALUES (%s)
                    """,
                    (
                        StatusAparelho.Descricao
                    ))
        
            conn.commit()
        finally:
            cursor.close()
            conn.close()
    def Listar_Horario(self):
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

    def Editar_Aparelho(self,StatusAparelho): 
            conn = DatabaseConnector().get_connection()
            try: 
                cursor = conn.cursor()
                cursor.execute("""UPDATE Aparelhos 
                               SET Descricao = %s, idModelo = %s 
                               WHERE id = %s""",(StatusAparelho.IdStatus,StatusAparelho.Descricao))
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