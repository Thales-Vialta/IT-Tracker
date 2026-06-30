from dbConnector.Database import DatabaseConnector


class AlocacaoRepository:

    def inserir_Alocacao(
        self,
        idUsuario: int,
        id_Aparelho: int,
        idSala: int,
        DataAlocacao: str,
        DataDevolucao: str,
    ):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO Alocacao
                (idUsuario, id_Aparelho, idSala, DataAlocacao, DataDevolucao)
                VALUES (%s, %s, %s, %s, %s)
            """,
                (idUsuario, id_Aparelho, idSala, DataAlocacao, DataDevolucao),
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def Aparelhos_menos_Alocados(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT id_Aparelho, COUNT(idAlocacao) as total_alocacoes
                FROM Alocacao 
                GROUP BY id_Aparelho
                ORDER BY total_alocacoes ASC;
            """
            )
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            conn.close()

    def Listar_Alocacao(self):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
            SELECT
            u.Nome_Usuario,
            GROUP_CONCAT(a.Patrimonio ORDER BY a.Patrimonio SEPARATOR ', ') AS Patrimonios,
            al.DataAlocacao,
            al.DataDevolucao,
            sa.NomeSala
            FROM Alocacao al
            JOIN Usuario u ON al.idUsuario = u.idUsuario
            JOIN Aparelho a ON al.id_Aparelho = a.id_Aparelho
            JOIN Sala sa ON sa.idSala = al.idSala
            ORDER BY u.idUsuario, al.DataAlocacao, al.DataDevolucao, al.idAlocacao;;""")
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            conn.close()



    def Buscar_Alocacao(self, idAlocacao: int):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT * FROM Alocacao WHERE idAlocacao LIKE %s""", (idAlocacao,)
            )
            resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            conn.close()

    def Editar_Alocacao( self,atributo: str, valor: str,idAlocacao: int):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(f"""
                UPDATE Alocacao SET {atributo} = %s
                WHERE idAlocacao = %s
            """,
                (valor,idAlocacao),
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def Deletar_Alocacao(self, idAlocacao: int):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                DELETE FROM Alocacao
                WHERE idAlocacao = %s
            """,
                (idAlocacao,),
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def Listar_Aparelhos_Disponiveis(self, data_inicio, data_fim, marca_desejada):
        conn = DatabaseConnector().get_connection()
        try:
            cursor = conn.cursor()
            
            # 1ª TENTATIVA: Buscar disponíveis da MARCA ESPECÍFICA
            query_marca = """
                SELECT 
                    a.id_Aparelho, 
                    a.patrimonio, 
                    m.Marca, 
                    m.Modelo
                FROM Aparelho a
                JOIN Modelo_Aparelho m ON a.idModelo = m.idModelo
                WHERE m.Marca = %s 
                AND a.id_Aparelho NOT IN (
                    SELECT id_Aparelho 
                    FROM Alocacao 
                    WHERE DataAlocacao < %s 
                    AND DataDevolucao > %s
                );
            """
            
            # Executa passando a marca, data_fim e data_inicio
            cursor.execute(query_marca, (marca_desejada, data_fim, data_inicio))
            resultado = cursor.fetchall()
            
            # Se encontrou aparelhos da marca desejada, já retorna eles
            if resultado:
                return resultado
                
            # 2ª TENTATIVA: Se não achou nenhum daquela marca, busca QUALQUER marca disponível
            print(f"Nenhum aparelho da marca '{marca_desejada}' disponível. Buscando alternativas...")
            
            query_geral = """
                SELECT 
                    a.id_Aparelho, 
                    a.patrimonio, 
                    m.Marca, 
                    m.Modelo
                FROM Aparelho a
                JOIN Modelo_Aparelho m ON a.idModelo = m.idModelo
                WHERE a.id_Aparelho NOT IN (
                    SELECT id_Aparelho 
                    FROM Alocacao 
                    WHERE DataAlocacao < %s 
                    AND DataDevolucao > %s
                );
            """
            
            cursor.execute(query_geral, (data_fim, data_inicio))
            return cursor.fetchall()

        except Exception as e:
            print(f"Erro ao listar aparelhos disponíveis: {e}")
            return []
            
        finally:
            cursor.close()
            conn.close()

repoAlocacao = AlocacaoRepository()