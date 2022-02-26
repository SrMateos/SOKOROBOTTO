class Tablero:
    def __init__(self):
        # Matriz tablero
        self.__matriz = [[]]
        # Posicion robot
        self.__robot  = None
        # Posiciones cajas
        self.__cajas  = []
        # Posiciones objetivo cajas
        self.__objetivoCajas = []

    def cargarDatos(self, fichero):
        # Abrimos el fichero
        f = open(fichero,'r')
        # Leemos el fichero entero, quitamos todos los saltos de línea, separamos por comas y quitamos espacio final
        l = f.read().replace('\n','').split(",")[0:-1]
        # Convertimos a __matriz de enteros y devolvemos
        self.__matriz = [[int(l[i*10+j]) for j in range(10) ] for i in range(10)]
        # Guardamos 
        self.__posicionJugadorCajas()
  
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
        # Mostrado de datos
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
    
    
    def __actualizarMatriz(self,x,y,movimientoCaja):
        # Actualizar Robot
        self.__matriz[self.__robot[0]][self.__robot[1]] = 4
        
        # Pintamos Caja más si ha habido movimiento de caja
        if movimientoCaja:
            self.__matriz[self.__robot[0] + x][self.__robot[1] + y] = 2
        
        # Antigua posicion de robot
        x0 = self.__robot[0] - x   
        y0 = self.__robot[1] - y
        
        # Si la posicion antigua del robot era un objetivo
        if [x0,y0] in self.__objetivoCajas: 
            self.__matriz[x0][y0] = 3 
        else: 
            self.__matriz[x0][y0] = 0

    def __mover(self,x,y,empujar):
        if self.__comprobarMovimientoVacio(self.__robot[0] + x, self.__robot[1] + y) and not empujar:
            # Movemos robot
            self.__robot[0],self.__robot[1] = self.__robot[0] + x, self.__robot[1] + y 
            self.__actualizarMatriz(x,y,False)
                        
        elif self.__matriz[self.__robot[0] + x][self.__robot[1] + y] == 2 and empujar: 
            if self.__comprobarMovimientoVacio(self.__robot[0] + 2*x, self.__robot[1] + 2*y):
                
                # Movemos robot
                self.__robot[0],self.__robot[1] = self.__robot[0] + x, self.__robot[1] + y 
                for caja in self.__cajas:
                    # TODO self.__cajas
                    if caja == self.__robot:
                        # Actualizamos la caja que estamos moviendo
                        caja[0],caja[1] = caja[0] + x, caja[1] + y 

            self.__actualizarMatriz(x,y,True)

    def movIzquierda(self,empujar):
        self.__mover(0, -1, empujar)
                       
    def movDerecha(self,empujar):
        self.__mover(0, 1, empujar)

    def movArriba(self,empujar):
        self.__mover(-1, 0, empujar)
            
    def movAbajo(self,empujar):
        self.__mover(1, 0, empujar)
    
    def intercambio(self, x, y):
        for caja in self.__cajas:
            if [self.__robot[0] + x , self.__robot[1] + y] == caja:
                self.__robot[0], self.__robot[1] = caja[0], caja[1]
                caja[0], caja[1] = caja[0] - x, caja[1] - y
                self.__matriz[self.__robot[0]][self.__robot[1]] = 4
                self.__matriz[caja[0]][caja[1]] = 2
                            
    def intercambioIzquierda(self):
        self.intercambio(0, -1)
    
    def intercambioDerecha(self):
        self.intercambio(0, 1)
    
    def intercambioArriba(self):
        self.intercambio(-1, 0)
    
    def intercambioAbajo(self):
        self.intercambio(1, 0)
    
    def ganar(self):
        for caja in self.__cajas:
            if caja not in self.__objetivoCajas:
                return False 
        
        return True 