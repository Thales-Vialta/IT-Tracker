class ModeloAparelho:
    def ini (self, idModelo: int, marca: str, modelo: str):
        # Atributos padrão do modelo
        self._idModelo = idModelo
        self._marca = marca
        self._modelo = modelo

    # --- GETTERS PADRÃO ---

    @property
    def idModelo(self) -> int:
        return self._idModelo

    @property
    def marca(self) -> str:
        return self._marca

    @property
    def modelo(self) -> str:
        return self._modelo

    def mostra(self) -> str:
        """Retorna os atributos do modelo formatados em texto"""
        return f"ID: {self._idModelo} | Marca: {self._marca} | Modelo: {self._modelo}"