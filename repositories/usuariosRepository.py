from dbConnector.Database import DatabaseConnector
from models.usuarios import *

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
            conn.close()

    def Usuario_Nunca_Alocou(self): 
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()

            cursor.execute("""SELECT idUsuario, Nome_Usuario AS Usuario_Nunca_Alocou
            FROM Usuario
            WHERE idUsuario NOT IN (
            SELECT idUsuario
            FROM Alocacao)""")
            resultado = cursor.fetchall()
            return resultado
            
        finally: 
            cursor.close()
            conn.close()

    def listarUsuarios():
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
            cursor.execute('''Select Nome_Usuario from Usuario Order by Nome_Usuario''')
            resultado = cursor.fetchall()
            return resultado
        except ValueError: 
                print("Erro! Nome vazio")
        finally:
                cursor.close()
                conn.close()

    def buscarUsuario(self,usuario):
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
            cursor.execute('''Select * from Usuario where Nome_Usuario like %s''',(usuario.nome_usuario))
            resultado = cursor.fetchall()
            return resultado
        except ValueError: 
                print("Erro! Nome vazio")
        finally:
            cursor.close()
            conn.close()
        
    
repo = UsuarioRepository()

for id_usuario, nome in repo.Usuario_Nunca_Alocou():
    print(f"{id_usuario} - {nome}")

