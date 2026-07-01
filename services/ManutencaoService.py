from repositories.ManutencaoRepository import ManutencaoRepo

class ManutencaoService:
    
    def __init__(self, ManutencaoRepo):
        self.repository = ManutencaoRepo

    def obter_aparelhos_defeituosos(self):

        aparelhos = self.repository.Listar_Defeituosos()
        
        if not aparelhos:
            return 
            
        return aparelhos
    def adicionar_aparelho_na_manutencao(self, id_aparelho,):
        if not id_aparelho or int(id_aparelho) <= 0:
            raise ValueError("ID do aparelho inválido.")
            
        sucesso = self.repository.Adicionar_na_Manutencao(id_aparelho, )
        
        if not sucesso:
            raise Exception("Não foi possível registrar o aparelho na manutenção.")
            
        return "Aparelho registrado na manutenção com sucesso!"
    
    def obter_quantidade_em_manutencao(self):
        return self.repository.retorna_Total()

    def liberar_aparelho_da_manutencao(self, id_aparelho):

        if not id_aparelho or int(id_aparelho) <= 0:
            raise ValueError("ID do aparelho inválido para operação.")
            
        sucesso = self.repository.Tirar_da_Manutencao(id_aparelho)
        
        if not sucesso:
            raise Exception(f"Não foi possível liberar o aparelho {id_aparelho}. Verifique se ele já foi liberado.")
            
        return "Aparelho liberado com sucesso e pronto para uso!"
    

manutencaoServe = ManutencaoService(ManutencaoRepo)