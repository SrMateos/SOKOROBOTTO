def cargaDatos(fichero):
    #Abrimos el fichero
    f = open(fichero,'r')
    #Leemos el fichero entero, quitamos todos los saltos de línea, separamos por comas y quitamos espacio final
    l = f.read().replace('\n','').split(",")[0:-1]
    #Convertimos a matriz de enteros y devolvemos
    l = [[int(l[i*10+j]) for j in range(10) ]for i in range(10)]
    return l

def main():
    #Realizamos la carga de datos en una matriz m
    m = cargaDatos("input/SOKOBOTTO1.txt")

    #Mostrado de datos
    for i in range(10):
        for j in range(10):
            print(m[i][j], end=',')
        print()

if __name__ == '__main__':
    main()