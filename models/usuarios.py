class Usuario:
    def __init__(self,nomeUsuario:str, cargo: Cargo):

        self.__idUsuario = None
        self.__nomeUsuario = nomeUsuario
        self.__idCargo = cargo

    
    #essa func. serve pra quando der print em um obj ele imprimir os valores dos atributos e não o caminho do obj
    def __str__(self):
        return f"Usuario [ID: {self.__idUsuario} | Nome: {self.__nomeUsuario} | ID Cargo: {self.__idCargo}]"
    

