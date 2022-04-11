#!/usr/bin/env python3

from algoritmos import Algoritmos
from tablero import Tablero
from estado import Estado
import os
from time import time
from time import sleep

def cargarMatriz(fichero):
    # Abrimos el fichero
    f = open(fichero,'r')
    
    # Leemos el fichero entero, quitamos todos los saltos de línea, separamos por comas y quitamos espacio final
    l = f.read().replace('\n','').split(",")[0:-1]
    
    # Convertimos a __matriz de enteros y devolvemos
    matriz = [[int(l[i*10+j]) for j in range(10) ] for i in range(10)]
    return matriz

def cargarEstado(matriz):
    robot = None
    cajas = []
    objetivoCajas = []
    
    for i in range(10):
        for j in range(10):
            if matriz[i][j] !=0 and matriz[i][j] !=1:
                # Comprobamos caja
                if matriz[i][j] == 2:
                    cajas.append([i,j])
                    matriz[i][j] = 0
                # Comprobamos objetivo
                elif matriz[i][j] == 3:
                    objetivoCajas.append([i,j])
                # Comprobamos robot
                else:
                    robot = [i,j]
                    matriz[i][j] = 0

    Estado.setTablero(Tablero(matriz,objetivoCajas))
    return Estado(robot, cajas, 0, None, "", 3)

if __name__ == '__main__':
    estadoInicial = cargarEstado(cargarMatriz("input/SOKOBOTTO1.txt"))
    
    algoritmos = Algoritmos()
    # algoritmos.funcionAEstrella(estadoInicial)
    
    ganar=1
    intentos=0
    while ganar == 1 and intentos<1000000:
        ganar = algoritmos.maximaPendienteRandom(estadoInicial)
        intentos += 1
    print (intentos)
