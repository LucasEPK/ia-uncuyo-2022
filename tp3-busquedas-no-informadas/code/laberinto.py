#modulo que configura el agente que se mueve en el laberinto
from random import random
from f_matrices import *
from linkedlist import add, LinkedList
from graph_search_a import *
import math, random

class Environment: #clase que configura la grilla, sus funciones y atributos
    def __init__(self, sizeX, sizeY, p_inicialX, p_inicialY, p_finalX, p_finalY, obstacle_rate): #atributos de la clase (obstacle_rate tiene que estar escrito no como porcentaje sino que como por ejemplo: 100%=1 50%=0.5)

        self.grilla= crear_matriz(sizeY, sizeX) #se crea la grilla en la que se mueve el agente
        llenar_matriz(self.grilla, 0) #llenamos la grilla de 0

        #Punto donde empieza el agente
        self.p_inicialX = p_inicialX
        self.p_inicialY = p_inicialY
        self.grilla[p_inicialY][p_inicialX] = 2 #representamos el agente con un 2 en la grilla

        #punto donde tiene que llegar el agente
        self.p_finalX = p_finalX
        self.p_finalY = p_finalY

        self.grilla[p_finalY][p_finalX] = 3 #representamos al punto final con un 3 en la grilla


        self.obstacle_rate = insertar_obstaculos(self.grilla, obstacle_rate) #metemos obstaculos en la grilla segun el porcentaje

def insertar_obstaculos(mapa, obstacle_rate):#inserta obstaculos del porcentaje que nosotros queramos (obstacle_rate) del mapa de manera random

    obstaculo = 1
    
    n_casillas_obstaculos= math.trunc(obstacle_rate * len(mapa) * len(mapa[0])) #convertimos el porcentaje en un numero de casillas
    while n_casillas_obstaculos > 0: #insertamos obstaculos hasta quedarnos sin casillas a las cuales habia que asignarles obstaculos
        i= random.randint(0,len(mapa)-1)
        j= random.randint(0, len(mapa[i])-1)

        if mapa[i][j] == 0: #esto se hace para que cuando la casilla sea repetida o sea una casilla especial se vuelva a insertar_obstaculos otra vez
            mapa[i][j]= obstaculo
            n_casillas_obstaculos -= 1
            
    return

class Agent: #clase agente que va a ser quien resuelva el laberinto
    def __init__(self, env): #copia la posicion inicial de la grilla para posicionar nuestro agente en ella, toma un objeto de tipo environment como parametro
        self.posX = env.p_inicialX 
        self.posY = env.p_inicialY

    def solve_by_bfs(self, env): #resolvemos el problema que nos da el environment mediante bfs
        print_grilla(env.grilla)
        print("Guia: obstaculo=1, inicio=2, final=3, casilla libre=0")
        filas_grilla = len(env.grilla)

        grafo = crear_grafo_segun_grilla(env.grilla)
        p_final_codificado = createVertex((env.p_finalY)*filas_grilla + env.p_finalX)
        p_inicial_codificado = createVertex((self.posY)*filas_grilla + self.posX)
        frontier = LinkedList() #cola que nos sirve en bfs
        solution = bfs(grafo, p_final_codificado, p_inicial_codificado, frontier, filas_grilla) #bfs nos va a dar las acciones a realizar
        
        printSolution(solution, env.grilla, self.posY, self.posX)
        return 0

    def solve_by_US(self, env): #resolvemos el problema que nos da el environment mediante uniform search
        print_grilla(env.grilla)
        print("Guia: obstaculo=1, inicio=2, final=3, casilla libre=0")
        filas_grilla = len(env.grilla)

        grafo = crear_grafo_segun_grillaUS(env.grilla)
        p_final_codificado = createVertex((env.p_finalY)*filas_grilla + env.p_finalX)
        p_inicial_codificado = createVertex((self.posY)*filas_grilla + self.posX)
        frontier = LinkedList() #cola que nos sirve en uniform cost search
        solution = uniform_cost_search(grafo, p_final_codificado, p_inicial_codificado, frontier, filas_grilla) #uniform_cost_search nos va a dar las acciones a realizar
        
        printSolution(solution, env.grilla, self.posY, self.posX)
        return 0

    def solve_by_dfsL(self, env): #resolvemos el problema que nos da el environment mediante limited dfs
        print_grilla(env.grilla)
        print("Guia: obstaculo=1, inicio=2, final=3, casilla libre=0")
        filas_grilla = len(env.grilla)

        grafo = crear_grafo_segun_grilla(env.grilla)
        p_final_codificado = createVertex((env.p_finalY)*filas_grilla + env.p_finalX)
        p_inicial_codificado = createVertex((self.posY)*filas_grilla + self.posX)
        limite = trunc(len(env.grilla)+len(env.grilla[0])/2) #tomamos el limite de posiciones que no podemos desplazar desde el principio como la suma de las filas y las columnas dividido 2
        solution = dfs_limited(grafo, p_final_codificado, p_inicial_codificado, filas_grilla, limite) #dfs_limited nos va a dar las acciones a realizar
        
        printSolution(solution, env.grilla, self.posY, self.posX)
        return 0

