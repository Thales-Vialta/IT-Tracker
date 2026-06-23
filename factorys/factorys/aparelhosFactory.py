# Como deve ficar (Certo):
from models.aparelhos import Aparelhos, Notebook

class aparelhosfactory:
    @staticmethod
    def criar_aparelho(tipo:str,serial:str,idModelo:str):

        if tipo.lower().strip() == "notebook":
            return Notebook(serial=serial,statusAparelho="1",idModelo = idModelo)
        
        else:
            return Aparelhos(serial=serial,statusAparelho="1",idModelo = idModelo)
        #