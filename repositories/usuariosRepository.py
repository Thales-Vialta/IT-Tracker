from dbConnector.Database import DatabaseConnector
from models.usuarios import *

class UsuarioRepository:

    def inserir_usuario(self, Usuario):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Usuario
                (Nome_Usuario, ID_Cargo)
                VALUES (%s, %s)
            """,
            (
                Usuario.nome_usuario,
                Usuario.id_cargo
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

    def listarUsuarios(self):
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

    def buscarUsuario(self,Usuario):
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
            cursor.execute('''Select * from Usuario where Nome_Usuario like %s''',(Usuario.nome_usuario))
            resultado = cursor.fetchall()
            return resultado
        except ValueError: 
                print("Erro! Nome vazio")
        finally:
            cursor.close()
            conn.close()

    def removerUsuario(self, Usuario):
           conn = DatabaseConnector().get_connection()
           try:
               cursor = conn.cursor()
               cursor.execute('''DELETE FROM Usuario WHERE Nome_Usuario = %s''', (Usuario.nome_usuario,))
               conn.commit()
           finally:
               cursor.close()
               conn.close()
   
    def editarUsuario(self, nome_sala: str, atributo: str, valor: str):
           conn = DatabaseConnector().get_connection()
           try:
               cursor = conn.cursor()
               query = f"UPDATE Sala SET {atributo} = %s WHERE NomeSala = %s"
               cursor.execute(query, (valor, nome_sala))
               conn.commit()
           finally:
               cursor.close()
               conn.close()