class Cargo: 
        def __init__(self,Descricao_cargo:str):
        
                self.__idCargo = None
                self.__Descricao_cargo = ""

        def __str__(self):
                 return f"ID_Cargo: {self.__idCargo} | Cargo: {self.__Descricao_cargo}"
