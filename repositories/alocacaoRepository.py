from dbConnector.Database import DatabaseConnector


class AlocacaoRepository:
    def faz_connection(self):
        return DatabaseConnector().get_connection()

    def inserir_alocacao(self, id_usuario: int,id_aparelhos: list[int],id_sala: int,  data_alocacao: str,  data_devolucao: str,):
        conn = self.faz_connection()

        try:
            cursor = conn.cursor()

            cursor.execute("""INSERT INTO Alocacao
                (idUsuario,idSala,DataAlocacao,DataDevolucao)
                VALUES (%s,%s,%s,%s)""",(id_usuario,id_sala,data_alocacao,data_devolucao,),)
            id_alocacao = cursor.lastrowid
            cursor.executemany("""INSERT INTO Item_Alocacao(ID_Alocacao,ID_Aparelho)
                VALUES (%s,%s)
                """,
                [(id_alocacao, aparelho) for aparelho in id_aparelhos],)
            conn.commit()
            return id_alocacao
        except Exception as e: 
            return f"Erro! {e}"
        finally:
            cursor.close()
            conn.close()
    def listar_alocacoes(self):
        conn = self.faz_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT
                    al.idAlocacao,
                    u.Nome_Usuario,
                    s.NomeSala,
                    al.DataAlocacao,
                    al.DataDevolucao,

                    GROUP_CONCAT(
                        a.Patrimonio
                        ORDER BY a.Patrimonio
                    ) AS Patrimonios,

                    GROUP_CONCAT(
                        CONCAT(m.Marca,' ',mo.Modelo)
                        SEPARATOR ' | '
                    ) AS Aparelhos

                FROM Alocacao al

                JOIN Usuario u
                    ON al.idUsuario=u.idUsuario

                JOIN Sala s
                    ON al.idSala=s.idSala

                JOIN Item_Alocacao ia
                    ON al.idAlocacao=ia.ID_Alocacao

                JOIN Aparelho a
                    ON ia.ID_Aparelho=a.id_Aparelho

                JOIN Modelo_Aparelho mo
                    ON a.idModelo=mo.idModelo

                JOIN Marca m
                    ON mo.idMarca=m.idMarca

                GROUP BY
                    al.idAlocacao,
                    u.Nome_Usuario,
                    s.NomeSala,
                    al.DataAlocacao,
                    al.DataDevolucao

                ORDER BY
                    u.Nome_Usuario,
                    al.DataAlocacao;
                """
            )

            return cursor.fetchall()

        finally:
            cursor.close()
            conn.close()

    def buscar_alocacao(self, id_alocacao):
        conn = self.faz_connection()
        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT

                    al.idAlocacao,
                    al.DataAlocacao,
                    al.DataDevolucao,
                    al.idSala,
                    al.idUsuario,

                    GROUP_CONCAT(ia.ID_Aparelho)

                FROM Alocacao al

                LEFT JOIN Item_Alocacao ia
                    ON ia.ID_Alocacao=al.idAlocacao

                WHERE al.idAlocacao=%s

                GROUP BY al.idAlocacao
                """,
                (id_alocacao,),
            )

            return cursor.fetchone()

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
                DELETE FROM Alocacao
                WHERE idAlocacao=%s
                """,
                (id_alocacao,),
            )

            conn.commit()

        finally:
            cursor.close()
            conn.close()

    
repoAlocacao = AlocacaoRepository()