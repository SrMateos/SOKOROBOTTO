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
                if self.__matriz[i][j] != 0:
                    print(self.__matriz[i][j], end=' ')
                else:
                    print(".", end=' ')
            print()

    def mostrarPosicionRobot(self):
        print(self.__robot)

    def mostrarPosicionCajas(self):
        print(self.__cajas)

    def mostrarPosicionObjetivo(self):
        print(self.__objetivoCajas)

    def __comprobarMovimientoVacio(self,x,y):
        return self.__matriz[x][y] == 0 or self.__matriz[x][y] == 3
    
    #0-celda vacia 1-muro 2-caja 3-objetivo 4-robot
    def __actualizarMatriz(self,x,y,movimientoCaja):
        #Actualizar cajas
        self.__matriz[self.__robot[0]][self.__robot[1]] = 4
        if movimientoCaja:
            self.__matriz[self.__robot[0] + x][self.__robot[1] + y] = 2

        x0 = self.__robot[0] - x   
        y0 = self.__robot[1] - y
        
        if [x0,y0] in self.__objetivoCajas:
            self.__matriz[x0][y0] = 3 
        else: 
            self.__matriz[x0][y0] = 0
    

    def __mover(self,x,y):
        if self.__comprobarMovimientoVacio(self.__robot[0] + x, self.__robot[1] + y):
            self.__robot[0],self.__robot[1] = self.__robot[0] + x, self.__robot[1] + y #movemos robot
            self.__actualizarMatriz(x,y,False)
                        
        elif self.__matriz[self.__robot[0] + x][self.__robot[1] + y] == 2: 
            if self.__comprobarMovimientoVacio(self.__robot[0] + 2*x, self.__robot[1] + 2*y):
                self.__robot[0],self.__robot[1] = self.__robot[0] + x, self.__robot[1] + y #movemos robot
                for caja in self.__cajas:
                    if caja == self.__cajas:
                        caja[0],caja[1] = caja[0] + 2*x, caja[1] + 2*y #actualizamos la caja que estamos moviendo

            self.__actualizarMatriz(x,y,True)

    #0-celda vacia 1-muro 2-caja 3-objetivo 4-robot
    def movIzquierda(self):
        self.__mover(0, -1)
                       
    def movDerecha(self):
        self.__mover(0, +1)

    def movArriba(self):
        self.__mover(-1, 0)
            
    def movAbajo(self):
        self.__mover(1, 0)
    
