from dbConnector.Database import DatabaseConnector
from services.userService import usuarioService
class UsuarioRepository:

    def inserir_usuario(self, nome_usuario, id_cargo):
        conn = DatabaseConnector().get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Usuario
                (Nome_Usuario, ID_Cargo)
                VALUES (%s, %s)
            """,
            (
                nome_usuario,
                id_cargo
            ))

            conn.commit()

        finally:
            cursor.close()
            conn.close()

def buscarIdCargo(self, cargo: str):
        conn = DatabaseConnector().get_connection()
        with conn.cursor() as cursor:
            try: 
                cursor.execute('''SELECT idCargo FROM Cargo WHERE Cargos = %s''', (cargo,))
                resultado = cursor.fetchall()
                return resultado if resultado else None
            except ValueError: 
                print("Erro! Nome vazio")
            finally:
                conn.close()

def listarUsuarios(self):
    conn = DatabaseConnector().get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT Nome_Usuario
            FROM Usuario
            ORDER BY Nome_Usuario
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()

def buscarUsuario(self, nome_usuario):
    conn = DatabaseConnector().get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Usuario
            WHERE Nome_Usuario = %s
            """,
            (nome_usuario,)
        )

        return cursor.fetchone()

    finally:
        cursor.close()
        conn.close()

def editarUsuario(self, nome_usuario, atributo, valor):
    conn = DatabaseConnector().get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
                        UPDATE Usuario
                        SET {atributo} = %s
                        WHERE Nome_Usuario = %s
                    """, (valor, nome_usuario))
        resultado = cursor.fetchone()
        conn.commit()
        return resultado
    finally:
        cursor.close()
        conn.close()

def removerUsuario(self, nome_usuario):
    conn = DatabaseConnector().get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM Usuario
            WHERE Nome_Usuario = %s
            """,
            (nome_usuario,)
        )

        conn.commit()

    finally:
        cursor.close()
        conn.close()