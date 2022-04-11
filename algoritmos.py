from estado import Estado
from random import randint

class Algoritmos():
    def __init__(self):
        self.nodosAbiertos = []
        self.nodosCerrados = []
        self.nodosTotales = 1
    def metodologia(self):
        pass

    def funcionAEstrella(self, estadoInicial):
        estado = estadoInicial
        while estado.ganar() == False: 
            self.nodosCerrados.append(estado)
            nuevosSucesores = estado.generarSucesores()
 
            for sucesor in nuevosSucesores:
                if sucesor not in self.nodosCerrados and sucesor not in self.nodosAbiertos:
                    self.nodosTotales += 1
                    sucesor.calcularHeuristica()
                    self.nodosAbiertos.append(sucesor)
        
            self.nodosAbiertos = sorted(self.nodosAbiertos, key=lambda x: x.getCheur())
            
            estado = self.nodosAbiertos[0]
            self.nodosAbiertos.pop(0)
            
        print("ganamos siuuuuuuuuuuuuuuuuuuuuupato") 
        estado.imprimirPadres()
        print(self.nodosTotales)



    def maximaPendiente(self, estadoInicial):
        estado = estadoInicial
        estado.calcularHeuristica()
        for i in range(10000):
            nuevosSucesores = estado.generarSucesores()
            self.nodosTotales += len(nuevosSucesores)
            for sucesor in nuevosSucesores:
                    sucesor.calcularHeuristica()
                    
            estado = sorted(nuevosSucesores, key=lambda x: x.getHeuristica())[0]
            estado.mostrarEstado()
            if estado.ganar() == True:
                print("ganamos siuuuuuuuuuuuuuuuuuuuuupato") 
                estado.imprimirPadres()
                print(self.nodosTotales)
                return 0                   

    def maximaPendienteRandom(self, estadoInicial):
        estado = estadoInicial
        self.nodosCerrados = []
        self.nodosTotales=0
        for i in range(1000):
            self.nodosCerrados.append(estado)
            nuevosSucesores = estado.generarSucesores()
            self.nodosTotales += len(nuevosSucesores)
            for sucesor in nuevosSucesores:
                if sucesor not in self.nodosCerrados:
                    sucesor.calcularHeuristica()
                    
            nuevosSucesores = sorted(nuevosSucesores, key=lambda x: x.getHeuristica())[0:2]
            estado = nuevosSucesores[randint(0,len(nuevosSucesores)-1)]
            # estado.mostrarEstado()
            if estado.ganar() == True:
                print("ganamos siuuuuuuuuuuuuuuuuuuuuupato") 
                estado.imprimirPadres()
                print(self.nodosTotales)
                return 0
        return 1    
        
    def funcionAlfa(self,coste,estado): 
        pass


        

