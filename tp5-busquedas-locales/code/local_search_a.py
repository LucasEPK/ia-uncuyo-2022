#modulo que define 3 algoritmos de busqueda local, hill climbing basico, temple simulado y algoritmos geneticos

from f_matrices import crear_matriz
import random, math

class Node: #clase nodo en la cual vamos a guardar un tablero en state y el valor de la funcion heuristica de ese tablero en value
    state = None
    value = None

#!!!!!!!!!!!!!!!!!!!!!!!!! funciones principales !!!!!!!!!!!!!!!!!!!!!!!!!!

def hillClimbing(tablero): #intenta solucionar el tablero con n reinas a travez de un algoritmo de hill climbing basico, devuelve la solucion encontrada o hasta donde se llegó antes de explorar la maxima cantidad de estados

    current = make_node(tablero)
    max_states = 35 #para que no se quede en un bucle
    estados_recorridos = 0
    while max_states > 0:
        neighbor = best_successor(current.state) #es un node el cual tiene la mejor funcion heuristica entre los posibles proximos pasos
        print("h:", neighbor.value)
        if neighbor.value >= current.value: #si la mejor opcion es mayor que la que tenemos significa que ya tenemos una solucion local o global osea que la devolvemos
            print("estados recorridos:", estados_recorridos)
            print("mejor h encontrado:", current.value)
            if current.value == 0:
                print("SOLUCION OPTIMA")
            return current.state
        current = neighbor #sino seguimos a ver hasta donde nos lleva el estado vecino
        max_states -= 1
        estados_recorridos += 1

    print("estados recorridos:", estados_recorridos)
    print("mejor h encontrado:", current.value)
    if current.value == 0:
        print("SOLUCION OPTIMA")
    return current.state


def SimulatedAnnealing(tablero): #intenta resolver el tablero con n reinas a travez de un algoritmo de temple simulado, devuelve la solucion encontrada o hasta donde se llegó antes de explorar la maxima cantidad de estados

    current = make_node(tablero)
    T = 10
    max_states= 5000
    estados_recorridos = 0
    while max_states > 0:
        neighbor = random_successor(current.state) #es un node en el cual se elige un tablero random donde se a movido solo 1 reina con respecto al tablero original
        print("h:", neighbor.value)
        estados_recorridos += 1
        if neighbor.value == 0:
            print("SOLUCION OPTIMA ENCONTRADA")
            print("estados recorridos:", estados_recorridos)
            print("mejor h encontrado:", neighbor.value)
            return neighbor.state

        deltaE= (current.value - neighbor.value)
        probabilityE = 1/math.exp((-deltaE*100)/T)
        #print(probabilityE)
        random_n = random.random() #numero random entre 1(no incluido) y 0 
        if deltaE > 0:
            current = neighbor
        elif random_n <= probabilityE:
            current = neighbor

        if T > 1:
            T -= 1

        max_states -= 1
        


    print("estados recorridos:", estados_recorridos)
    print("mejor h encontrado:", current.value)
    return current.state

def geneticAlgorithm(population): #population es un array de python con k tableros, a travez del algoritmo genetico nos devuelve la mejor solucion encontrada en el limite de estados dado

    max_states = 10000 #limite de estados
    estados_recorridos = 0
    size=len(population)
    max_fitness= calcular_fitness_max(population[0])
    while max_states > 0:
        print("h:", fitness(best_fitness(population)))
        new_population = []
        estados_recorridos += 1
        for i in range(size): #creamos una nueva poblacion seleccionado pares de individuos y tomando el hijo como nuevo miembro de la nueva poblacion, la nueva poblacion va a tener el mismo numero de individuos
            #seleccionamos 2 padres
            selection = random_selection(population)
            x= selection[0]
            y= selection[1]

            child = reproduce(x, y)

            if 1 == random.randint(1,100): #pequeña chance de que el niño mute
                child = mutate(child)
            
            if fitness(child) == max_fitness:
                print("estados recorridos:", estados_recorridos)
                print("SOLUCION OPTIMA ENCONTRADA")
                print("mejor fitness encontrado:", max_fitness)
                return child
                
            new_population.append(child)   
        population = new_population

        max_states -= 1

    print("estados recorridos:", estados_recorridos)
    return best_fitness(population)

#!!!!!!!!!!!!!!!!!!!!!! funciones auxiliares!!!!!!!!!!!!!!!!!!!!!!!!!!

def make_node(tablero): #funcion general que genera un nodo a travez de un tablero dando como state el tablero y como value la funcion heuristica de ese tablero
    node = Node()
    node.state = tablero
    node.value = h(tablero)
    return node

