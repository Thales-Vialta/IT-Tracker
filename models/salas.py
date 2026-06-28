class Sala:
    def __init__(self, NomeSala: str, EnderecoSala: str):
        self.idSala = None
        self.NomeSala = NomeSala
        self.EnderecoSala = EnderecoSala

    def __str__(self):
        return f"Sala [ID: {self.idSala} | Nome: {self.NomeSala} | Endereço: {self.EnderecoSala}]"