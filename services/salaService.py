from models.salas import Sala
from repositories.salaRepository import salaRepository

class salaService:

    def __init__(self, sala_repository):
        self.sala_repo = sala_repository

    def listarSalas(self):
        return self.sala_repo.listarSalas()

    def buscarSalas(self, nome: str):
        return self.sala_repo.buscarSala(nome)

    def existeSala(self, NomeSala: str):
        if not self.buscarSalas(NomeSala):
            #sala não existe e pode cadastrar uma nova
            
            return True
        else:
            #sala existe e não pode cadastrar uma nova
            return False

    def cadastrarSalas(self, NomeSala: str, EnderecoSala: str):
            validacao = self.existeSala(NomeSala)
            if not validacao:
                return "Sala já cadastrada!"
            else:
                nova_sala = Sala(NomeSala, EnderecoSala)
                
                nome_puro = nova_sala.NomeSala
                endereco_puro = nova_sala.EnderecoSala
                
                self.sala_repo.Inserir_Sala(nome_puro, endereco_puro)
                
                return "tentando cadastrar sala"

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