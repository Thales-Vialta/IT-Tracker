from models.usuarios import Usuario
from repositories.usuariosRepository import UsuarioRepository
from repositories.cargoRepository import CargoRepository

class usuarioService:

    def __init__(self, usuario_repository, cargo_repository):
        # Os atalhos curtos são definidos aqui:
        self.usuario_repo = usuario_repository
        self.cargo_repo = cargo_repository

    def validarUsuario(self, nomeUsuario):
        if not self.usuario_repo.buscarUsuario(nomeUsuario):
            # Se buscar usuário e não encontrar, usuário foi validado e não existe
            print("Usuário não existe")
            return True
        else:
            # Se encontrar algo, usuário foi validado e existe
            print("Usuário existente")
            return False

    def cadastrarUsuario(self, nomeUsuario: str, cargo: str):
        validacao = self.validarUsuario(nomeUsuario)

        if not validacao:
            return "Usuário já cadastrado!"
        
        else:
            idCargo = self.cargo_repo.buscarCargoPorId(cargo) 
                      
            self.usuario_repo.inserir_usuario(nomeUsuario, idCargo)
            
            return "Usuário cadastrado com sucesso!"