from dbConnector.Database import DatabaseConnector

class UsuarioRepository:

    def inserir_usuario(self, nome_usuario: str, id_cargo: int):
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
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
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
            cursor.execute('''
                SELECT u.Nome_Usuario, c.Cargos 
                FROM Usuario u
                INNER JOIN Cargo c ON u.ID_Cargo = c.ID_Cargo
                ORDER BY u.Nome_Usuario
            ''')
            resultado = cursor.fetchall()
            return resultado
        except ValueError: 
                print("Erro! Nome vazio")
        except Exception as e:
                print(f"Erro ao inserir usuário: {e}")
        finally:
                cursor.close()
                conn.close()

    def buscarUsuario(self, nome_usuario: str):
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
            cursor.execute('''Select * from Usuario where Nome_Usuario like %s''',(nome_usuario,))
            resultado = cursor.fetchall()
            return resultado
        except ValueError: 
                print("Erro! Nome vazio")
        except Exception as e:
                print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            conn.close()

    def removerUsuario(self, nome_usuario: str):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('''DELETE FROM Usuario WHERE Nome_Usuario = %s''', (nome_usuario,))
            conn.commit()
            return True
        except Exception as e:
            if "a foreign key constraint fails" in str(e).lower() or "1451" in str(e):
                return "vinculado"
            print(f"Erro ao remover usuário: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
   
    def editarUsuario(self, nome_usuario: str, atributo: str, valor: str):
           conn = DatabaseConnector().get_connection()
           try:
               cursor = conn.cursor()
               query = f"UPDATE Usuario SET {atributo} = %s WHERE Nome_Usuario = %s"
               cursor.execute(query, (valor, nome_usuario))
               conn.commit()
           finally:
               cursor.close()
               conn.close()

userRepo = UsuarioRepository()