class Cargo:
    def __init__(self,nomeCargo:str):

        self.__idCargo = None
        self.__nomeCargo = nomeCargo
        self.__idCargo = None

    
    #essa func. serve pra quando der print em um obj ele imprimir os valores dos atributos e não o caminho do obj
    def __str__(self):
        return f"Cargo [ID: {self.__idCargo} | Nome: {self.__nomeCargo}]"
    

