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
        ensuciar(self.mapa)

        self.init_posX= random.randint(0, len(self.mapa[0])-1)
        self.init_posY= random.randint(0,len(self.mapa)-1)

        self.dirt_rate= dirt_rate #porcentaje de suciedad en total
        self.life = 1000 #acciones maximas


    def accept_action(self, action, agent):
        if self.life != 0:
            self.life -= 1
            
            if action == 0: #up
                #verificamos que no nos salgamos de los bordes
                if agent.posY + 1 >= self.sizeY:
                    return False
                else:
                    return True
            elif action == 1: #down
                #verificamos que no nos salgamos de los bordes
                if agent.posY - 1 < 0:
                    return False
                else:
                    return True
            elif action == 2: #left
                #verificamos que no nos salgamos de los bordes
                if agent.posX - 1 < 0:
                    return False
                else:
                    return True
            elif action == 3: #right
                #verificamos que no nos salgamos de los bordes
                if agent.posX + 1 >= self.sizeX:
                    return False
                else:
                    return True
            elif action == 4: #suck
                #limpiamos el espacio en donde esta el agente

                self.mapa[agent.posY][agent.posX]= 0
                return True
            elif action == 5: #idle
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

    def print_enviroment(self): #falta terminar
        self.mapa

def ensuciar(mapa):#ensucia de manera random la mitad o menos del mapa

    dirt = 1
    for k in range(math.trunc(len(mapa)*len(mapa[i])/2)):
        i= random.randint(0,len(mapa)-1)
        j= random.randint(0, len(mapa[i])-1)
        mapa[i][j]= dirt

class Agent():
    def __init__(self, env):
        self.posX = env.init_posX
        self.posY = env.init_posY
        self.points = 0 #puntos asignados

    def up(self, env): #accion 0
        if env.accept_action(env, 0, self):
            self.posY += 1

    def down(self, env): #accion 
        if env.accept_action(env, 1, self):
            self.posY -= 1

    def left(self, env): #accion 2
        if env.accept_action(env, 2, self):
            self.posX -= 1

    def right(self, env): #accion 3
        if env.accept_action(env, 3, self):
            self.posY += 1

    def suck(self, env): #accion 4
        env.accept_action(env, 4, self)
        self.points += 1 

    def idle(self, env): #accion 5
        env.accept_action(env, 5, self)

    def perspective(self, env): #accion 6
        #el agente solo percibe la casilla en donde está
        #esta accion no quita vida
        return env.mapa[self.posY, self.posX] #envia si la casilla esta sucia (1) o limpia (0)

    def think(self, env): #accion 7
        #esta accion no quita vida

        life_remaining = 0
        while env.life != 0: #mientras tengamos acciones disponibles vamos a pensar
            if self.perspective(self, env) == 1: #si estamos en una casilla sucia la limpiamos
                self.suck(self, env)
            else:
                if env.dirt_rate == 0: #si no hay más suciedad, nos quedamos idles
                    life_remaining = env.life #dato que nos sirve para calcular eficiencia
                    self.idle(self, env)
                else: #si sigue habiendo suciedad nos movemos de forma random para encontrar suciedad
                    self.move_random(self, env)

        return life_remaining

    def move_random(self, env): #elige entre ir arriba abajo derecha izquierda de manera random
        accion= random.randint(0, 3)

        if accion == 0:
            self.up(self, env)
        elif accion == 1:
            self.down(self, env)
        elif accion == 2:
            self.left(self, env)
        elif accion == 3:
            self.right(self, env)