from dbConnector.Database import DatabaseConnector
from models.aparelhos import *


class AparelhoRepository:

    def inserir_aparelho(self, serial: str, statusAparelho: str, idModelo: int):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO Aparelho
                (Patrimonio,IDStatus,idModelo)
                VALUES (%s,%s,%s)
            """,
                (serial, statusAparelho, idModelo),
            )

            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def Listar_Todos_Aparelhos(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""SELECT a.id_Aparelho, a.patrimonio, ma.Marca,  mo.Modelo 
            FROM Aparelho a
            INNER JOIN Modelo_Aparelho mo
            ON a.idModelo = mo.idModelo
            INNER JOIN Marca ma
            ON mo.IDMarca = ma.IDMarca
            ORDER BY mo.Modelo, a.patrimonio;"""
            )
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conn.close()

    def Buscar_Aparelho(self, idAparelho: int):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """Select * from Aparelho where id_Aparelho like %s""", (idAparelho,)
            )
            resultado = cursor.fetchall()
            return resultado # <--- CORRIGIDO: Retorna a lista pura, sem f-string
        except ValueError:
            print("Erro! Nome vazio")
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            conn.close()

    def Aparelho_mais_utilizado(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT patrimonio AS Aparelho_mais_utilizado from Aparelho
            WHERE id_Aparelho = (
            SELECT id_Aparelho
            FROM Alocacao
            GROUP BY id_Aparelho
            ORDER BY COUNT(*) DESC
            LIMIT 1)"""
            )
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conn.close()

    def Editar_Aparelho(self, atributo, valor, id_Aparelho):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
        
            sql = f"UPDATE Aparelho SET `{atributo}` = %s WHERE id_Aparelho = %s"
    
            cursor.execute(sql, (valor, id_Aparelho))
        
            conn.commit() 
            return cursor.rowcount
    
        finally:
            cursor.close()
            conn.close()


    def Deletar_Aparelho(self, idAparelho: str):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """Delete from Aparelho
                               WHERE id_Aparelho = %s""",
                (idAparelho,)
            )
            conn.commit()
            return True
            
        finally:
            cursor.close()
            conn.close()

    def Listar_Aparelhos_Disponiveis(self, marca=None):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            
            # 1. Se a marca foi informada
            if marca and marca.strip():
                query_marca = """
                    SELECT 
                        a.id_Aparelho, 
                        a.patrimonio, 
                        ma.Marca, 
                        m.Modelo
                    FROM Aparelho a
                    JOIN Modelo_Aparelho m ON a.idModelo = m.idModelo
                    JOIN Marca ma ON m.IDMarca = ma.IDMarca
                    WHERE ma.Marca = %s 
                    AND a.idStatus = 1;
                """
                cursor.execute(query_marca, (marca,))
                resultado = cursor.fetchall()
                if resultado:
                    return resultado
            
            # 2. CONTINGÊNCIA / GERAL (O que está sendo chamado na criação da reserva)
            query_geral = """
                SELECT 
                    a.id_Aparelho, 
                    a.patrimonio, 
                    ma.Marca, 
                    m.Modelo
                FROM Aparelho a
                JOIN Modelo_Aparelho m ON a.idModelo = m.idModelo
                JOIN Marca ma ON m.IDMarca = ma.IDMarca
                WHERE a.idStatus = 1;
            """
            cursor.execute(query_geral)
            return cursor.fetchall()

        except Exception as e:
            print(f"Erro ao listar aparelhos disponíveis: {e}")
            return []
            
        finally:
            cursor.close()
            conn.close()

    def Buscar_Aparelho_Por_Serial(self, serial: str):
            conn = DatabaseConnector().get_connection()
            try:
                cursor = conn.cursor()
                # Busca na tabela Aparelho onde a coluna Patrimonio bate com o serial enviado
                cursor.execute(
                    """SELECT * FROM Aparelho WHERE Patrimonio = %s;""", (serial,)
                )
                resultado = cursor.fetchall()
                return resultado # Retorna a lista pura de tuplas
                
            except Exception as e:
                print(f"Erro ao buscar aparelho por serial: {e}")
                return []
            finally:
                cursor.close()
                conn.close()

repoAp = AparelhoRepository()

