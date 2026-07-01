class Salas:
    def __init__(self, nomeSala: str, enderecoSala: str):
        # Atributos padrão do modelo (definidos na criação)

        self._nomeSala = nomeSala
        self._enderecoSala = enderecoSala

    # --- GETTERS PADRÃO ---

    @property
    def nomeSala(self) -> str:
        return self._nomeSala

    @property
    def enderecoSala(self) -> str:
        return self._enderecoSala

