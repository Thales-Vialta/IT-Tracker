class Usuario:
    def __init__(self, nomeUsuario: str, cargo: int):
        self.__idUsuario = None
        self.__nomeUsuario = nomeUsuario
        self.__idCargo = cargo  # Corrigido aqui para receber o valor do parâmetro 'cargo'

    def __str__(self):
        return f"Usuario [ID: {self.__idUsuario} | Nome: {self.__nomeUsuario} | ID Cargo: {self.__idCargo}]"

    # --- PROPERTIES (GETTERS) ---

    @property
    def idUsuario(self):
        return self.__idUsuario

    @property
    def nomeUsuario(self):
        return self.__nomeUsuario

    @property
    def idCargo(self):
        return self.__idCargo