def crear_grafo_segun_grilla(grilla): #crea un grafo con la codificacion de que cada vertice tiene un numero del 0 al 9999 (ya que la grilla va a ser de 100x100 en nuestro caso en particular)

    filas = len(grilla)
    columnas = len(grilla[0])
    casillas_totales = filas*columnas

    #creamos una lista de vertices cada uno con un numero del 0 al 9999
    l_vertices= LinkedList()
    for i in range(casillas_totales-1,-1, -1):
        add(l_vertices, i)

    #creamos una lista de aristas que va a conectar todos los cuadrados de la grilla con su cuadrados adyacentes (menos los diagonales)
    l_aristas= LinkedList()
    for i in range(filas):
        for j in range(columnas):

            if grilla[i][j] != 1: #revisa que no sea una casilla obstaculo el vertice actual
                #calculamos el valor de los vertices segun la codificacion
                vertice_actual = i*filas+j
                vertice_arriba = (i-1)*filas+j
                vertice_abajo = (i+1)*filas+j
                vertice_izq = i*filas + (j-1)
                vertice_der = i*filas + (j+1)

                vertex = createVertex(vertice_actual)
                #acá revisamos condiciones de los bordes, porque en los bordes hay menos opciones de aristas y además revisamos que los vertices de al lado no sean obstaculos
                if i > 0 and grilla[i-1][j] != 1:
                    add(l_aristas, createWeightedArista(vertice_actual, vertice_arriba, vertex))
                if i < filas-1 and grilla[i+1][j] != 1:
                    add(l_aristas, createWeightedArista(vertice_actual, vertice_abajo, vertex))
                if j > 0 and grilla[i][j-1] != 1:
                    add(l_aristas, createWeightedArista(vertice_actual, vertice_izq, vertex))
                if j < columnas-1 and grilla[i][j+1] != 1:
                    add(l_aristas, createWeightedArista(vertice_actual, vertice_der, vertex))


    return createGraph(l_vertices, l_aristas)

