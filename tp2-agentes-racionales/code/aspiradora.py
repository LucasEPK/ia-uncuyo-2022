#modulo que configura el agente aspiradora
from random import random
from f_matrices import *
import math, random

class Environment:
    def __init__(self, sizeX, sizeY):

        self.sizeX= sizeX
        self.sizeY= sizeY
        self.mapa= crear_matriz(sizeY, sizeX) #se crea la grilla en la que se mueve el agente
        llenar_matriz(self.mapa, 0)
        self.dirt_count = ensuciar(self.mapa)

        self.init_posX= random.randint(0, len(self.mapa[0])-1)
        self.init_posY= random.randint(0,len(self.mapa)-1)

        self.dirt_rate= calcular_suciedad(self) #porcentaje de suciedad en total
        self.life = 1000 #acciones maximas


    def accept_action(self, action, agent):
        if self.life != 0:
            self.life -= 1
            
            if action == 0: #up
                print("arriba")
                #verificamos que no nos salgamos de los bordes
                if agent.posY - 1 < 0:
                    return False
                else:
                    return True
            elif action == 1: #down
                print("abajo")
                #verificamos que no nos salgamos de los bordes
                if agent.posY + 1 >= self.sizeY:
                    return False
                else:
                    return True
            elif action == 2: #left
                print("izquierda")
                #verificamos que no nos salgamos de los bordes
                if agent.posX - 1 < 0:
                    return False
                else:
                    return True
            elif action == 3: #right
                print("derecha")
                #verificamos que no nos salgamos de los bordes
                if agent.posX + 1 >= self.sizeX:
                    return False
                else:
                    return True
            elif action == 4: #suck
                print("limpiar")
                #limpiamos el espacio en donde esta el agente, sacamos uno a dirt count y recalculamos el dirt rate

                self.mapa[agent.posY][agent.posX]= 0
                self.dirt_count -= 1
                self.dirt_rate = calcular_suciedad(self)

                return True
            elif action == 5: #idle
                #print("ociar")
                return True

        else:
            print("Action denied")
            return False

    def is_dirty(self, X, Y): #funcion que devuelve si una casilla está sucia
        if self.mapa[Y][X] == 0:
            return False
        else:
            return True

    def get_performance(self):
        return self.points

    def print_environment(self, agent): #imprime el mapa con el agente

        filas = len(self.mapa)
        for i in range(filas):
            columnas = len(self.mapa[i])
            for j in range(columnas):
                if i != agent.posY or j != agent.posX:
                    print(self.mapa[i][j], end=' ')
                else:
                    print('X', end=' ')
            print()

def ensuciar(mapa):#ensucia de manera random la mitad o menos del mapa y devuelve la cantidad de sucedia total

    dirt = 1
    dirt_count = 0
    for k in range(math.trunc(len(mapa)*len(mapa[0])/2)):
        i= random.randint(0,len(mapa)-1)
        j= random.randint(0, len(mapa[i])-1)
        if mapa[i][j] == 0:
            mapa[i][j]= dirt
            dirt_count += 1
            
    return dirt_count

def calcular_suciedad(env):

    return env.dirt_count / (env.sizeY * env.sizeX)

class Agent:
    def __init__(self, env):
        self.posX = env.init_posX
        self.posY = env.init_posY
        self.points = 0 #puntos asignados

    def up(self, env): #accion 0
        if env.accept_action(0, self):
            self.posY -= 1

    def down(self, env): #accion 
        if env.accept_action(1, self):
            self.posY += 1

    def left(self, env): #accion 2
        if env.accept_action(2, self):
            self.posX -= 1

    def right(self, env): #accion 3
        if env.accept_action(3, self):
            self.posX += 1

    def suck(self, env): #accion 4
        env.accept_action(4, self)
        self.points += 1 

    def idle(self, env): #accion 5
        env.accept_action(5, self)

    def perspective(self, env): #accion 6
        #el agente solo percibe la casilla en donde está
        #esta accion no quita vida
        return env.mapa[self.posY][self.posX] #envia si la casilla esta sucia (1) o limpia (0)

    def think(self, env): #accion 7
        #esta accion no quita vida

        life_remaining = 0
        while env.life != 0: #mientras tengamos acciones disponibles vamos a 

            if env.dirt_rate != 0:
                print("posicion:","X:", self.posX,"Y:", self.posY)
                print("vida:", env.life)
                print("puntos:", self.points)
                env.print_environment(self)

            if self.perspective(env) == 1: #si estamos en una casilla sucia la limpiamos
                self.suck(env)
            else:
                if env.dirt_rate == 0: #si no hay más suciedad, nos quedamos idles
                    return env.life #dato que nos sirve para calcular eficiencia
                    #self.idle(env)
                else: #si sigue habiendo suciedad nos movemos de forma random para encontrar suciedad
                    self.move_random(env)

            if env.dirt_rate != 0:
                print("---------")

        return life_remaining

    def move_random(self, env): #elige entre ir arriba abajo derecha izquierda de manera random
        accion= random.randint(0, 3)

        if accion == 0:
            self.up(env)
        elif accion == 1:
            self.down(env)
        elif accion == 2:
            self.left(env)
        elif accion == 3:
            self.right(env)