from estado import Estado
from random import randint


class Algoritmos():
    def __init__(self):
        self.nodosAbiertos = []
        self.nodosCerrados = []
        self.nodosTotales = 1

    def funcionAEstrella(self, estadoInicial):
        estado = estadoInicial
        estado.mostrarEstado()
        i = 0
        while not estado.ganar() and i<10_000: 
            self.nodosCerrados.append(estado)
            nuevosSucesores = estado.generarSucesores()
 
            for sucesor in nuevosSucesores:
                if sucesor not in self.nodosCerrados:
                    if sucesor not in self.nodosAbiertos:
                        
                        # Agregamos un nuevo nodo a la lista de abiertos
                        self.nodosTotales += 1
                        sucesor.calcularHeuristica()
                        self.nodosAbiertos.append(sucesor)
                    
                    # En caso de que un nodo abierto tenga mejor coste, lo cambiamos
                    else:
                        sucesorAntiguo = self.nodosAbiertos[self.nodosAbiertos.index(sucesor)]
                        if sucesor.getCoste() < sucesorAntiguo.getCoste():
                            self.nodosAbiertos[self.nodosAbiertos.index(sucesor)] = sucesor
                
                # En caso de que un nodo cerrado tenga mejor coste, actualizamos el padre de este (junto con su letra), 
                # su coste y el coste de toda su descendencia
                else:
                    sucesorAntiguo = self.nodosCerrados[self.nodosCerrados.index(sucesor)]
                    if sucesor.getCoste() < sucesorAntiguo.getCoste():
                        sucesorAntiguo.setPadre(sucesor.getPadre())
                        sucesorAntiguo.setLetra(sucesor.getLetra())
                        sucesorAntiguo.actualizarCosteSucesores()
                       
            # Ordenamos la lista de abiertos por heurística + coste (Coste + HEURistica = Cheur) y elegimos el mejor
            self.nodosAbiertos = sorted(self.nodosAbiertos, key=lambda x: x.getCheur())
            estado = self.nodosAbiertos[0]
            self.nodosAbiertos.pop(0)
            i += 1
            
        if(i == 10_000):
            print("No se encontró solución")
        else:
            # Imprimimos solución
            estado.imprimirPadres()
            print("Nodos totales: ", self.nodosTotales)
            print("Coste de la solución: ", estado.getCoste())
            
    def primeroMejor(self, estadoInicial):
        estado = estadoInicial
        estado.mostrarEstado()
        i = 0
        while not estado.ganar() and i<10_000: 
            self.nodosCerrados.append(estado)
            nuevosSucesores = estado.generarSucesores()
 
            for sucesor in nuevosSucesores:
                if sucesor not in self.nodosCerrados and sucesor not in self.nodosAbiertos:
                    # Agregamos un nuevo nodo a la lista de abiertos
                    self.nodosTotales += 1
                    sucesor.calcularHeuristica()
                    self.nodosAbiertos.append(sucesor)
                    
            # Ordenamos los nodos por heurística y elegimos el primero
            self.nodosAbiertos = sorted(self.nodosAbiertos, key=lambda x: x.getHeuristica())
            estado = self.nodosAbiertos[0]
            self.nodosAbiertos.pop(0)
            i += 1
        
        if(i == 10000):
            print("No se encontró solución")
        else:
            # Imprimimos solución
            estado.imprimirPadres()
            print("Nodos totales: ", self.nodosTotales)
            print("Coste de la solución: ", estado.getCoste())
  
    def maximaPendiente(self, estadoInicial):
        estado = estadoInicial
        self.nodosCerrados = []
        self.nodosTotales = 0
        while not estado.ganar():
            
            self.nodosAbiertos = []
            self.nodosCerrados.append(estado)
            nuevosSucesores = estado.generarSucesores()
            self.nodosTotales += len(nuevosSucesores)
            for sucesor in nuevosSucesores:
                sucesor.calcularHeuristica()
                self.nodosAbiertos.append(sucesor)

            listaNodos = sorted(self.nodosAbiertos, key=lambda x: x.getHeuristica())
            listaNodos = [x for x in listaNodos if x.getHeuristica() == listaNodos[0].getHeuristica() and x not in self.nodosCerrados
                          and x.getHeuristica() < estado.getHeuristica()]
            
            if(len(listaNodos) == 0):
                print("No encuentra solución")
                return False

            estado = listaNodos[randint(0,len(listaNodos)-1)]
            estado.mostrarEstado()


    def maximaPendienteRandom(self, estadoInicial):
        ganar    = 1
        intentos = 0
        while not self.__maximaPendienteRandom(estadoInicial) and intentos<1000000:
            intentos += 1
            if intentos % 1000 == 0:
                print(f"Intento número {intentos}")
        print(f"Intentos: {intentos}")
        
    def __maximaPendienteRandom(self, estadoInicial):
        estado = estadoInicial
        self.nodosCerrados = []
        self.nodosTotales=0
        for i in range(100):
            self.nodosCerrados.append(estado)
            nuevosSucesores = estado.generarSucesores()
            self.nodosTotales += len(nuevosSucesores)
            for sucesor in nuevosSucesores:
                if sucesor not in self.nodosCerrados:
                    sucesor.calcularHeuristica2()
                else:
                    sucesor.calcularHeuristica2()
                    sucesor.setHeuristica(sucesor.getHeuristica()+100)

            nuevosSucesores = sorted(nuevosSucesores, key=lambda x: x.getHeuristica())[0:2]

            estado = nuevosSucesores[randint(0,len(nuevosSucesores)-1)]
            
            if estado.ganar():
                estado.imprimirPadres()
                print("Nodos totales: ", self.nodosTotales)
                print("Coste de la solución: ", estado.getCoste())
                return True
        return False


        estado.imprimirPadres()
        print("Nodos totales: ", self.nodosTotales)
        print("Coste de la solución: ", estado.getCoste()) 
        

