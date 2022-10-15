from n_queens import *

#como el tablero se representa por un arreglo el numero de reinas tiene que ser igual al tamaño del tablero
env = Environment(8)
agente = Agent()
agente.solve_by_HillClimbing(env)
#??????????????recorre demasiados estados fijate porque????????????