from dbConnector.Database import DatabaseConnector

class salaRepository: 
    def Inserir_Sala(self, sala): 
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()     
            cursor.execute("""
                        INSERT INTO Sala
                        (idSala,NomeSala,EnderecoSala)
                        VALUES (%s,%s,%s)
                    """,
                    (
                        sala.idSala,sala.NomeSala,sala.EnderecoSala
                    ))
            print('sala cadastrada com sucesso')
            conn.commit()
        except Exception as e:
            print(f"Erro ao inserir sala: {e}")
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