def crear_grafo_segun_grillaUS(grilla): #crea un grafo modificado para uniform search que necesita aristas con peso con la codificacion de que cada vertice tiene un numero del 0 al 9999 (ya que la grilla va a ser de 100x100 en nuestro caso en particular)

    filas = len(grilla)
    columnas = len(grilla[0])
    casillas_totales = filas*columnas

    #creamos una lista de vertices cada uno con un numero del 0 al 9999
    l_vertices= LinkedList()
    for i in range(casillas_totales-1,-1, -1):
        add(l_vertices, i)

    #creamos una lista de aristas que va a conectar todos los cuadrados de la grilla con su cuadrados adyacentes (menos los diagonales)
    l_aristas= LinkedList()
    for i in range(filas):
        for j in range(columnas):

            if grilla[i][j] != 1: #revisa que no sea una casilla obstaculo el vertice actual
                #calculamos el valor de los vertices segun la codificacion
                vertex_actual = createVertex(i*filas+j)
                vertex_arriba = createVertex((i-1)*filas+j)
                vertex_abajo = createVertex((i+1)*filas+j)
                vertex_izq = createVertex(i*filas + (j-1))
                vertex_der = createVertex(i*filas + (j+1))

                weight = 1 #hardcodeado en 1 porque por ahora tenemos mismo peso para todas las conexiones
                
                #acá revisamos condiciones de los bordes, porque en los bordes hay menos opciones de aristas y además revisamos que los vertices de al lado no sean obstaculos
                if i > 0 and grilla[i-1][j] != 1:
                    add(l_aristas, createWeightedArista(vertex_actual, vertex_arriba, weight))
                if i < filas-1 and grilla[i+1][j] != 1:
                    add(l_aristas, createWeightedArista(vertex_actual, vertex_abajo, weight))
                if j > 0 and grilla[i][j-1] != 1:
                    add(l_aristas, createWeightedArista(vertex_actual, vertex_izq, weight))
                if j < columnas-1 and grilla[i][j+1] != 1:
                    add(l_aristas, createWeightedArista(vertex_actual, vertex_der, weight))


    return createGraphUS(l_vertices, l_aristas)

def printSolutionWords(solution): #funcion que imprime las acciones a realizar desde el principio para llegar a la resolucion
    UP= 0
    LEFT = 1
    DOWN = 2
    RIGHT= 3

    if solution == None or solution == 0 or solution == 1:
        print("No tiene solución")
        return None

    currentNode = solution.head
    for i in range(length(solution)):

        if currentNode.value == UP:
            print("up", end=', ')
        elif currentNode.value == LEFT:
            print("left", end=', ')
        elif currentNode.value == DOWN:
            print("down", end=', ')
        elif currentNode.value == RIGHT:
            print("right", end=', ')

        currentNode = currentNode.nextNode

    print("")

def printSolution(solution, grilla, p_inicialY, p_inicialX): #funcion que imprime las acciones a realizar desde el principio para llegar a la resolucion
    UP= 0
    LEFT = 1
    DOWN = 2
    RIGHT= 3

    if solution == None or solution == 1:
        print("No tiene solución")
        return None
    elif solution == 0:
        print("Se corta antes de llegar a la solución")
        return None

    currentNode = solution.head
    anteriorY= p_inicialY
    anteriorX= p_inicialX
    print("[", p_inicialX, ",", p_inicialY, "]")
    for i in range(length(solution)):

        if currentNode.value == UP:
            #grilla[anteriorY][anteriorX]= 0
            p_resultadoY= anteriorY - 1
            p_resultadoX= anteriorX
            #grilla[p_resultadoY][p_resultadoX]= 2
            print("up: [", p_resultadoX, ",", p_resultadoY, "]")
        elif currentNode.value == LEFT:
            #grilla[anteriorY][anteriorX]= 0
            p_resultadoY= anteriorY
            p_resultadoX= anteriorX - 1
            #grilla[p_resultadoY][p_resultadoX]= 2
            print("left: [", p_resultadoX, ",", p_resultadoY, "]")
        elif currentNode.value == DOWN:
            #grilla[anteriorY][anteriorX]= 0
            p_resultadoY= anteriorY + 1
            p_resultadoX= anteriorX
            #grilla[p_resultadoY][p_resultadoX]= 2
            print("down: [", p_resultadoX, ",", p_resultadoY, "]")
        elif currentNode.value == RIGHT:
            #grilla[anteriorY][anteriorX]= 0
            p_resultadoY= anteriorY
            p_resultadoX= anteriorX + 1
            #grilla[p_resultadoY][p_resultadoX]= 2
            print("right: [", p_resultadoX, ",", p_resultadoY, "]")

        #print_grilla(grilla)

        anteriorY= p_resultadoY
        anteriorX= p_resultadoX
        currentNode = currentNode.nextNode

def print_grilla(matriz): #imprime la grilla en pantalla

    filas = len(matriz)
    for i in range(filas):
        columnas = len(matriz[i])
        for j in range(columnas):
            if j == 0:
                print(i, ":  ", end='')
            print(matriz[i][j], end='')
        print()