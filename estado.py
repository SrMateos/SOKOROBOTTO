from tkinter.messagebox import NO


class Estado():
    def __init__(self, robot, cajas):
        self.__robot = robot
        self.__cajas = cajas

        self.__heuristica = 0
        self.__coste      = 0

        self.__sucesores = []
        self.__padre     = None

    def setRobot(self):
        pass

    def setCajas(self):
        pass

    def getRobot(self):
        pass

    def getCajas(self):
        pass

    def getHeuristica(self):
        pass

    def getCoste(self):
        pass
    
    def generarSucesores(self):
        pass

    def calcularHeurística(self):
        pass

