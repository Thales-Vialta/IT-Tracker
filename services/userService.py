from views.limparTela import limpar_tela
from views.cores import CORES

from models.usuarios import Usuario
from repositories.usuariosRepository import userRepo
from services.cargoService import cargoService

class usuarioService:

    def __init__(self, usuario_repository, cargo_service):
        self.usuario_repo = usuario_repository
        self.cargo_service = cargo_service

    def validarUsuario(self, nomeUsuario):
        if not self.usuario_repo.buscarUsuario(nomeUsuario):
            # Se buscar usuário e não encontrar, usuário foi validado e não existe
            return True
        else:
            # Se encontrar algo, usuário foi validado e existe
            return False

    def cadastrarUsuario(self, nomeUsuario: str, cargo: str):
        validacao = self.validarUsuario(nomeUsuario)

        if not validacao:
            return " já cadastrado!"
        else:
            idCargo = self.cargo_service.buscarIdCargo(cargo) 
            self.usuario_repo.inserir_usuario(nomeUsuario, idCargo)
            return " cadastrado com sucesso!"
        
    def listarUsuarios(self):
        limpar_tela()
        usuarios = self.usuario_repo.listarUsuarios()
        resultado = (f"{CORES['AZUL']}{CORES['NEGRITO']}========== LISTA DE USUÁRIOS ==========\n\n{CORES['RESET']}")
        numero = 0
    
        for usuario in usuarios:
            numero += 1
            nome = usuario[0]
            resultado += f"{CORES['AMARELO']}{CORES['NEGRITO']}{numero}.{CORES['RESET']} {nome}\n"
            
        return resultado
    
    def buscaUsuario(self,nome):
        usuario = " ".join(nome.split()).title()
        return self.usuario_repo.buscarUsuario(usuario)
    
    def atualizaUsuario(self,nomeUsuario,atributo:str,valor:str):

        validacao = self.validarUsuario(nomeUsuario)

        if validacao:
            return "Usuário não encontrado!"
        else:
            if atributo == 'Cargo':
                atributo = 'ID_Cargo'
                valor = self.cargo_service.buscarIdCargo(valor)

                self.usuario_repo.editarUsuario(nomeUsuario,atributo,valor)
                return " atualizado!"    
            
            else:
                self.usuario_repo.editarUsuario(nomeUsuario,atributo,valor)
                return " atualizado!"                  

    def removerUsuario(self,nomeUsuario):
        validacao = self.validarUsuario(nomeUsuario)

        if validacao:
            return " não encontrado!"
        else:
            self.usuario_repo.removerUsuario(nomeUsuario)
            return "removido com sucesso!"
        
userService = usuarioService(userRepo, cargoService)
