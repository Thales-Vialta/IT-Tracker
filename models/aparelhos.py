class Aparelhos:
    def __init__(self, serial: str, statusAparelho:int, idModelo: int):

        self._serial = serial
        self._statusAparelho = 1
        self._idModelo = idModelo

    @property
    def serial(self) -> int:
        return self._serial

    @property
    def statusAparelho(self) -> bool:
        return self._statusAparelho

    @property
    def idModelo(self) -> int:
        return self._idModelo

    # --- FUNÇÃO DE EXIBIÇÃO COM NOME NORMAL ---

    def mostra(self) -> str:
        """Retorna os atributos do aparelho formatados em texto"""
        status_texto = "Ativo" if self._statusAparelho else "Inativo"
        return f"ID Aparelho: {self._idAparelho} | Serial: {self._serial} | Status: {status_texto} | ID Modelo: {self._idModelo}"
    
