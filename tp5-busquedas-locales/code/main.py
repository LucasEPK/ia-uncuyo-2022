from local_search_a import fitness
from n_queens import *

#como el tablero se representa por un arreglo el numero de reinas tiene que ser igual al tamaño del tablero
#env = Environment(8)
agente = Agent()
#agente.solve_by_HillClimbing(env)
#??????????????recorre demasiados estados fijate porque????????????

env = Environment(8)
env.crear_k_tableros(8)
agente.solve_by_GeneticAlgorithm(env)

