from repositories.cargoRepository import CargoRepository

class CargoService:

    def __init__(self, cargo_repository):
        self.cargo_repo = cargo_repository

    def capturarCargos(self):
        print('entrou em capturar cargos')
        return self.cargo_repo.listarCargos()
    
    def buscarIdCargo(self,cargo:str):
        return self.cargo_repo.buscarIdCargo(cargo)