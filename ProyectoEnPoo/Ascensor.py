
from ObjetoEscenario import ObjetoEscenario

class Ascensor(ObjetoEscenario):
    def __init__(self, posicion, imagen,animacion,velocidad,PisoActual,PisoPedido) -> None:
        super().__init__(posicion, imagen)
        self.velocidad = velocidad
        self.animacion  = animacion
        self.PisoActual = PisoActual
        self.PisoPedido = PisoPedido
    
    def _subir(self):
        pass
    def _bajar(self):
        pass
    def __AbrirPuertas(self):
        pass
    def _CerrarPuertas(self):
        pass
