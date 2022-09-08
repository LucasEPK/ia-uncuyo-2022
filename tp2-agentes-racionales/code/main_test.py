from f_matrices import *
from aspiradora_random import *

mapa1 = Environment(16, 16, 0.4)
aspiradora1 = Agent(mapa1)

print("Grilla: ",mapa1.sizeX,"X", mapa1.sizeY)
print("Dirt rate:", 0.4)

vida= aspiradora1.think(mapa1)

print("Puntos finales:", aspiradora1.points)
print("Vida al momento de dejar todo limpio o terminar:", vida)
print("-----")