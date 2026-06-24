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

    def listarSalas(self):
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
            cursor.execute('''SELECT NomeSala FROM Sala ORDER BY NomeSala''')
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conn.close()

    def buscarSala(self, nome_sala: str):
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM Sala WHERE NomeSala LIKE %s''', (nome_sala,))
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conn.close()

    def removerSala(self, nome_sala: str):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('''DELETE FROM Sala WHERE NomeSala = %s''', (nome_sala,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def editarSala(self, nome_sala: str, atributo: str, valor: str):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            query = f"UPDATE Sala SET {atributo} = %s WHERE NomeSala = %s"
            cursor.execute(query, (valor, nome_sala))
            conn.commit()
        finally:
            cursor.close()
            conn.close()