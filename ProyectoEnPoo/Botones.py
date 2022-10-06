from Ascensor import Ascensor
from Ascensor import Ascensor

class Botones(Ascensor):
    def __init__(self, posicion, imagen,direccion) -> None:
        super().__init__(posicion, imagen)
        self._direccion = direccion

    