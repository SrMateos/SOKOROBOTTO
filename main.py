from tablero import Tablero

def main():
    t = Tablero()
    t.cargarDatos("input/SOKOBOTTO1.txt")
    t.mostrarTablero()
    t.mostrarPosicionRobot()
    t.mostrarPosicionCajas()
    t.movIzquierda()
    t.mostrarPosicionRobot()
    
    
if __name__ == '__main__':
    main()