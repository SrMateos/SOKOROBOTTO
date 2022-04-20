from tablero import Tablero
from direcciones import direccion

class Estado():
    tablero = None
    
    def __init__(self, robot, cajas, coste, padre, letra, intercambios):
        self.__robot = robot
        self.__cajas = cajas

        self.__heuristica = 9999
        self.__coste      = coste
        self.__cheur      = 0
        

        self.__sucesores = []
        self.__padre     = padre

        self.__letra = letra

        self.__intercambios = intercambios

    def __eq__(self, other):
        if other != None:
            return self.__robot == other.getRobot() and self.__cajas == other.getCajas()
        return False

    def __ne__(self, other):
        if other != None:
            return self.__robot != other.getRobot() or self.__cajas != other.getCajas()
        return True

    def setTablero(tab):
        Estado.tablero = tab

    def setPadre(self,padre):
        self.__padre = padre

    def setCoste(self, coste):
        self.__coste = coste
    
    def setLetra(self, letra):
        self.__letra = letra

    def setHeuristica(self, heuristica):
        self.__heuristica = heuristica

    def getRobot(self):
        return self.__robot

    def getCajas(self):
        return self.__cajas
    
    def getHeuristica(self):
        return self.__heuristica
    
    def getCheur(self):
        return self.__cheur

    def getCoste(self):
        return self.__coste

    def getSucesores(self):
        return self.__sucesores

    def getTablero(self):
        return Estado.tablero 

    def getPadre(self):
        return self.__padre 

    def getLetra(self):
        return self.__letra 

    def mostrarEstado(self):
        print()
        print("Robot: ", self.__robot)
        print("Cajas: ", self.__cajas)
        print("Coste: ", self.__coste)
        print("Letra: ", self.__letra)
        # self.calcularHeuristica()
        print("h': ", self.__heuristica)
        Estado.tablero.mostrarTablero(self.__robot, self.__cajas)

    def mostrarHijos(self):
        for suc in self.__sucesores:
            suc.mostrarEstado()

    def generarSucesores(self):
        self.generarSucesoresMovimiento()
        self.generarSucesoresEmpujar()
        self.generarSucesoresIntercambiar()
        return self.__sucesores

    def generarSucesoresMovimiento(self):
        direcciones = ["A","B","I","D"]
        for i in direcciones:
            movimientoValido, robot = Estado.tablero.comprobarMovimiento(i, self.__robot, self.__cajas)
            if movimientoValido and self.__padre != self:
                self.__sucesores.append(Estado(robot, self.__cajas, self.__coste+1, self, i, self.__intercambios)) 
    
    def generarSucesoresEmpujar(self):
        direcciones = ["EA","EB","EI","ED"]
        for i in direcciones:
            movimientoValido, robot, caja = Estado.tablero.comprobarEmpuje(i, self.__robot, self.__cajas)
            if movimientoValido and self.__padre != self:
                cajas = [c for c in self.__cajas if c != robot]
                cajas.append(caja)
                self.__sucesores.append(Estado(robot, cajas, self.__coste+1, self, i, self.__intercambios))
                
    def generarSucesoresIntercambiar(self):
        direcciones = ["IA","IB","II","ID"]
        if self.__intercambios > 0:
            for i in direcciones:
                movimientoValido, robot, caja = Estado.tablero.comprobarIntercambio(i, self.__robot, self.__cajas)
                if movimientoValido and self.__padre != self:
                    cajas = [c for c in self.__cajas if c != robot]
                    cajas.append(caja)
                    self.__sucesores.append(Estado(robot, cajas, self.__coste+1, self, i, self.__intercambios - 1))

    def calcularHeuristica(self):
    # calculo de la distancia del robot a la caja mas cercana que no esté en un objetivo
        distanciaMenorRobotCaja = 999
        cajaMasCercana = None
        for caja in self.__cajas:
            distancia = self.calcularDistancia(self.__robot, caja)
            # print(self.__robot)
            # print(caja)
            if distancia < distanciaMenorRobotCaja and caja not in Estado.tablero.getObjetivoCajas():
                # print(f"distancia: {distancia} y distanciaMenorRobotCaja: {distanciaMenorRobotCaja}")
                distanciaMenorRobotCaja = distancia
                cajaMasCercana = caja
        
        # print("cajamascercana: ", cajaMasCercana)

        # calculo de la distancia de la caja mas cercana que no esta en un objetivo (si hay) a su objetivo mas cercano
        distanciaMenorCajaObjetivo = 0
        distancia = 0
        if(cajaMasCercana != None):
            distanciaMenorCajaObjetivo = 999
            for objetivoCajas in Estado.tablero.getObjetivoCajas():
                distancia = self.calcularDistancia(cajaMasCercana, objetivoCajas)
                if distancia < distanciaMenorCajaObjetivo:
                    distanciaMenorCajaObjetivo = distancia
        else:
            distanciaMenorRobotCaja = 0

        #calculo de las cajas que no estan en objetivos
        cajasNoEnObjetivos = 0
        for caja in self.__cajas:
            if(caja not in Estado.tablero.getObjetivoCajas()):
                cajasNoEnObjetivos += 100
        
        # print(" Distancia caja mas cercana: ", distanciaMenorRobotCaja, " Distancia caja mas cercana objetivo: ", distanciaMenorCajaObjetivo, " Cajas no en objetivos: ", cajasNoEnObjetivos)
        self.__heuristica = 3*distanciaMenorRobotCaja  + distanciaMenorCajaObjetivo + cajasNoEnObjetivos
        self.__cheur = self.__coste + self.__heuristica # 7.143 valor de coste mejor
    
    def calcularHeuristica2(self):
        distanciaMenorRobotCaja = 999
        cajaMasCercana = None
        for caja in self.__cajas:
            distancia = self.calcularDistancia(self.__robot, caja)
            if distancia < distanciaMenorRobotCaja and caja not in Estado.tablero.getObjetivoCajas():
                # print(f"distancia: {distancia} y distanciaMenorRobotCaja: {distanciaMenorRobotCaja}")
                distanciaMenorRobotCaja = distancia
                cajaMasCercana = caja

        distanciaMenorCajaObjetivo = 0
        if(cajaMasCercana != None):
            distanciaMenorCajaObjetivo = 999
            for objetivoCajas in Estado.tablero.getObjetivoCajas():
                distancia = self.calcularDistancia(cajaMasCercana, objetivoCajas)
                if distancia < distanciaMenorCajaObjetivo:
                    distanciaMenorCajaObjetivo = distancia
        else:
            distanciaMenorRobotCaja = 0
    
        self.__heuristica = distanciaMenorRobotCaja + 7*distanciaMenorCajaObjetivo 
        self.__cheur = self.__coste + self.__heuristica

    def calcularDistancia(self, punto1,punto2):
        return abs(punto1[0]-punto2[0]) + abs (punto1[1]-punto2[1])

    def imprimirPadres(self):
        lista = []
        self.__imprimirPadres(lista)
        print(lista)

    def __imprimirPadres(self,lista):
        if(self.__padre != None):
            self.__padre.__imprimirPadres(lista)
            lista.append(self.__letra)
        
        self.mostrarEstado()

    def actualizarCosteSucesores(self):
        self.__coste = self.__padre.getCoste()+1
        for suc in self.__sucesores:
            suc.actualizarCosteSucesores()

    def ganar(self):
        return Estado.tablero.ganar(self.__cajas)
