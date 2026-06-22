from dbConnector.Database import DatabaseConnector

class salaRepository: 
    def Inserir_Horario(self, sala): 
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()     
            cursor.execute("""
                        INSERT INTO HoraFunc
                        (NomeSala,EnderecoSala)
                        VALUES (%s,%s)
                    """,
                    (
                        sala.NomeSala,sala.EnderecoSala
                    ))
        
            conn.commit()
        finally:
            cursor.close()
            conn.close()
    def Total_Por_Sala(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()     
            cursor.execute("""
            SELECT s.NomeSala,COUNT(al.id_Aparelho) AS Total_Por_Sala
            FROM Sala s LEFT JOIN Alocacao al
            ON s.idSala = al.idSala
            GROUP BY s.idSala;""")
            conn.commit()
        finally:
            cursor.close()
            conn.close()
