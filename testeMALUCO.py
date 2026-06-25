from services.cargoService import CargoService
from repositories.cargoRepository import CargoRepository
from repositories.usuariosRepository import UsuarioRepository
from services.userService import usuarioService
from services.horarioService import horarioService
from repositories.horarioRepository import HorarioRepository
from repositories.salaRepository import salaRepository
from services.salaService import salaService
from repositories.alocacaoRepository import AlocacaoRepository

# INSTANCIAÇÃO DE CLASSES
repo_Cargo = CargoRepository()
servCargo = CargoService(repo_Cargo)
repo_Horario = HorarioRepository()
servHora = horarioService(repo_Horario)
repo_Sala = salaRepository()
servSala = salaService(repo_Sala)
repo_Usuario = UsuarioRepository()
serv_Usuario = usuarioService(repo_Usuario,servCargo)
repo_Aloc = AlocacaoRepository()
# TESTE CARGOS
print('TESTE CARGOS')
cargoAleatorio = 'Professor'

cargos = servCargo.capturarCargos()
print(cargos)

idCargo = servCargo.buscarIdCargo(cargoAleatorio)
print(idCargo)
print()
print()
print()
print()
print()

# TESTE USUÁRIOS
print('TESTE USUARIOS')
serv_Usuario = usuarioService(repo_Usuario,servCargo)

userCap = serv_Usuario.listarUsuarios() 
print(userCap)

print(serv_Usuario.cadastrarUsuario('João', 'Professor')) 
print()
print()
search_user = serv_Usuario.buscaUsuario('Helena Pera') 
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

print(servSala.cadastrarSalas('Sala dos pessoalzinho do ti', 'A113 | Bloco B | 2°Andar'),'\n')

print(servSala.editarSalas('Sala das Mana','EnderecoSala','A67'),'\n')

print(servSala.removerSalas('Sala das Mana'),'\n')

print()
print()
print()


# TESTE HORÁRIOS
print('TESTE HORARIOS')

hora = servHora.listarHorarios()
print(hora)

#TESTE ALOCAÇÃO

print(repo_Aloc.inserir_Alocacao(1,3,10,'2026-07-01','2026-07-02'))

print(repo_Aloc.Aparelhos_menos_Alocados())

print(repo_Aloc.Editar_Alocacao(15,21,100,'2026-07-04','2026-07-06',16))

print(repo_Aloc.Deletar_Alocacao(17))



