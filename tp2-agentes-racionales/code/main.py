from f_matrices import *
from aspiradora import *

mapa1 = Environment(4, 4)
aspiradora = Agent(mapa1)

aspiradora.think(mapa1)

print("Puntos finales:", aspiradora.points)
print("Vida final:", mapa1.life)