from dbConnector.Database import DatabaseConnector


class AlocacaoRepository:
    def faz_connection(self):
        return DatabaseConnector().get_connection()

    def inserir_Alocacao_Principal(self, idUsuario: int, idSala: int, DataAlocacao: str, DataDevolucao: str) -> int:
            conn = DatabaseConnector().get_connection()
            try:
                cursor = conn.cursor()
                # Note que não passamos mais o aparelho aqui!
                query = """
                    INSERT INTO Alocacao (idUsuario, idSala, DataAlocacao, DataDevolucao)
                    VALUES (%s, %s, %s, %s);
                """
                cursor.execute(query, (idUsuario, idSala, DataAlocacao, DataDevolucao))
                conn.commit()
                
                # RETORNA o ID que o AUTO_INCREMENT acabou de criar no banco
                return cursor.lastrowid
            finally:
                cursor.close()
                conn.close()

    def inserir_Item_Alocacao(self, idAlocacao: int, idAparelho: int):
            conn = DatabaseConnector().get_connection()
            try:
                cursor = conn.cursor()
                # Preste atenção se os nomes batem com as maiúsculas/minúsculas do seu banco (ex: ID_Alocacao)
                query = """
                    INSERT INTO Item_Alocacao (ID_Alocacao, ID_Aparelho)
                    VALUES (%s, %s);
                """
                cursor.execute(query, (idAlocacao, idAparelho))
                conn.commit()
            finally:
                cursor.close()
                conn.close()



    def listar_alocacoes(self):
            conn = DatabaseConnector().get_connection()
            try:
                cursor = conn.cursor()
                
                query = """
                    SELECT
                        al.idAlocacao,
                        IFNULL(u.Nome_Usuario, 'Usuário não encontrado') AS Nome_Usuario,
                        IFNULL(sa.NomeSala, 'Sala não encontrada') AS NomeSala,
                        al.DataAlocacao,
                        al.DataDevolucao,
                        IFNULL(GROUP_CONCAT(a.patrimonio SEPARATOR ', '), 'Sem aparelho') AS patrimonios,
                        IFNULL(GROUP_CONCAT(CONCAT(ma.Marca, ' ', mo.Modelo) SEPARATOR ' | '), 'N/A') AS aparelhos
                    FROM Alocacao al
                    LEFT JOIN Usuario u ON al.idUsuario = u.idUsuario
                    LEFT JOIN Sala sa ON sa.idSala = al.idSala
                    LEFT JOIN Item_Alocacao it ON al.idAlocacao = it.ID_Alocacao
                    LEFT JOIN Aparelho a ON it.ID_Aparelho = a.id_Aparelho
                    LEFT JOIN Modelo_Aparelho mo ON a.idModelo = mo.idModelo
                    LEFT JOIN Marca ma ON mo.IDMarca = ma.IDMarca
                    GROUP BY al.idAlocacao;
                """
                
                cursor.execute(query)
                resultado = cursor.fetchall()
                return resultado 

            except Exception as e:
                print(f"Erro ao listar alocações no repositório: {e}")
                return []
            finally:
                cursor.close()
                conn.close()



    def buscar_alocacao(self, id_alocacao: int):
            conn = DatabaseConnector().get_connection()
            try:
                cursor = conn.cursor()
                query = """
                    SELECT 
                        al.idAlocacao,
                        al.DataAlocacao,
                        al.DataDevolucao,
                        sa.NomeSala,
                        u.Nome_Usuario,
                        GROUP_CONCAT(a.patrimonio SEPARATOR ', ') AS ids_aparelhos
                    FROM Alocacao al
                    LEFT JOIN Usuario u ON al.idUsuario = u.idUsuario
                    LEFT JOIN Sala sa ON sa.idSala = al.idSala
                    LEFT JOIN Item_Alocacao it ON al.idAlocacao = it.ID_Alocacao
                    LEFT JOIN Aparelho a ON it.ID_Aparelho = a.id_Aparelho
                    WHERE al.idAlocacao = %s
                    GROUP BY al.idAlocacao;
                """
                cursor.execute(query, (id_alocacao,))
                resultado = cursor.fetchall()
                
                # Se encontrar, retorna a primeira linha (a tupla). Se não, retorna None.
                return resultado[0] if resultado else None
            finally:
                cursor.close()
                conn.close()

    def editar_alocacao(self, atributo, valor, id_alocacao):

        conn = self.faz_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(f"""UPDATE Alocacao SET {atributo} = %s WHERE idAlocacao = %s""",(valor, id_alocacao),)
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def deletar_alocacao(self, id_alocacao):
        conn = self.faz_connection()
        try:
            cursor = conn.cursor()

        
            cursor.execute(
            """
            DELETE FROM Item_Alocacao
            WHERE ID_Alocacao = %s
            """,
            (id_alocacao,),
        )
            cursor.execute(
            """
            DELETE FROM Alocacao
            WHERE idAlocacao = %s
            """,
            (id_alocacao,),
        )

            conn.commit()

        except Exception as e:
            conn.rollback() 
            raise e
        finally:
            cursor.close()
            conn.close()
    

    def editar_alocacao_principal(self, coluna: str, valor, id_alocacao: int):
            conn = DatabaseConnector().get_connection()
            try:
                cursor = conn.cursor()
                # Injetamos o nome da coluna de forma segura usando f-string apenas para a estrutura,
                # e o valor (dado do usuário) via %s de forma protegida contra SQL Injection
                query = f"UPDATE Alocacao SET {coluna} = %s WHERE idAlocacao = %s;"
                cursor.execute(query, (valor, id_alocacao))
                conn.commit()
            finally:
                cursor.close()
                conn.close()    

    def limpar_itens_alocacao(self, id_alocacao: int):
            conn = DatabaseConnector().get_connection()
            try:
                cursor = conn.cursor()
                query = "DELETE FROM Item_Alocacao WHERE ID_Alocacao = %s;"
                cursor.execute(query, (id_alocacao,))
                conn.commit()
            finally:
                cursor.close()
                conn.close()
repoAlocacao = AlocacaoRepository()