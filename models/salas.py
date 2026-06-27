class Sala:
    def __init__(self, NomeSala: str, EnderecoSala: str):
        self.__idSala = None
        self.__NomeSala = NomeSala
        self.__EnderecoSala = EnderecoSala

    def __str__(self):
        return f"Sala [ID: {self.__idSala} | Nome: {self.__NomeSala} | Endereço: {self.__EnderecoSala}]"


    @property
    def idSala(self):
        return self.__idSala

    @property
    def NomeSala(self):
        return self.__NomeSala

    @property
    def EnderecoSala(self):
        return self.__EnderecoSala