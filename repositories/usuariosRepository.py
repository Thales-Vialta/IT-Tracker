from Singleton.Database import DatabaseConnector
class UsuarioRepository:

    def inserir_usuario(self, usuario):

        conn = DatabaseConnector().get_connection()

        try:

            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Usuario
                (Nome_Usuario, ID_Cargo)
                VALUES (%s, %s)
            """,
            (
                usuario.nome_usuario,
                usuario.id_cargo
            ))

            conn.commit()

        finally:

            cursor.close()