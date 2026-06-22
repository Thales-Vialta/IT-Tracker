from models.cargos import cargo
class usuario:
    def __init__(self,nomeUsuario:str, cargo: cargo):

        self.__idUsuario = None
        self.__nomeUsuario = nomeUsuario
        self.__idCargo = cargo

    
    @property
    def nome_usuario(self): 
        return self.__nomeUsuario
    @property
    def id_cargo(self): 
        return self.__idCargo.id_cargo
    def __str__(self):
        return f"Usuario [ID: {self.__idUsuario} | Nome: {self.__nomeUsuario} | ID Cargo: {self.__idCargo}]"
    

