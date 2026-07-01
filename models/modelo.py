class ModeloAparelho:
    def __init__(self, idMarca: int, modelo: str):
        # Atributos padrão do modelo

        self._idMarca = idMarca
        self._modelo = modelo

    @property
    def idMarca(self) -> str:
        return self._idMarca

    @property
    def modelo(self) -> str:
        return self._modelo

    
