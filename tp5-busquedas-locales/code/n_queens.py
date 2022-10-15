#modulo que configura el agente que mueve las reinas en el tablero, que va a ser resuelto por hill climbing, simulated annealing y algoritmo genetico
from f_matrices import *
from local_search_a import hillClimbing
import math, random

class Environment: #clase que configura el tablero sus funciones y atributos y coloca las reinas de manera random en el
    def __init__(self, size): #sizeY es el numero de filas y sizeX es el numero de columnas

        self.tablero= crear_tablero(size) #se crea el arreglo que representa el tablero
        #nota: el tablero va a ser siempre cuadrado

def crear_tablero(size): #creamos un arreglo de tamaño N, donde en cada posición hace referencia a una columna de tablero. Y cada valor hace referencia a una fila.
    tablero = [] #el tablero lo vemos de abajo hacia arriba
    for i in range(0, size):
        tablero.append(random.randint(0,size-1))

    return tablero

class Agent: #clase agente que va a ser quien resuelva el problema de las n_reinas

    def solve_by_HillClimbing(self, env): #intenta resolver el problema de las n_reinas a travez de hill climbing
        print("Original:\n", env.tablero)

        solution = hillClimbing(env.tablero)
        
        print("Mejor solucion encontrada por Hill Climbing:\n", solution)
        return
