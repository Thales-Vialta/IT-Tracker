from models.usuarios import Usuario
from repositories.usuariosRepository import UsuarioRepository
from services.cargoService import CargoService
class usuarioService:

    def __init__(self, usuario_repository, cargo_service):
        # Os atalhos curtos são definidos aqui:
        self.usuario_repo = usuario_repository
        self.cargo_service = cargo_service

    def validarUsuario(self, nomeUsuario):
        if not self.usuario_repo.buscarUsuario(nomeUsuario):
            # Se buscar usuário e não encontrar, usuário foi validado e não existe
            print('User não existe')
            return True
        else:
            # Se encontrar algo, usuário foi validado e existe
            print('user existe')
            return False

    def cadastrarUsuario(self, nomeUsuario: str, cargo: str):
        print('Entrou no cadastro')
        validacao = self.validarUsuario(nomeUsuario)
        print(f'puxou validação {validacao}')

        if not validacao:
            print('entrou no if')
            return "Usuário já cadastrado!"
        
        else:
            print('entrou no else')
            idCargo = self.cargo_service.capturarIdCargo(cargo) 
                      
            self.usuario_repo.inserir_usuario(nomeUsuario, idCargo)
            
            return "Usuário cadastrado com sucesso!"
        
    def capturaUsuarios(self): # não deveria ser listarUsuarios pelo diagrama?
        return self.usuario_repo.listarUsuarios()
    
    def buscaUsuario(self,nome):

        usuario = " ".join(nome.split()).title()

        return self.usuario_repo.buscarUsuario(usuario)
    
    def atualizaUsuario(self,nomeUsuario,atributo:str,valor:str):

        validacao = self.validarUsuario(nomeUsuario)

        if validacao:
            return "Usuário não encontrado!"

        else:
            self.usuario_repo.editarUsuario(nomeUsuario,atributo,valor)
            return "Usuário atualizado!"    

    def removerUsuario(self,nomeUsuario):
        validacao = self.validarUsuario(nomeUsuario)

        if validacao:
            return "Usuário não encontrado!"
        else:
            self.usuario_repo.removerUsuario(nomeUsuario)
            return "Usuário removido com sucesso!"
        

        
