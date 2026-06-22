from dbConnector.Database import DatabaseConnector

class HorarioRepository: 
    def Inserir_Horario(self, horafunc): 
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()     
            cursor.execute("""
                        INSERT INTO HoraFunc
                        (Descricao,HoraInicio,HoraFim)
                        VALUES (%s,%s,%s)
                    """,
                    (
                        horafunc.HoraInicio,horafunc.HoraFim
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
                        SELECT * FROM HoraFunc
                    """)
        
            conn.commit()
        finally:
            cursor.close()
            conn.close()
