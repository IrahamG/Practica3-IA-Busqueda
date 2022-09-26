"""
Practica 3.2: Busqueda
25 - Sep - 2022
Equipo 2:
    Gardea Saucedo Carlos Iraham
    Granillo Gutierrez Nancy Michel
    Lazareno Lopez Julio Eduardo
El programa consiste en simular un agente movil que se desplaza por una pista en
forma de espina de pescado, con una vertebra principal y costillas las cuales pueden
tener el objetivo de manera aleatoria.
El agente buscará entre las costillas para encontrar el objetivo y cuando lo encuentre
se va a dirigir al final.
"""

# Importación de las librerias
from anytree import Node
from random import randint

# Creación de un objeto llamado Agente, este almacenará su nombre y su ubicación
# en la espina o en este caso en el arbol
class Agente:
    def __init__(self, nombre, ubi):
        self.nombre = nombre
        self.ubi = ubi

# Creación de un arbol para representar la espina de pescado por la cual se
# moverá el agente
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

# Lista de los nombres para los nodos en los cuales puede aparecer el objetivo
letterList = ['B', 'C', 'E', 'F', 'H', 'I', 'K', 'L']
# Generar un numero aleatorio para escoger de la lista anterior una letra al azar.
randomInt = randint(0, 7)
randomLet = letterList[randomInt]
# Bandera que determina si ya se encontró el objetivo
flag = 0

print("El objetivo se encuentra en: " + randomLet)

"""
Mientras que el agente no se encuentre en el objetivo final este bucle seguira
activo. Primero se verifican los hijos del agente y si uno de estos es secundario
se dirigirá a el para ver si se encuentra el objetivo, si no se encuentra se
dirige al otro nodo secundario para verificar, si no lo encuentra se dirige al
tercer hijo, el cual es uno nodo principal y el que tiene otros tres hijos.
Asi sucesivamente hasta que el agente encuentre el objetivo, cuando se encuentra
la bandera se enciende y el agente ya no tiene que verificar los nodos secundarios
del arbol, solo continuar por los primarios hasta la salida.
"""

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
input("Presione cualquier tecla para continuar: ")