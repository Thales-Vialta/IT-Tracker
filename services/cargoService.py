from repositories.cargoRepository import repoCar

class CargoService:

    def __init__(self, repo):
        self.cargo_repo = repo

    def capturarCargos(self):
        return self.cargo_repo.listarCargos()
    
    def buscarIdCargo(self,cargo:str):
        return self.cargo_repo.buscarIdCargo(cargo)
    

cargoService = CargoService(repoCar)
