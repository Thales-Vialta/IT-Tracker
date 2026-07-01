class Marca():
    def __init__(self,marca:str):
        
        self._marca = marca

    @property
    def marca(self) -> str:
        return self.marca