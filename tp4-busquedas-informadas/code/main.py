from f_matrices import *
from laberinto import *

p_inicialY = random.randint(0,99)
p_inicialX = random.randint(0,99)
p_finalY = random.randint(0,99)
p_finalX = random.randint(0,99)
obstacle_rate = random.randint(5,10)/100
mapa = Environment(100,100, p_inicialX, p_inicialY, p_finalX, p_finalY, obstacle_rate)

agent = Agent(mapa)
think = agent.solve_by_aStar(mapa)
