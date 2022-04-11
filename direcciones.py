from enum import Enum

class direccion(Enum):
    ARRIBA    = (-1,0)
    ABAJO     = (1,0)
    IZQUIERDA = (0,-1)
    DERECHA   = (0,1)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getCoordenadas(self):
        return [self.x, self.y]

    def letraADireccion(letra):
        if letra == "A":
            return direccion.ARRIBA
        elif letra == "B":
            return direccion.ABAJO
        elif letra == "I":
            return direccion.IZQUIERDA
        elif letra == "D":
            return direccion.DERECHA
        else:
            return None


