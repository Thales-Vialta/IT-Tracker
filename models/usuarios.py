from models.cargos import cargo
class Usuario:
    def __init__(self,nomeUsuario:str, cargo: cargo):

        self.__idUsuario = None
        self.__nomeUsuario = nomeUsuario
        self.__idCargo = cargo
    def __str__(self):
        return f"Usuario [ID: {self.__idUsuario} | Nome: {self.__nomeUsuario} | ID Cargo: {self.__idCargo}]"
    

