class Sala:
    def __init__(self, idSala, NomeSala: str, EnderecoSala: str):
        self.idSala = idSala
        self.NomeSala = NomeSala
        self.EnderecoSala = EnderecoSala

    def __str__(self):
        return f"Sala [ID: {self.idSala} | Nome: {self.NomeSala} | Endereço: {self.EnderecoSala}]"