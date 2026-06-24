from services.cargoService import CargoService
from repositories.cargoRepository import CargoRepository


repo = CargoRepository()
serv = CargoService(repo)
cargos = serv.capturarCargos()

print(cargos)

cargoAleatorio = 'Professor'

idCargo = serv.capturarIdCargo(cargoAleatorio)
print(idCargo)
