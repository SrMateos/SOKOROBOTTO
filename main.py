#!/usr/bin/env python3

from tablero import Tablero

def main():
    t = Tablero()
    t.cargarDatos("input/SOKOBOTTO1.txt")
    t.mostrarTablero()
    print()
    while(True):
        n = str(input("Introduce una eleccion\n"))
        if n == "s":
            break
        else:
            eleccion(t,n)

def eleccion(t,n):
    if n == "i":
        t.movIzquierda()
    elif n == "d":
        t.movDerecha()
    elif n == "a":
        t.movArriba()    
    elif n == "b":
        t.movAbajo()
    
    t.mostrarTablero()
    print()

if __name__ == '__main__':
    main()


'''    
    t.mostrarTablero()
    t.movAbajo()
    print()
    t.mostrarTablero()
    
    t.movAbajo()
    print()
    t.mostrarTablero()
'''