class Aparelhos:

    def __init__(self,serial:str,statusAparelho: str,idModelo:str):
        self.__idAparelho = None
        self.__serial = serial
        self.__statusAparelho = statusAparelho
        self.__idModelo = idModelo

    def __str__(self):
        return f"Aparelho [ID: {self.__idAparelho} | Serial: {self.__serial} | Status: {self.__statusAparelho} | Modelo: {self.__idModelo}]"

class Notebook(Aparelhos):
    pass
