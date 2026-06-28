from models.salas import Sala
from repositories.salaRepository import salaRepo

from  views.limparTela import limpar_tela
from views.cores import CORES

class salaService:

    def __init__(self, sala_repository):
        self.sala_repo = sala_repository

    def listarSalas(self):
        limpar_tela()
        salas = self.sala_repo.listarSalas()
        resultado = f"{CORES['AZUL']}{CORES['NEGRITO']}---- LISTA DE SALAS ----\n\n{CORES['RESET']}"

        for sala in salas:
            nome_sala = sala[0]
            endereco = sala[1]

            nome_format = nome_sala.ljust(30)
            resultado += f"{CORES['NEGRITO']}{CORES['AMARELO']}{nome_format} |{CORES['RESET']} {CORES['RESET']} {endereco}\n"
        
        return resultado

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
            self.sala_repo.Inserir_Sala(nova_sala)
            return "tentando cadastrar sala"

    def removerSalas(self, NomeSala: str):
        validacao = self.existeSala(NomeSala)
        if validacao:
            return "Sala não encontrada!"
        else:
            status = self.sala_repo.removerSala(NomeSala)
            if status == "vinculada":
                return("não pode ser removida, pois existem reservas para ela!")
            return "Sala removida com sucesso!"

    def editarSalas(self, NomeSala: str, atributo: str, valor: str):
        validacao = self.existeSala(NomeSala)
        if validacao:
            return "Sala não encontrada!"
        else:
            self.sala_repo.editarSala(NomeSala, atributo, valor)
            return "Sala updated!"

salaService = salaService(salaRepo)