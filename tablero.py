class Tablero:
    def __init__(self):
        #Matriz tablero
        self.matriz = [[]]
        #Posicion robot
        self.robot  = []
        #posiciones cajas
        self.cajas  = [[]]

    def cargarDatos(self, fichero):
        #Abrimos el fichero
        f = open(fichero,'r')
        #Leemos el fichero entero, quitamos todos los saltos de línea, separamos por comas y quitamos espacio final
        l = f.read().replace('\n','').split(",")[0:-1]
        #Convertimos a matriz de enteros y devolvemos
        self.matriz = [[int(l[i*10+j]) for j in range(10) ]for i in range(10)]

    def mostrarTablero(self):
        #Mostrado de datos
        for i in range(10):
            for j in range(10):
                print(self.matriz[i][j], end=' ')
            print()