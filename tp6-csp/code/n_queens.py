#modulo que configura el agente que mueve las reinas en el tablero, que va a ser resuelto por hill climbing, simulated annealing y algoritmo genetico
from f_matrices import *
from csp import CSP, Variables, forward_checking_search, backtracking_search
import copy
import time

class Environment: #clase que configura el csp
    def __init__(self, size): #size es el numero de filas y columnas

        self.csp = 0 #se crea el csp que representa el problema de las n-reinas
        self.size = size
        #nota: el tablero va a ser siempre cuadrado

    def crear_csp(self): #creamos un csp para el problema de las n-queens
        csp1 = CSP()
        csp1.variables = []
        domain = []
        for i in range(self.size):
            domain.append(i)
        for i in range(self.size):
            v1 = Variables()
            v1.value = i
            v1.domain = copy.deepcopy(domain)
            csp1.variables.append(v1)
        self.csp = csp1


class Agent: #clase agente que va a ser quien resuelva el problema de las n_reinas

    def solve_by_Backtracking(self, env): #resuelve el problema de las n_reinas a travez de backtracking
        start = time.time()

        solution = backtracking_search(env.csp)
        
        print("Solucion encontrada por Backtracking:\n", solution)
        stop=time.time()
        print("Tiempo de ejecución:", stop-start)
        return

    def solve_by_Forward_Checking(self, env): #resuelve el problema de las n_reinas a travez de forward checking
        start = time.time()

        solution = forward_checking_search(env.csp)

        print("Solucion encontrada por Forward Checking:\n", solution)
        stop=time.time()
        print("Tiempo de ejecución:", stop-start)
