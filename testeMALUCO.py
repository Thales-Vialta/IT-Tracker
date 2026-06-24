from services.cargoService import CargoService
from repositories.cargoRepository import CargoRepository
from repositories.usuariosRepository import UsuarioRepository
from services.userService import usuarioService
from services.horarioService import horarioService
from repositories.horarioRepository import HorarioRepository
from repositories.salaRepository import salaRepository
from services.salaService import salaService



repo_Sala = salaRepository()
servSala = salaService(repo_Sala)

'''print(servSala.listarSalas(),'\n')

print(servSala.buscarSalas('Auditório Principal'),'\n')

print(servSala.existeSala('Sala dos mano'),'\n')

print(servSala.cadastrarSalas(100,'Sala dos mano', 'A113 | Bloco B | 2°Andar'),'\n')

print(servSala.editarSalas('Sala das Mana','EnderecoSala','A67'),'\n')

print(servSala.removerSalas('Sala das Mana'),'\n')'''
'''repo_Cargo = CargoRepository()
servCargo = CargoService(repo_Cargo)
repo_Horario = HorarioRepository()
servHora = horarioService(repo_Horario)'''



'''repo_Usuario = UsuarioRepository()
serv_Usuario = usuarioService(repo_Usuario,servCargo)'''

'''servHora.listarHorarios()'''

"""cargoAleatorio = 'Professor'"""

'''userCap = serv_Usuario.capturaUsuarios()
print(userCap)'''

#search_user = serv_Usuario.buscaUsuario('João de Oliveira Stekel')
#print(search_user)

'''Validar = serv_Usuario.validarUsuario('João de Oliveira Stekel')
print(Validar)'''

'''atualizar = serv_Usuario.atualizaUsuario('Joana de Oliveira Stekel','ID_Cargo','2')
print(atualizar)'''

"""eliminar_joao = serv_Usuario.removerUsuario('João')
print(eliminar_joao)"""


"""
cargos = serv.capturarCargos()
print(cargos)"""

"""idCargo = serv.capturarIdCargo(cargoAleatorio)
print(idCargo)


for id_usuario, nome in repo_Usuario.Usuario_Nunca_Alocou():
    print(f"{id_usuario} - {nome}")

serv_Usuario = usuarioService(repo_Usuario,serv)
print('Teste começa aqui')
print(serv_Usuario.cadastrarUsuario('João', 'Professor'))
"""

























