from repositories.cargoRepository import CargoRepository

class CargoService:
    def __init__(self, cargo_repository):
        # Os atalhos curtos são definidos aqui:
        self.cargo_repo = cargo_repository

    def capturarCargos(self):
        print('entrou em capturar cargos')
        return self.cargo_repo.listarCargos()
    
    def capturarIdCargo(self,cargo:str):
        return self.cargo_repo.buscarIdCargo(cargo)


        
    