#modulo que configura el agente aspiradora
from random import random
from f_matrices import *
import math, random

class Environment: #clase que configura la grilla, sus funciones y atributos
    def __init__(self, sizeX, sizeY, dirt_rate): #atributos de la clase

        self.sizeX= sizeX #numero de columnas de la grilla
        self.sizeY= sizeY #numero de filas de la grilla
        self.mapa= crear_matriz(sizeY, sizeX) #se crea la grilla en la que se mueve el agente
        llenar_matriz(self.mapa, 0) #llenamos la grilla de 0

        self.dirt_count = ensuciar(self.mapa, dirt_rate) #ensuciamos la grilla segun el porcentaje
        self.dirt_rate = calcular_suciedad(self) #este atributo simboliza el porcentaje de suciedad de la grilla en el momento, lo recalculamos porque el dirt_rate verdadero va truncado y cambia

        #generamos la posicion random donde va a empezar nuestro agente
        self.init_posX= random.randint(0, len(self.mapa[0])-1)
        self.init_posY= random.randint(0,len(self.mapa)-1)

        self.life = 1000 #acciones maximas posibles


    def accept_action(self, action, agent): #esta funcion checkea algunas condiciones segun la accion que queremos hacer y quita 1 al numero de acciones que se pueden hacer en total

        if self.life != 0:
            self.life -= 1
            
            if action == 0: #up
                #print("arriba")
                #verificamos que no nos salgamos de los bordes
                if agent.posY - 1 < 0:
                    return False
                else:
                    return True
            elif action == 1: #down
                #print("abajo")
                #verificamos que no nos salgamos de los bordes
                if agent.posY + 1 >= self.sizeY:
                    return False
                else:
                    return True
            elif action == 2: #left
                #print("izquierda")
                #verificamos que no nos salgamos de los bordes
                if agent.posX - 1 < 0:
                    return False
                else:
                    return True
            elif action == 3: #right
                #print("derecha")
                #verificamos que no nos salgamos de los bordes
                if agent.posX + 1 >= self.sizeX:
                    return False
                else:
                    return True
            elif action == 4: #suck
                #print("limpiar")
                #limpiamos el espacio en donde esta el agente, sacamos uno a dirt count y recalculamos el dirt rate actualizandolo
                if self.mapa[agent.posY][agent.posX] != 0:
                    self.mapa[agent.posY][agent.posX]= 0
                    self.dirt_count -= 1
                    self.dirt_rate = calcular_suciedad(self)

                    return True
                else:
                    return False
            elif action == 5: #idle, no hacemos nada
                #print("ociar")
                return True

        else:
            print("NO LIFE LEFT")
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

def ensuciar(mapa, dirt_rate):#ensucia el porcentaje que nosotros queramos (dirt_rate) del mapa de manera random y devuelve la cantidad de casillas sucias

    dirt = 1
    dirt_count = 0
    k=0

    n_casillas_sucias= math.trunc(dirt_rate * len(mapa) * len(mapa[0])) #convertimos el porcentaje en un numero de casillas
    dirt_count= n_casillas_sucias
    while n_casillas_sucias > 0: #ensuciamos hasta quedarnos sin casillas sucias
        i= random.randint(0,len(mapa)-1)
        j= random.randint(0, len(mapa[i])-1)

        if mapa[i][j] == 0: #esto se hace para que cuando la casilla sea repetida se vuelva a ensuciar otra
            mapa[i][j]= dirt
            n_casillas_sucias -= 1
            
    return dirt_count

def calcular_suciedad(env): #calculamos el porcentaje de casillas sucias
    return env.dirt_count / (env.sizeY * env.sizeX)

class Agent: #clase agente que va a ser nuestra aspiradora "inteligente"
    def __init__(self, env): #copia la posicion inicial de la grilla para posicionar nuestro agente en ella, toma un objeto de tipo environment como parametro
        self.posX = env.init_posX 
        self.posY = env.init_posY
        self.points = 0 #puntos asignados por limpiar un lugar

    def up(self, env): #accion 0, toma un objeto de tipo environment como parametro
        #nos fijamos si es posible ir para arriba
        if env.accept_action(0, self):
            self.posY -= 1

    def down(self, env): #accion , toma un objeto de tipo environment como parametro
        #nos fijamos si es posible ir para abajo
        if env.accept_action(1, self):
            self.posY += 1

    def left(self, env): #accion 2, toma un objeto de tipo environment como parametro
        #nos fijamos si es posible ir para la izquierda
        if env.accept_action(2, self):
            self.posX -= 1

    def right(self, env): #accion 3, toma un objeto de tipo environment como parametro
        #nos fijamos si es posible ir para la derecha
        if env.accept_action(3, self):
            self.posX += 1

    def suck(self, env): #accion 4, toma un objeto de tipo environment como parametro
        #limpiamos la casilla en la que estamos porque pensamos que está sucia y agregamos un punto
        if env.accept_action(4, self):
            self.points += 1 

    def idle(self, env): #accion 5, toma un objeto de tipo environment como parametro
        #no hacemos nada pero cuenta como accion
        env.accept_action(5, self)

    def perspective(self, env): #accion 6
        #el agente solo percibe la casilla en donde está
        #esta accion no quita vida
        return env.mapa[self.posY][self.posX] #envia si la casilla esta sucia (1) o limpia (0)

    def think(self, env): #accion 7, toma un objeto de tipo environment como parametro
        #esta accion no quita vida

        while env.life > 0: #mientras tengamos acciones disponibles vamos a seguir pensando

            #imprimimos info
            # print("posicion:","X:", self.posX,"Y:", self.posY)
            # print("vida:", env.life)
            # print("puntos:", self.points)
            # env.print_environment(self)

            if env.dirt_rate == 0: #si no hay más suciedad, nos quedamos idles
                return env.life #dato que nos sirve para calcular eficiencia
            else: #si sigue habiendo suciedad nos movemos de forma random para encontrar suciedad
                self.move_random(env)

            # print("---------")

        return env.life

    def move_random(self, env): #elige entre ir arriba abajo derecha izquierda de manera random
        accion= random.randint(0, 5)

        if accion == 0:
            self.up(env)
        elif accion == 1:
            self.down(env)
        elif accion == 2:
            self.left(env)
        elif accion == 3:
            self.right(env)
        elif accion == 4:
            self.suck(env)
        elif accion == 5:
            self.idle(env)