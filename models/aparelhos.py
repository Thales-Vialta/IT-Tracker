class Aparelhos:
    def __init__(self,serial:str,statusAparelho: str,idModelo:str):

        self.__idAparelho = None
        self.__serial = serial
        self.__statusAparelho = statusAparelho
        self.__idModelo = idModelo

    @property
    def serial(self): 
        return self.__serial
    @property
    def statusAparelho(self): 
            return self.__statusAparelho
    @property
    def idModelo(self): 
            return self.__idModelo
    
    #essa func. serve pra quando der print em um obj ele imprimir os valores dos atributos e não o caminho do obj
    def __str__(self):
        return f"Aparelho [ID: {self.__idAparelho} | Serial: {self.__serial} | Status: {self.__statusAparelho} | Modelo: {self.__idModelo}]"
    
class Notebook(Aparelhos):
    pass
