class Tablero:
    def __init__(self):
        #Matriz tablero
        self.__matriz = [[]]
        #Posicion robot
        self.__robot  = None
        #Posiciones cajas
        self.__cajas  = []
        #Posiciones objetivo cajas
        self.__objetivoCajas = []

    def cargarDatos(self, fichero):
        #Abrimos el fichero
        f = open(fichero,'r')
        #Leemos el fichero entero, quitamos todos los saltos de línea, separamos por comas y quitamos espacio final
        l = f.read().replace('\n','').split(",")[0:-1]
        #Convertimos a __matriz de enteros y devolvemos
        self.__matriz = [[int(l[i*10+j]) for j in range(10) ] for i in range(10)]
        #Guardamos 
        self.__posicionJugadorCajas()
  
    #0-celda vacia 1-muro 2-caja 3-objetivo 4-robot
    def __posicionJugadorCajas(self):
        for i in range(10):
            for j in range(10):
                if self.__matriz[i][j] !=0 and self.__matriz[i][j] !=1:
                    if self.__matriz[i][j] == 2:
                        self.__cajas.append([i,j])
                    elif self.__matriz[i][j] == 3:
                        self.__objetivoCajas.append([i,j])
                    elif self.__matriz[i][j] == 4:
                        self.__robot = [i,j]
                    
    def mostrarTablero(self):
        #Mostrado de datos
        for i in range(10):
            for j in range(10):
                print(self.__matriz[i][j], end=' ')
            print()

    def mostrarPosicionRobot(self):
        print(self.__robot)

    def mostrarPosicionCajas(self):
        print(self.__cajas)

    def mostrarPosicionObjetivo(self):
        print(self.__objetivoCajas)

    def __comprobarMovimientoVacio(self,x,y):
        return self.__matriz[x][y] == 0 or self.__matriz[x][y] == 3
        
    def movIzquierda(self):
        if self.__comprobarMovimientoVacio(self.__robot[0],self.__robot[1]-1):
            self.__robot[1] -= 1

            self.__matriz
        elif self.__matriz[ self.__robot[0] ][ self.__robot[1]-1 ] == 2
        
    def movDerecha(self):
        if self.__comprobarMovimientoVacio(self.__robot[0],self.__robot[1]+1):
            self.__robot[1] += 1

        elif if self.__matriz[self.__robot[0]][self._robot[1] + 1] == 2
    
    def movArriba(self):
        if self.__comprobarMovimientoVacio(self.__robot[0]-1,self.__robot[1]):
            self.__robot[0] -= 1
    
    def movAbajo(self):
        if self.__comprobarMovimientoVacio(self.__robot[0]+1,self.__robot[1]):
            self.__robot[0] += 1

    def cambioPosicion(self):

