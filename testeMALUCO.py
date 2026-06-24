from services.cargoService import CargoService
from repositories.cargoRepository import CargoRepository
from repositories.usuariosRepository import UsuarioRepository
from services.userService import usuarioService
from services.horarioService import horarioService
from repositories.horarioRepository import HorarioRepository
from repositories.salaRepository import salaRepository
from services.salaService import salaService


# INSTANCIAÇÃO DE CLASSES
repo_Cargo = CargoRepository()
servCargo = CargoService(repo_Cargo)
repo_Horario = HorarioRepository()
servHora = horarioService(repo_Horario)
repo_Sala = salaRepository()
servSala = salaService(repo_Sala)
repo_Usuario = UsuarioRepository()
serv_Usuario = usuarioService(repo_Usuario,servCargo)

# TESTE CARGOS
"""print('TESTE CARGOS')
cargoAleatorio = 'Professor'

cargos = servCargo.capturarCargos()
print(cargos)

idCargo = servCargo.buscarIdCargo(cargoAleatorio)
print(idCargo)
print()
print()
print()
print()
print()"""

# TESTE USUÁRIOS
print('TESTE USUARIOS')
serv_Usuario = usuarioService(repo_Usuario,servCargo)

userCap = serv_Usuario.listarUsuarios() 
print(userCap)

"""print(serv_Usuario.cadastrarUsuario('João', 'Professor')) 
print()
print()
search_user = serv_Usuario.buscaUsuario('Joana de Oliveira Stekel') #retornou lista vazia
print(search_user)
print()
print()

Validar = serv_Usuario.validarUsuario('João de Oliveira Stekel')
print(Validar)
print()
print()

atualizar = serv_Usuario.atualizaUsuario('Joana de Oliveira Stekel','Cargo','Professor')
print(atualizar)
print()
print()

eliminar_joao = serv_Usuario.removerUsuario('João')
print(eliminar_joao)
print()
print()
print()
print()
print()

# TESTE SALAS
print('TESTE SALAS')

print(servSala.listarSalas(),'\n')

print(servSala.buscarSalas('Auditório Principal'),'\n')

print(servSala.existeSala('Sala dos mano'),'\n')

print(servSala.cadastrarSalas(100,'Sala dos mano', 'A113 | Bloco B | 2°Andar'),'\n')

print(servSala.editarSalas('Sala das Mana','EnderecoSala','A67'),'\n')

print(servSala.removerSalas('Sala das Mana'),'\n')

print()
print()
print()


# TESTE HORÁRIOS
print('TESTE HORARIOS')

hora = servHora.listarHorarios()
print(hora)"""









