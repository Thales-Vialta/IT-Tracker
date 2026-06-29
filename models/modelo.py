class Modelo:
    def __init__(self, marca: str, modelo: str):
        self._idModelo = None  
        self.marca = marca     
        self.modelo = modelo   

    @property
    def idModelo(self):
        return self._idModelo
    
    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    def __str__(self):
        return f"ModeloAparelho [ID: {self.idModelo} | Marca: {self.marca} | Modelo: {self.modelo}]"
    
