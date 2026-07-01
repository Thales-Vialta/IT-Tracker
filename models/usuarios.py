class Usuario:
    def __init__(self,nomeUsuario: str, idCargo: int):

        self._nomeUsuario = nomeUsuario
        self._idCargo = idCargo

    @property
    def nomeUsuario(self) -> str:
        return self._nomeUsuario

    @property
    def idCargo(self) -> int:
        return self._idCargo

    
