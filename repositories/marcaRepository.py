from dbConnector.Database import DatabaseConnector

class MarcaRepository:

    def inserir_Marca(self, marca: str):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Marca (Marca)
                VALUES (%s)
            """, (marca,))

            conn.commit()

        finally:
            cursor.close()
            conn.close()


    def listar_Marcas(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT idMarca, Marca
                FROM Marca
                ORDER BY Marca;
            """)

            return cursor.fetchall()

        finally:
            cursor.close()
            conn.close()


    def buscar_Marca(self, marca):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT idMarca, Marca
                FROM Marca
                WHERE Marca LIKE %s
                ORDER BY Marca;
            """, (marca,))

            return cursor.fetchall()

        finally:
            cursor.close()
            conn.close()


    def Editar_Marca(self, idMarca, atributo, valor):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            coluna = "Marca" if atributo == "NomeMarca" else atributo

            query = f"""
                UPDATE Marca
                SET {coluna} = %s
                WHERE idMarca = %s
            """

            cursor.execute(query, (valor, idMarca))
            conn.commit()

        finally:
            cursor.close()
            conn.close()


    def excluir_Marca(self, idMarca):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM Marca
                WHERE idMarca = %s
            """, (idMarca,))

            conn.commit()
            return True
        
        except Exception as e:
            if "a foreign key constraint fails" in str(e).lower() or "1451" in str(e):
                return "vinculado"
            print(f"Erro ao remover marca no repositório: {e}")
            return False

        finally:
            cursor.close()
            conn.close()

marcaRepo = MarcaRepository()