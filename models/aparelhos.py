class Aparelhos:

    def __init__(self,serial:str,statusAparelho: str,idModelo:str):
        self.__idAparelho = None
        self.__serial = serial
        self.__statusAparelho = statusAparelho
        self.__idModelo = idModelo

    def __str__(self):
        return f"Aparelho [ID: {self.__idAparelho} | Serial: {self.__serial} | Status: {self.__statusAparelho} | Modelo: {self.__idModelo}]"

    def getIdAparelho(self):
        return self.__idAparelho
    def getSerial(self):
        return self.__serial
    def getStatus(self):
        return self.__statusAparelho
    def getIdModelo(self):
        return self.__idModelo

    def setIdAparelho(self, new_data):
        self.__idAparelho = new_data
    def setSerial(self, new_data):
        self.__serial = new_data
    def setStatus(self, new_data):
        self.__statusAparelho = new_data
    def setIdModelo(self, new_data):
        self.__idModelo = new_data


class Notebook(Aparelhos):
    pass