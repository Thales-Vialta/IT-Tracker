from models.salas import Sala
from repositories.salaRepository import salaRepository

class salaService:

    def __init__(self, sala_repository):
        self.sala_repo = sala_repository

    def listarSalas(self):
        return self.sala_repo.listarSalas()

    def buscarSalas(self, nome: str):
        sala = " ".join(nome.split()).title()
        return self.sala_repo.buscarSala(sala)

    def existeSala(self, NomeSala: str):
        if not self.buscarSalas(NomeSala):
            return True
        else:
            return False

    def cadastrarSalas(self, NomeSala: str, EnderecoSala: str):
        validacao = self.existeSala(NomeSala)
        if not validacao:
            return "Sala já cadastrada!"
        else:
            nova_sala = Sala(NomeSala, EnderecoSala)
            self.sala_repo.Inserir_Horario(nova_sala)
            return "Sala cadastrada com sucesso!"

    def removerSalas(self, NomeSala: str):
        validacao = self.existeSala(NomeSala)
        if validacao:
            return "Sala não encontrada!"
        else:
            self.sala_repo.removerSala(NomeSala)
            return "Sala removida com sucesso!"

    def editarSalas(self, NomeSala: str, atributo: str, valor: str):
        validacao = self.existeSala(NomeSala)
        if validacao:
            return "Sala não encontrada!"
        else:
            self.sala_repo.editarSala(NomeSala, atributo, valor)
            return "Sala updated!"