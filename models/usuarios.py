from models.cargos import Cargo
class Usuario:
    def __init__(self,nomeUsuario:str, Cargo:Cargo):

        self.__idUsuario = None
        self.__nomeUsuario = nomeUsuario
        self.__idCargo = Cargo.__idCargo
    def __str__(self):
        return f"Usuario [ID: {self.__idUsuario} | Nome: {self.__nomeUsuario} | ID Cargo: {self.__idCargo}]"
    

