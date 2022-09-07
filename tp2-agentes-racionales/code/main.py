from f_matrices import *
from aspiradora import *

dimensiones= 2
i=1
while dimensiones <= 128:
    dirt_rate = 0.1
    if dimensiones != 8:
        while dirt_rate <= 0.8:
            mapa1 = Environment(dimensiones, dimensiones, dirt_rate)
            aspiradora1 = Agent(mapa1)

            print("Grilla: ",mapa1.sizeX,"X", mapa1.sizeY)
            print("Dirt rate:", dirt_rate)

            vida= aspiradora1.think(mapa1)

            print("Puntos finales:", aspiradora1.points)
            print("Vida al momento de dejar todo limpio o terminar:", vida)
            print("-----")
            dirt_rate= dirt_rate * 2

    i += 1
    dimensiones = 2 ** i

