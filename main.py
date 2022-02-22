from tablero import Tablero

def main():
    t = Tablero()
    t.cargarDatos("input/SOKOBOTTO1.txt")
    
    t.mostrarTablero()
    t.movAbajo()
    print()
    t.mostrarTablero()
    
    t.movAbajo()
    print()
    t.mostrarTablero()
    
    t.movAbajo()
    print()
    t.mostrarTablero()
    
    t.movAbajo()
    print()
    t.mostrarTablero()
    
    t.movDerecha()
    print()
    t.mostrarTablero()
    
    t.movAbajo()
    print()
    t.mostrarTablero()




if __name__ == '__main__':
    main()