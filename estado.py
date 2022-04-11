from tablero import Tablero
from direcciones import direccion

class Estado():
    tablero = None
    
    def __init__(self, robot, cajas, coste, padre, letra, intercambios):
        self.__robot = robot
        self.__cajas = cajas

        self.__heuristica = 99
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

    def setPadre(self,tab):
        self.__padre = tab

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

    def getTablero(self):
        return self.__tablero 

    def mostrarEstado(self):
        print("Robot: ", self.__robot)
        print("Cajas: ", self.__cajas)
        print("Coste: ", self.__coste)
        self.calcularHeuristica()
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
        distanciaMenorRobotCaja = 999
        cajaMasCercana = None
        for caja in self.__cajas:
            distancia = self.calcularDistancia(self.__robot, caja)
            if distancia < distanciaMenorRobotCaja:
                distanciaMenorRobotCaja = distancia
                cajaMasCercana = caja
        
        distanciaMenorCajaObjetivo = 999
        for objetivoCajas in Estado.tablero.getObjetivoCajas():
            distancia = self.calcularDistancia(cajaMasCercana, objetivoCajas)
            if distancia < distanciaMenorCajaObjetivo:
                distanciaMenorCajaObjetivo = distancia
        
        self.__heuristica = distanciaMenorRobotCaja + 7*distanciaMenorCajaObjetivo #heuristica actual = distancia a caja mas cercana TODO incorporar distancia de cajas a objetivos y otras cosas
        self.__cheur = 1.1*self.__coste + self.__heuristica

    def calcularHeuristica2(self):
        distanciaMenorRobotCaja = 999
        cajaMasCercana = None

        for caja in self.__cajas:
            distancia = self.calcularDistancia(self.__robot, caja)
            if distancia < distanciaMenorRobotCaja and caja not in Estado.tablero.getObjetivoCajas():
                distanciaMenorRobotCaja = distancia
                cajaMasCercana = caja

        distanciaMenorCajaObjetivo = 0
        if(cajaMasCercana != None):
            distanciaMenorCajaObjetivo = 999
            for objetivoCajas in Estado.tablero.getObjetivoCajas():
                distancia = self.calcularDistancia(cajaMasCercana, objetivoCajas)
                if distancia < distanciaMenorCajaObjetivo:
                    distanciaMenorCajaObjetivo = distancia

        distanciaMediaCajasObjetivos = 0
        for objetivoCaja in Estado.tablero.getObjetivoCajas():
            distanciaMenor = 99
            for caja in self.__cajas:
                if self.calcularDistancia(objetivoCaja,caja)<distanciaMenor:
                    distanciaMenor = self.calcularDistancia(objetivoCaja,caja) 
            distanciaMediaCajasObjetivos += distanciaMenor
        distanciaMediaCajasObjetivos /= len(self.__cajas)
        
        cajasEnObjetivos = 0
        for caja in self.__cajas:
            if(caja in Estado.tablero.getObjetivoCajas()):
                cajasEnObjetivos += 1

        self.__heuristica = distanciaMenorRobotCaja+ 4*distanciaMediaCajasObjetivos + 5*distanciaMenorCajaObjetivo + 10*cajasEnObjetivos
        self.__cheur = 1.5*self.__coste + self.__heuristica

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

    def ganar(self):
        return Estado.tablero.ganar(self.__cajas)
