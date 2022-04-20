
from direcciones import direccion

class Tablero:
    def __init__(self,matriz,objetivoCajas):
        # Matriz tablero
        self.__matriz = matriz
        # Posiciones objetivo cajas
        self.__objetivoCajas = objetivoCajas

    def getObjetivoCajas(self):
        return self.__objetivoCajas

    def getMatriz(self):
        return self.__matriz

    def mostrarTablero(self,robot,cajas):
        # Mostrado de datos
        print(end='   ')
        for i in range(10):
            print(i, end=' ')
        print()
        print()

        for i in range(10):
            print(i, end='  ')
            for j in range(10):
                if [i,j] == robot:
                    print(4, end=' ')
                elif [i,j] in cajas:
                    print(2, end=' ')
                elif [i,j] in self.__objetivoCajas:
                    print(3, end=' ')
                elif self.__matriz[i][j] == 0:
                    print(".", end=' ')
                else:
                     print(self.__matriz[i][j], end=' ')
            print()
                
    def mostrarPosicionObjetivo(self):
        print(self.__objetivoCajas)

    def comprobarMovimiento(self, s ,robot, cajas):
        diccionarioDireccion = {"A":direccion.ARRIBA, "B":direccion.ABAJO, "I":direccion.IZQUIERDA, "D":direccion.DERECHA}
        
        d = diccionarioDireccion.get(s).getCoordenadas()
        posicionRobot = [robot[0]+d[0],robot[1]+d[1]]
        return self.__matriz[posicionRobot[0]][posicionRobot[1]] != 1 and posicionRobot not in cajas, posicionRobot

    def comprobarEmpuje(self, s, robot, cajas):
        diccionarioDireccion = {"EA":direccion.ARRIBA, "EB":direccion.ABAJO, "EI":direccion.IZQUIERDA, "ED":direccion.DERECHA}
        d = diccionarioDireccion.get(s).getCoordenadas()
        posicionRobot = [robot[0]+d[0],robot[1]+d[1]]
        posicionCaja = [posicionRobot[0]+d[0],posicionRobot[1]+d[1]]
        return  posicionRobot in cajas and posicionCaja not in cajas and self.__matriz[posicionRobot[0]][posicionRobot[1]] in [0,3] and self.__matriz[posicionCaja[0]][posicionCaja[1]] in [0,3], posicionRobot, posicionCaja

    def comprobarIntercambio(self, s, robot, cajas):
        diccionarioDireccion = {"IA":direccion.ARRIBA, "IB":direccion.ABAJO, "II":direccion.IZQUIERDA, "ID":direccion.DERECHA}
        d = diccionarioDireccion.get(s).getCoordenadas()
        posicionRobot,posicionCaja = [robot[0]+d[0],robot[1]+d[1]],robot
        return  posicionRobot in cajas, posicionRobot, posicionCaja

    def ganar(self,cajas):
        for caja in cajas:
            if caja not in self.__objetivoCajas:
                return False 
        
        return True 
