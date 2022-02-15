from tablero import Tablero

def main():
    t = Tablero()
    t.cargarDatos("input/SOKOBOTTO1.txt")
    t.mostrarTablero()

if __name__ == '__main__':
    main()