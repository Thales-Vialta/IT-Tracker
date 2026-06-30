from datetime import datetime
from typing import List

class Alocacao:
    def __init__(self, idUsuario: int, idSala: int, id_Aparelho: List[int], dataAlocacao: datetime, dataDevolucao: datetime):
        self._idAlocacao = None          
        self._idUsuario = idUsuario      
        self._idSala = idSala            
        self._id_Aparelho = id_Aparelho  
        self._dataAlocacao = dataAlocacao
        self._dataDevolucao = dataDevolucao 


    @property
    def idAlocacao(self):
        return self._idAlocacao

    @property
    def idUsuario(self):
        return self._idUsuario

    @property
    def idSala(self):
        return self._idSala

    @property
    def id_Aparelho(self) -> List[int]:
        """Retorna a lista de IDs dos aparelhos alocados"""
        return self._id_Aparelho

    @property
    def dataAlocacao(self):
        return self._dataAlocacao

    @property
    def dataDevolucao(self):
        return self._dataDevolucao