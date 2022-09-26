# -*- coding: utf-8 -*-
"""
Practica 3. Crear un agente para que encuentre un objetivo en la pista
con forma de costilla con diferentes nodos.
Este programa es más que nada para probar la libreria de anytree y saber si 
nos va a servir para algo aaaaaaa.
"""

from anytree import Node, RenderTree
from random import randint

# Objeto de agente
class Agente:
    def __init__(self, nombre, ubi):
        self.nombre = nombre
        self.ubi = ubi

# Creación de nodos
#pepe = Node("pepe")
#morris = Node("morris", parent=pepe)
#etesech = Node("etesech", parent=pepe)

#print(pepe)
#print(morris)

# Imprimir el arbol de manera más visual.
#for pre, fill, node in RenderTree(pepe):
#    print("%s%s" % (pre, node.name))
    
# Creación del arbol para la mamada de IA
# Implementar de alguna u otra manera, ya sea por intervención divina o
# habilidad bruta, una forma de generar automaticamente el siguiente arbol:
inicio = Node("inicio")
nodoA = Node("A", parent=inicio, tipo="pri")
nodoB = Node("B", parent=nodoA, tipo="sec", pos="izq")
nodoC = Node("C", parent=nodoA, tipo="sec", pos="der")
nodoD = Node("D", parent=nodoA, tipo="pri")
nodoE = Node("E", parent=nodoD, tipo="sec", pos ="izq")
nodoF = Node("F", parent=nodoD, tipo="sec", pos ="der")
nodoG = Node("G", parent=nodoD, tipo="pri")
nodoH = Node("H", parent=nodoG, tipo="sec", pos="izqr")
nodoI = Node("I", parent=nodoG, tipo="sec", pos="der")
nodoJ = Node("J", parent=nodoG, tipo="pri")
nodoK = Node("K", parent=nodoJ, tipo="sec", pos="izq")
nodoL = Node("L", parent=nodoJ, tipo="sec", pos="der")
final = Node("final", parent=nodoJ, tipo="pri")


# Creación de un agente
ag1 = Agente("Pepe", inicio)

# Lista de los nombres para los nodos
letterList = ['B', 'C', 'E', 'F', 'H', 'I', 'K', 'L']
randomInt = randint(0, 7)
randomLet = letterList[randomInt]
flag = 0


# La idea del siguiente ciclo es que continue siempre y cuando el agente no se encuentre
# en el nodo final. En cada ciclo el agente pasará por un for para determinar sus
# hijos y si estos son secundarios va a determinar si este es el elegido para que sea
# el objetivo, de lo contrario pasará al siguiente nodo principal y hará lo mismo.

print("El objetivo se encuentra en: " + randomLet)

while (ag1.ubi != final):
    print("El agente se movio hacia: " + ag1.ubi.name)
    if(flag == 0):
        for child in ag1.ubi.children:
            if(child.tipo == "sec"):
                ag1.ubi = child
                print("El agente se movio hacia: " + ag1.ubi.name)
                if(ag1.ubi.name == randomLet):
                    flag = 1
                    print("El agente encontró el objetivo")
                ag1.ubi = child.parent
                print("El agente se movio hacia: " + ag1.ubi.name)
            if(child.tipo == "pri"):
                nextLoc = child
        ag1.ubi = nextLoc
        
    elif(flag == 1):
            for child in ag1.ubi.children:
                if(child.tipo == "pri"):
                    ag1.ubi = child
                    print("El agente se movio hacia: " + ag1.ubi.name)
                    
                    
print("El agente llegó a la meta")

"""while(True):
    for child in ag1.ubi.children:
        if(child.tipo == "sec"):
            ag1.ubi = child
            print(ag1.ubi)
    break
"""    
            



"""for pre, fill, node in RenderTree(inicio):
    print("%s%s" % (pre, node.name))
    
for child in inicio.children:
    if "A" == child.name:
        print("Se encontro el A mi gente")"""