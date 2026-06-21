from dbConnector.Database import DatabaseConnector
from models.usuarios import *

class UsuarioRepository:

    def inserir_cargo(self, usuario):
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
            conn.close()

    def Consulta_template(self): 
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()

            cursor.execute("""SELECT u.ID_Usuario, u.Nome_Usuario,c.Nome_Cargo
            FROM Usuario u
            JOIN Cargo c ON u.ID_Cargo = c.ID_Cargo
            WHERE u.ID_Usuario = %s
        """, ((usuario.id_usuario,),))
        finally: 
            cursor.close()
            conn.close()

usuario1 = UsuarioRepository.inserir_usuario('Thales',1)

print(usuario1)