#!/usr/bin/env python3

from algoritmos import Algoritmos
from tablero import Tablero
from estado import Estado
from time import time

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

def seleccionarInput():
    print("Seleccione el fichero de entrada:")
    for i in range(1,11):
        print(f"{i}. SOKOBOTTO{i}.txt")
    
    numeroFichero = input("Introduzca el número: ")
    return "input/SOKOBOTTO" + numeroFichero + ".txt"

if __name__ == '__main__':

    estadoInicial = cargarEstado(cargarMatriz(seleccionarInput()))
    
    algoritmos = Algoritmos()
    print("Elige un algoritmo: ")
    print("1.- A*")
    print("2.- Primero mejor")
    print("3.- Máxima pendiente")
    print("4.- Máxima pendiente random")
    alg = int(input("(Introduce un número del 1 al 4): "))
    funcion = None
    if alg == 1:
        funcion = algoritmos.funcionAEstrella
    elif alg == 2:
        funcion = algoritmos.primeroMejor
    elif alg == 3:
        funcion = algoritmos.maximaPendiente
    elif alg == 4:
        funcion = algoritmos.maximaPendienteRandom
    
    start = time()
    funcion(estadoInicial)
    print(f"Tiempo: {time()-start} segundos")
