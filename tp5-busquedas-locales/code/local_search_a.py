#modulo que define 3 algoritmos de busqueda local, hill climbing basico, temple simulado y algoritmos geneticos
from n_queens import *

class Node: #clase nodo en la cual vamos a guardar un tablero en state y el valor de la funcion heuristica de ese tablero en value
    state = None
    value = None

#!!!!!!!!!!!!!!!!!!!!!!!!! funciones principales !!!!!!!!!!!!!!!!!!!!!!!!!!

def hillClimbing(tablero): #intenta solucionar el tablero con n reinas a travez de un algoritmo de hill climbing basico, devuelve la solucion encontrada o hasta donde se llegó antes de explorar la maxima cantidad de estados

    current = make_node(tablero)
    max_states = 35 #para que no se quede en un bucle
    while max_states > 0:
        neighbor = best_successor(current.state) #es un node el cual tiene la mejor funcion heuristica entre los posibles proximos pasos
        if neighbor.value >= current.value: #si la mejor opcion es mayor que la que tenemos significa que ya tenemos una solucion local o global osea que la devolvemos
            print("estados recorridos:", max_states)
            print("mejor h encontrado:", current.value)
            return current.state
        current = neighbor #sino seguimos a ver hasta donde nos lleva el estado vecino
        max_states -= 1

    print("estados recorridos:", max_states)
    print("mejor h encontrado:", current.value)
    return current.state


def SimulatedAnnealing(tablero):
    bruh

def GeneticAlgorithm(tablero):
    bruh

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
    hola = 1
    return make_node(tablero_salvado) #devolvemos el tablero con la funcion heuristica menor en forma de nodo

def h(tablero): #funcion heuristica contabiliza la cantidad de pares de reinas amenazadas para un tablero y las devuelve
    h=0
    l_tablero = len(tablero)
    for i in range(0, l_tablero):
        #asumiendo que mi teoria es verdad, nunca miramos para la izquierda

        for j in range(i+1, l_tablero):
            #revisamos horizontal
            if tablero[j] == tablero[i]: #si esto pasa estan en la misma fila, osea se amenazan
                h +=1
            #revisamos diagonales
            elif tablero[j] == tablero[i]+(j-i) or tablero[j] == tablero[i]-(j-i): #j-i representa el aumento para que j sea una diagonal con respecto a i
                h+=1
        
    return h
