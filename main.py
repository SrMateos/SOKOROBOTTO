#!/usr/bin/env python3

from tablero import Tablero
import os
from time import time
from time import sleep

def main():
    startTime = time()
    t = Tablero()
    t.cargarDatos("input/SOKOBOTTO1.txt")
    t.mostrarTablero()
    print()
    while(not t.ganar()):
        os.system("clear")
        t.mostrarTablero()
        print()
        t.mostrarPosicionCajas()
        print()
        n = str(input("Introduce una eleccion\n"))
        if n == "s":
            break
        else:
            eleccion(t,n)
            
    elapsed_time = time() - startTime
    print(f'El tiempo es: {1}',elapsed_time) 
    print()

def eleccion(t,n):
    if n == "I":
        t.movIzquierda(False)
    elif n == "D":
        t.movDerecha(False)
    elif n == "A":
        t.movArriba(False)    
    elif n == "B":
        t.movAbajo(False)
    elif n == "EI":
        t.movIzquierda(True)
    elif n == "ED":
        t.movDerecha(True)
    elif n == "EA":
        t.movArriba(True)    
    elif n == "EB":
        t.movAbajo(True)
    elif n == "ID" :
        t.intercambioDerecha()
    elif n == "IA" :
        t.intercambioArriba()
    elif n == "II" :
        t.intercambioIzquierda()
    elif n == "IB" :
        t.intercambioAbajo()

def test():
    t = Tablero()
    t.cargarDatos("input/SOKOBOTTO1.txt")
    t.mostrarTablero()
    l = ['B','B','B','D','EB','A','I','I','B','B','D','ED','I','I','I','A','A','A','I','I','I','A','A','IA','EB','EB','EB','D','B','II','ED','A','D','EB']
    startTime = time()
    for i in l:
        #os.system("clear")
        #t.mostrarTablero()
        #print()
        eleccion(t,i)
        #sleep(1)

    elapsed_time = time() - startTime
    print()
    t.mostrarTablero()
    print()
    print(f'El tiempo es: {1}',elapsed_time)    

if __name__ == '__main__':
    main()