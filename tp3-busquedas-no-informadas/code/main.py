from f_matrices import *
from laberinto import *

mapa = Environment(100,100, 0, 0, 99, 99, 0.2)

agent = Agent(mapa)

think = agent.solve_by_bfs(mapa)

think = agent.solve_by_US(mapa)

think = agent.solve_by_dfsL(mapa)