from n_queens import *
from local_search_a import calcular_fitness_max, fitness

env = Environment(4)
# env.crear_tablero()
agente = Agent()
# print("RESOLUCION POR HILL CLIMBING:")
# agente.solve_by_HillClimbing(env)
# print("")

# print("RESOLUCION POR SIMULATED ANNEALING:")
# agente.solve_by_SimulatedAnnealing(env)
# print("")

env.crear_k_tableros(8)
print("RESOLUCION POR GENETIC ALGORITHM:")
agente.solve_by_GeneticAlgorithm(env)
print("")