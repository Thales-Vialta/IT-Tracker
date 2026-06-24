from services.cargoService import CargoService
from repositories.cargoRepository import CargoRepository
from repositories.usuariosRepository import UsuarioRepository

repo_Cargo = CargoRepository()
serv = CargoService(repo_Cargo)
cargos = serv.capturarCargos()

print(cargos)

cargoAleatorio = 'Professor'

idCargo = serv.capturarIdCargo(cargoAleatorio)
print(idCargo)

repo = UsuarioRepository()
for id_usuario, nome in repo.Usuario_Nunca_Alocou():
    print(f"{id_usuario} - {nome}")