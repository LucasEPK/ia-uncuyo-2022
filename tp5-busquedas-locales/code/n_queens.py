#modulo que configura el agente que mueve las reinas en el tablero, que va a ser resuelto por hill climbing, simulated annealing y algoritmo genetico
from f_matrices import *
from local_search_a import SimulatedAnnealing, geneticAlgorithm, hillClimbing
import math, random, time

class Environment: #clase que configura el tablero sus funciones y atributos y coloca las reinas de manera random en el
    def __init__(self, size): #sizeY es el numero de filas y sizeX es el numero de columnas

        self.tablero= 0 #se crea el arreglo que representa el tablero
        self.population = 0
        self.size = size
        #nota: el tablero va a ser siempre cuadrado

    def crear_tablero(self): #creamos un arreglo de tamaño N, donde en cada posición hace referencia a una columna de tablero. Y cada valor hace referencia a una fila.
        tablero = [] #el tablero lo vemos de abajo hacia arriba
        for i in range(0, self.size):
            tablero.append(random.randint(0, self.size-1))

        self.tablero = tablero

    def crear_k_tableros(self, k): #creamos un array con k tableros de tamaño size y lo devolvemos
        population = []

        #creamos los k tableros
        for i in range(k):
            
            tablero = [] #el tablero lo vemos de abajo hacia arriba
            for i in range(0, self.size):
                tablero.append(random.randint(0, self.size-1))
            population.append(tablero)

        self.population = population

class Agent: #clase agente que va a ser quien resuelva el problema de las n_reinas

    def solve_by_HillClimbing(self, env): #intenta resolver el problema de las n_reinas a travez de hill climbing
        start = time.time()
        print("Original:\n", env.tablero)

        solution = hillClimbing(env.tablero)
        
        print("Mejor solucion encontrada por Hill Climbing:\n", solution)
        stop=time.time()
        print("Tiempo de ejecución:", stop-start)
        return

    def solve_by_SimulatedAnnealing(self, env):
        start = time.time()
        print("Original:\n", env.tablero)

        solution = SimulatedAnnealing(env.tablero)

        print("Mejor solucion encontrada por simulated annealing:\n", solution)
        stop=time.time()
        print("Tiempo de ejecución:", stop-start)

    def solve_by_GeneticAlgorithm(self, env):
        start = time.time()
        print("Poblacion original:\n", env.population)

        solution = geneticAlgorithm(env.population)

        print("Mejor solucion encontrada:\n", solution)
        stop=time.time()
        print("Tiempo de ejecución:", stop-start)