def best_successor(tablero): #segun el tablero otorgado devuelve el tablero con menor valor de h que encuentra despues de mover una reina en alguna columna
    size = len(tablero)
    matriz_tablero = crear_matriz(size, size) #creamos esta matriz
    min_value= 100000 #!ojo que con muchas reinas esto podria dejar de funcionar!

    for i in range(size):
        for j in range(size):
            
            #creamos un tablero en donde la reina de la columna j se mueve a la fila (size-1)-i (esto se hace para que las filas se lean de abajo para arriba)
            tablero_M= tablero.copy()
            tablero_M[j] = (size-1)-i
            if tablero_M[j] != tablero[j]: #esto verifica que las posiciones en la que ya estan las reinas no se calculen
                h1 = h(tablero_M) #calculamos funcion heuristica
                matriz_tablero[i][j] = h1
                if h1 < min_value: #como buscamos el que tiene menos amenazas, buscamos el menor valor y copiamos el tablero
                    min_value = h1
                    tablero_salvado = tablero_M.copy()

    return make_node(tablero_salvado) #devolvemos el tablero con la funcion heuristica menor en forma de nodo

def random_successor(tablero): #segun el tablero otorgado devuelve un tablero random que encuentra despues de mover una reina en alguna columna
    
    size = len(tablero)
    posicion_ocupada = True
    while posicion_ocupada: #simulacion de un do while el cual se ocupa de revisar que no estemos elegiendo una posicion en la cual ya se encuentra una reina
        #elegimos de manera random a la posicion en la cual se va a mover una reina
        i= random.randint(0, size-1)
        j= random.randint(0, size-1)
            
        #creamos un tablero en donde la reina de la columna j se mueve a la fila (size-1)-i (esto se hace para que las filas se lean de abajo para arriba)
        tablero_M= tablero.copy()
        tablero_M[j] = (size-1)-i

        if tablero_M[j] != tablero[j]:
            posicion_ocupada = False


    return make_node(tablero_M) #devolvemos un nodo con un tablero random


def random_selection(population): #selecciona de manera random (aunque si tienen mejor fitness tienen más chances) un individuo de la poblacion
    k= len(population)
    fitness_l= []
    for pos in range(k):#calculamos el fitness de cada individuo de la poblacion y lo insertamos en una lista
        fitness_l.append(fitness(population[pos]))

    l_probability= probability_F(fitness_l) #calculamos las probabilidades segun el fitness

    seleccionado = random.choices(population, weights= l_probability, k=2)
    return seleccionado

def reproduce(x, y): #toma como parametro dos arreglos x e y, los divide en alguna parte c y toma la parte antes de c de x y la despues de c de y y las une para formar el hijo(tablero)

    n= len(x)
    c= random.randint(1, n-1)
    child = x[:c]+y[c:]
    return child

def h(tablero): #funcion heuristica contabiliza la cantidad de pares de reinas amenazadas para un tablero y las devuelve
    h=0
    l_tablero = len(tablero)
    for i in range(0, l_tablero):

        for j in range(i+1, l_tablero):
            #revisamos horizontal
            if tablero[j] == tablero[i]: #si esto pasa estan en la misma fila, osea se amenazan
                h +=1
            #revisamos diagonales
            elif tablero[j] == tablero[i]+(j-i) or tablero[j] == tablero[i]-(j-i): #j-i representa el aumento para que j sea una diagonal con respecto a i
                h+=1
        
    return h

def fitness(tablero):#funcion fitness que al recibir un tablero devuelve el numero de pares de reina no atacantes
    size= len(tablero)
    fitness = 0

    for pos in range(size):
        atacantes = 0
        for j in range(pos+1, size):#calculamos las reinas que atacan a una reina
            #revisamos horizontal
            if tablero[j] == tablero[pos]: #si esto pasa estan en la misma fila, osea se amenazan
                atacantes +=1
            #revisamos diagonales
            elif tablero[j] == tablero[pos]+(j-pos) or tablero[j] == tablero[pos]-(j-pos): #j-pos representa el aumento para que j sea una diagonal con respecto a pos
                atacantes +=1

        #calculamos los pares de reinas que no atacan restandole a cada par de reinas que tiene una reina a su derecha las reinas que si la atacan
        fitness = fitness + (size-(pos+1))-atacantes

    return fitness #devolvemos el numero de pares de reinas totales que no atacan

def probability_F(l_fitness): #teniendo un array de fitness devuelve un array de probabilidades
    len_fitness = len(l_fitness)
    l_probability = []

    #hacemos calculos para poder sacar el k que multiplicado por un fitness nos da un porcentaje
    suma= 0
    for i in range(len_fitness):
        suma = suma + l_fitness[i]

    k=100/suma

    for i in range(len_fitness):
        l_probability.append(round(k * l_fitness[i]))

    return l_probability

def mutate(tablero): #cambiamos el lugar de una reina random a un lugar random
    len_tablero = len(tablero)
    ri=random.randint(0, len_tablero-1)
    tablero[ri]= random.randint(0, len_tablero-1)
    return tablero

def best_fitness(population): #encuentra el individuo con mayor fitness en una poblacion y lo devuelve
    len_population = len(population)
    mayor_fitness = 0
    for pos in range(0, len_population):
        current_fitness = fitness(population[pos])
        if current_fitness > mayor_fitness:
            mayor_fitness = current_fitness
            mayor_t_fitness = population[pos]

    print("mayor fitness:", mayor_fitness)
    return mayor_t_fitness

def calcular_fitness_max(tablero):
    size = len(tablero)
    fitness_max = 0
    for i in range(size):
        fitness_max += (size-1)-i

    return fitness_max