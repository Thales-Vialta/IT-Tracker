from dbConnector.Database import DatabaseConnector

class HorarioRepository: 
    def Inserir_Horario(self, horafunc): 
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()     
            cursor.execute("""
                        INSERT INTO HorarioFunc
                        (Descricao,HoraInicio,HoraFim)
                        VALUES (%s,%s,%s)
                    """,
                    (
                        horafunc.Descricao,horafunc.HoraInicio,horafunc.HoraFim
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
                        SELECT HoraInicio, HoraFim, Descricao FROM HorarioFunc
                    """)
        
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()
repo = HorarioRepository()

for HoraInicio, HoraFim, Descricao in repo.Listar_Horario():
    print(f"+==========Lista de Horários==========+\n{Descricao} | {HoraInicio} - {HoraFim}")
