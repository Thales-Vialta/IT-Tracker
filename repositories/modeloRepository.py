from dbConnector.Database import DatabaseConnector
from models.usuarios import *

class ModeloRepository:

    def inserir_Modelo(self, Marca:str,Modelo_do_Aparelho:str):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Modelo_Aparelho
                (Marca, Modelo)
                VALUES (%s, %s)
            """,(Marca,Modelo_do_Aparelho))
            conn.commit()
        finally:
            cursor.close()
            conn.close()


    def listar_Modelos(self): 
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
            cursor.execute('''Select m.Marca,m.Modelo, count(a.id_Aparelho) as Quantidade_Disponivel 
                           from Aparelho a 
                           join Modelo_Aparelho m on a.idModelo = m.idModelo
                           left join Alocacao al on a.id_Aparelho = al.id_Aparelho 
                           and al.DataDevolucao >= NOW()
                           Where al.idAlocacao is Null
                           group by m.Marca, m.Modelo Order by m.Marca, m.Modelo''')
            resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            conn.close()

    def buscar_Modelo(self,Modelo:str): 
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
            cursor.execute('''Select * from Modelo_Aparelho where Modelo like %s''',(Modelo,))
            resultado = cursor.fetchall()
            return resultado
        except ValueError: 
                print("Erro! Nome vazio")
        except Exception as e:
                print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            conn.close()

    
    def Aparelhos_menos_Alocados(self):
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()

            cursor.execute("""Select a.patrimonio, m.Marca, m.Modelo, COUNT(al.idAlocacao) as Aparelhos_menos_Alocados
            from Aparelho a INNER JOIN Modelo_Aparelho m 
            ON a.idModelo = m.idModelo 
            LEFT JOIN Alocacao al on a.id_Aparelho = al.id_Aparelho 
            group by a.id_Aparelho
            ORDER BY Aparelhos_menos_Alocados;""")
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conn.close()
    
    def Editar_Modelo(self,Marca:str,Modelo_do_Aparelho:str,idModelo:int):
            conn = DatabaseConnector().get_connection()
            try: 
                cursor = conn.cursor()
                cursor.execute("""UPDATE Modelo_Aparelho 
                               SET Marca = %s, Modelo = %s 
                               WHERE idModelo = %s""",(Marca,Modelo_do_Aparelho,idModelo))
                resultado = cursor.fetchall()
                return resultado 
            finally: 
                cursor.close()
                conn.close()

    def Deletar_Modelo(self,idModelo:int):
                conn = DatabaseConnector().get_connection()
                try: 
                    cursor = conn.cursor()
                    cursor.execute("""Delete from Modelo_Aparelho
                                   WHERE idModelo = %s""",(idModelo,))
                    conn.commit()
                    return cursor.rowcount
                except Exception as e:
                    print(f"Erro no serviço ao remover modelo: {e}")
                finally: 
                    cursor.close()
                    conn.close()

modeloRepo = ModeloRepository()