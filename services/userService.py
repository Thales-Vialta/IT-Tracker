from repositories.usuariosRepository import listarUsuarios, buscarUsuario
class usuarioService:

    def validarUsuario(nomeUsuario):
        if buscarUsuario(nomeUsuario) == False:
            # Se buscar usuário e não encontrar, usuário foi valdiado e não existe

            return False
        
        else:
            # se encontrar algo, usuário foi válidado e existe
            return True

        pass


   