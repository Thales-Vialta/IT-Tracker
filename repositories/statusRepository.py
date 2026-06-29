from dbConnector.Database import DatabaseConnector

class StatusRepository:

    def Listar_Aparelhos_Status(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()     
            cursor.execute("""
                        SELECT * FROM StatusAparelho
                    """)
            conn.commit()
        finally:
            cursor.close()
            conn.close()


    def editar_status(self, idAparelho:int, idStatus:int):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute("""UPDATE Aparelho SET idStatus = %s WHERE id_Aparelho = %s """, (idStatus, idAparelho))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def Mostrar_Novo_Status(self,idAparelho: int): 
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""SELECT m.Modelo, s.Descricao FROM Aparelho a
            INNER JOIN Modelo_Aparelho m
            ON a.idModelo = m.idModelo
            INNER JOIN StatusAparelho s
            ON a.idStatus = s.idStatus
            WHERE a.id_Aparelho = %s;""", (idAparelho,))
            resultado = cursor.fetchone()
            return resultado 
        except ValueError: 
                print("Erro! Nome vazio")
        except Exception as e:
                print(f"Erro ao inserir usuário: {e}")
                
        finally:
            cursor.close()
            conn.close()


  

repo = StatusRepository()