from dbConnector.Database import DatabaseConnector

class HorarioRepository:

    def Inserir_Horario(self, Descricao:str,HoraInicio:str,HoraFim:str): 
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()     
            cursor.execute("""
                        INSERT INTO HorarioFunc
                        (Descricao,HoraInicio,HoraFim)
                        VALUES (%s,%s,%s)
                    """,(Descricao,HoraInicio,HoraFim))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def Listar_Horario(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()     
            cursor.execute("""
                        SELECT HoraInicio, HoraFim, Descricao FROM HorarioFunc
                    """)
        
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

horarioRepo = HorarioRepository()

