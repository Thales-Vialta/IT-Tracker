from repositories.cargoRepository import CargoRepository

class CargoService:

    def __init__(self, cargo_repository):
        self.cargo_repo = cargo_repository

    def capturarCargos(self):
        return self.cargo_repo.listarCargos()
    
    def capturarIdCargo(self,cargo:str):
        return self.cargo_repo.buscarIdCargo(cargo)