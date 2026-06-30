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


    def editar_Marca(self, idMarca, novaMarca):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Marca
                SET Marca = %s
                WHERE idMarca = %s
            """, (novaMarca, idMarca))

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

        finally:
            cursor.close()
            conn.close()

marcaRepo = MarcaRepository()