from dbConnector.Database import DatabaseConnector

class HorarioRepository:

    def Cadastrar_Horario(self, Descricao:str,HoraInicio:str,HoraFim:str): 
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()     
            cursor.execute("""
                        INSERT INTO HorarioFunc
                        (Descricao,HoraInicio,HoraFim)
                        VALUES (%s,%s,%s)
                    """,(Descricao,HoraInicio,HoraFim))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
            
    def Editar_Horario(self, atributo , novo_valor, descricao):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(f"""UPDATE HorarioFunc
            SET {atributo} = %s
            WHERE Descricao = %s
            """,(novo_valor, descricao))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def buscar_Horario(self,Descricao):
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
            cursor.execute('''Select * from HorarioFunc where Descricao like %s''',(Descricao,))
            resultado = cursor.fetchall()
            return resultado
        except ValueError: 
            print("Erro! Nome vazio")
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            conn.close() 

    def remover_Horario(self,Descricao): 
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
            cursor.execute('''Delete from HorarioFunc where Descricao like %s''',(Descricao,))
            resultado = cursor.fetchall()
            return resultado
        except ValueError: 
            print("Erro! Nome vazio")
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            conn.close() 
    def Mostrar_Horario(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()     
            cursor.execute("""
                        SELECT HoraInicio, HoraFim, Descricao FROM HorarioFunc
                    """)
        
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

horarioRepo = HorarioRepository()

