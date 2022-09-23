#modulo que ayuda a encontrar una solucion para el problema del agente no informado en un laberinto a travez de grafos y algoritmos de busqueda como bfs dfs ...
from math import trunc
from linkedlist import *
from f_matrices import *
from mypriorityqueue import dequeue_priority, enqueue_priorityReverse
from myqueue import *


#!!!!!!!!!!!!!!!!!!!!!!!!!!!estrucuras de datos!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class Aristas: #clase aristas con dos elementos, porque la aristas son relaciones de 2 vertices
    vi = None
    vj = None
    weight = None #acá vamos a poner un vertex

class Connection:
    value = None
    weight = None

class Vertex: #vertex para dfs
    state= None
    value = None #value encodeada del vertex (ejemplo la posicion [0,1] de la grilla encodeada es 100)
    color = 0 #WHITE es 0
    action = None #accion realizada por el nodo padre para llegar hasta aca
    path_cost = 0 #costo para llegar hasta acá
    parent = None #padre del vertice

    def actions(self, value, graph, filas_grilla): #funcion que dado un value, el grafo y el n de filas de la grilla devuelve las acciones que se pueden hacer desde ese value en un array
        UP= 0
        LEFT = 1
        DOWN = 2
        RIGHT= 3

        actions = []

        #acá nos fijamos con quien está conectado nuestro nodo del grafo, y ademas vemos si corresponde a arriba abajo izq o der
        for i in range(1, length(graph[value])): #empezamos desde 1 porque el primer elemento del grafo es su vertex
            if access(graph[value], i) == access(graph[value], 0).value -filas_grilla:
                actions.append(UP)
            elif access(graph[value], i) == access(graph[value], 0).value -1:
                actions.append(LEFT)
            elif access(graph[value], i) == access(graph[value], 0).value +filas_grilla:
                actions.append(DOWN)
            elif access(graph[value], i) == access(graph[value], 0).value +1:
                actions.append(RIGHT)

        return actions

    def actionsUS(self, value, graph, filas_grilla): #funcion que dado un value, el grafo y el n de filas de la grilla devuelve las acciones que se pueden hacer desde ese value en un array
        UP= 0
        LEFT = 1
        DOWN = 2
        RIGHT= 3

        actions = []

        #acá nos fijamos con quien está conectado nuestro nodo del grafo, y ademas vemos si corresponde a arriba abajo izq o der
        for i in range(1, length(graph[value])): #empezamos desde 1 porque el primer elemento del grafo es su vertex
            action= Connection()
            current_connection = access(graph[value], i)
            if current_connection.value == access(graph[value], 0).value -filas_grilla: #up
                action.value = UP
                action.weight = current_connection.weight
                actions.append(action)
            elif current_connection.value == access(graph[value], 0).value -1: #left
                action.value = LEFT
                action.weight = current_connection.weight
                actions.append(action)
            elif current_connection.value == access(graph[value], 0).value +filas_grilla: #down
                action.value = DOWN
                action.weight = current_connection.weight
                actions.append(action)
            elif current_connection.value == access(graph[value], 0).value +1: #right
                action.value = RIGHT
                action.weight = current_connection.weight
                actions.append(action)

        return actions


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Funciones de search!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def bfs(graph, v_buscado, v_inicial, frontier, filas_grilla): #funcion bfs que recibe un grafo (por matriz de adyacencia) 2 vertex 1 cola como parametros y el numero de filas en la grilla y que devuelve las acciones a seguir
    GRAY = 1
    BLACK = 2

    if graph[v_inicial.value] == None: #esta excepcion pasa cuando la grilla inicial está encerrada completamente desde el principio sin dejar espacio para moverse
        print("FAILURE: la casilla inicial está encerrada")
        return None
    node = access(graph[v_inicial.value], 0) #tomamos el vertex de la posicion inicial del grafo

    if node.value == v_buscado.value: #si la solucion es el mismo nodo inicial se devuelve la solucion con ese nodo
        return solution(node)
    
    enqueue(frontier, v_inicial) #empezamos la cola frontier
    node.color = GRAY #pintamos de gris el nodo a expandir

    while not isEmpty(frontier):

        node = dequeue(frontier)#sacamos el nodo que está primero en la cola
        node.color = BLACK #pintamos de negro el nodo porque lo vamos a expandir ahora

        for action in node.actions(node.value, graph, filas_grilla): #para cada accion que se puede hacer desde el nodo hacemos:
            child = child_node(node, action, graph, filas_grilla) #determinamos sus nodos hijos
            if child.color != GRAY and child.color != BLACK: #si sus nodos hijos no se han expandido o explorado:
                if child.value == v_buscado.value: #encontramos la solucion si esto es igual
                    return solution(child)

                enqueue(frontier, child) #ponemos en la cola a los nodos hijos
                child.color = GRAY #pintamos de gris el nodo a explorar

    print("FAILURE: no se puede llegar a la meta")
    return None


def dfs_limited(graph, v_buscado, v_inicial, filas_grilla, limite): #funcion dfs limitado que recibe un grafo (por matriz de adyacencia) y un vertex como parametros y que devuelve las acciones a seguir

    return recursive_dls(v_inicial, v_buscado, filas_grilla, graph, limite)

def recursive_dls(v_inicial, v_buscado, filas_grilla, graph, limit):
    GRAY = 1
    BLACK = 2

    cutoff = 0
    failure = 1

    node = access(graph[v_inicial.value], 0)
    node.color = GRAY
    if node.value == v_buscado.value: #si la solucion es el mismo nodo inicial se devuelve la solucion con ese nodo
        return solution(node)
    elif limit == 0:
        #print("Cutoff")
        return cutoff
    else:
        cutoff_occurred = False

        for action in node.actions(node.value, graph, filas_grilla): #para cada accion que se puede hacer desde el nodo hacemos:
            child = child_node(node, action, graph, filas_grilla) #determinamos sus nodos hijos
            if child.color != GRAY and child.color != BLACK:
                result = recursive_dls(child, v_buscado, filas_grilla, graph, limit-1)

                child.color = BLACK

                if result == 0:
                    cutoff_occurred = True
                elif result != failure:
                    #print("result:", result)
                    return result
        if cutoff_occurred:
            #print("Cutoff")
            return cutoff
        else:
            #print("Failure")
            return failure
        

def uniform_cost_search(graph, v_buscado, v_inicial, frontier, filas_grilla): #funcion de busqueda uniforme que recibe un grafo (por matriz de adyacencia) y un vertex como parametros y que devuelve las acciones a seguir
    GRAY = 1
    BLACK = 2

    if graph[v_inicial.value] == None: #esta excepcion pasa cuando la grilla inicial está encerrada completamente desde el principio sin dejar espacio para moverse
        print("FAILURE: la casilla inicial está encerrada")
        return None
    node = access(graph[v_inicial.value], 0) #tomamos el vertex de la posicion inicial del grafo
    
    enqueue_priorityReverse(frontier, v_inicial, 0) #empezamos la cola frontier
    node.color = GRAY #pintamos de gris el nodo a expandir

    while not isEmpty(frontier):

        node = dequeue_priority(frontier)#sacamos el nodo que está primero en la cola
        node.color = BLACK #pintamos de negro el nodo porque lo vamos a expandir ahora

        if node.value == v_buscado.value: #encontramos la solucion si esto es igual
            return solution(node)

        for action in node.actionsUS(node.value, graph, filas_grilla): #para cada accion que se puede hacer desde el nodo hacemos:
            child = child_nodeUS(node, action, graph, filas_grilla, frontier) #determinamos sus nodos hijos
            if child.color != GRAY and child.color != BLACK: #si sus nodos hijos no se han expandido o explorado:
                enqueue_priorityReverse(frontier, child, child.path_cost) #ponemos en la cola a los nodos hijos
                child.color = GRAY #pintamos de gris el nodo a explorar

    print("FAILURE: no se puede llegar a la meta")
    return None


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Funciones auxiliares!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def child_node(parent, action, graph, filas_grilla): #funcion que toma como parametros un padre, una accion, el grafo y el n de filas de la grilla y devuelve el vertex hijo del vertex padre (guardando padre y accion) al ejecutar la accion
    GRAY = 1
    BLACK = 2

    child = result(parent, action, graph, filas_grilla)
    if child.color != GRAY and child.color != BLACK:
        child.parent = parent
        child.action = action
        child.path_cost = parent.path_cost + 1 #+1 porque el costo de la path son todos iguales

    return child


def child_nodeUS(parent, actionC, graph, filas_grilla, frontier): #funcion que toma como parametros un padre, una accion, el grafo y el n de filas de la grilla y devuelve el vertex hijo del vertex padre (guardando padre y accion) al ejecutar la accion
    GRAY = 1
    BLACK = 2

    weight = actionC.weight
    child = result(parent, actionC.value, graph, filas_grilla)
    if child.color != GRAY and child.color != BLACK:

        child.parent = parent
        child.action = actionC.value
        child.path_cost = parent.path_cost + weight
    elif child.color == GRAY and child.path_cost > parent.path_cost + weight:
        delete(frontier, child)

        child.parent = parent
        child.action = actionC.value
        child.path_cost = parent.path_cost + weight

        enqueue_priorityReverse(frontier, child, child.path_cost)

        

    return child

def result(node, action, graph, filas_grilla): #funcion que recibe un vertex, una acción, el grafo y el n de filas de la grilla y retorna el vertex del vertex padre al ejecutar esa accion en el nodo padre

    UP= 0
    LEFT = 1
    DOWN = 2
    RIGHT= 3

    
    if action == UP:
        value = node.value - filas_grilla
    elif action == LEFT:
        value = node.value - 1
    elif action == DOWN:
        value = node.value + filas_grilla
    elif action == RIGHT:
        value = node.value + 1

    new_node = access(graph[value], 0)

    return new_node

def solution(node): #desde el nodo que buscabamos devolvemos el camino que se hizo para encontrarlo a travez del atributo parent y action

    current_node = node
    solution = LinkedList()

    while current_node.parent != None:
        add(solution, current_node.action)
        current_node = current_node.parent

    return solution

# !!!!!!!!!!!!!!!!!!!!!!!!!!! Funciones de creacion de estructuras !!!!!!!!!!!!!!!!!!!!!!!!!!


def createGraph(l_vertices, l_aristas): #creamos el grafo y lo devolvemos con return
    #creamos el grafo como lista de adyacencia

    #creamos un array con longitud igual a el numero de vertices
    graph = []
    n_vertices = length(l_vertices)
    for i in range(n_vertices):
        graph.append(None)

    n_aristas = length(l_aristas) #esto es para reccorer la lista eficientemente
    current_arista = l_aristas.head
    for j in range(n_aristas): #recorremos la lista de aristas y agregamos el segundo vertice de la arista a la lista del primer vertice en el grafo

        if graph[current_arista.value.vi] == None: #lo declaramos como linkedlist si el grafo en esta posicion no se ha inicializado todavia
            graph[current_arista.value.vi] = LinkedList()

            add(graph[current_arista.value.vi], current_arista.value.vj)# añadimos su segundo elemento a la linkedlist del grafo en la posicion del vertice

            add(graph[current_arista.value.vi], current_arista.value.weight) #esto nos deja el vertice que estabamos analizando siempre en el head
        else:
            insert(graph[current_arista.value.vi], current_arista.value.vj, 1) #esto nos deja el vertex en primera posicion
        current_arista = current_arista.nextNode
             
    return graph #devolvemos el grafo

def createGraphUS(l_vertices, l_aristas): #creamos el grafo y lo devolvemos con return
    #creamos el grafo como lista de adyacencia

    #creamos un array con longitud igual a el numero de vertices
    graph = []
    n_vertices = length(l_vertices)
    for i in range(n_vertices):
        graph.append(None)

    n_aristas = length(l_aristas) #esto es para reccorer la lista eficientemente
    current_arista = l_aristas.head
    for j in range(n_aristas): #recorremos la lista de aristas y agregamos el segundo vertice de la arista a la lista del primer vertice en el grafo
        connection = Connection()
        connection.value = current_arista.value.vj.value
        connection.weight = current_arista.value.weight
        if graph[current_arista.value.vi.value] == None: #lo declaramos como linkedlist si el grafo en esta posicion no se ha inicializado todavia
            graph[current_arista.value.vi.value] = LinkedList() #el doble value es porque son vertex

            add(graph[current_arista.value.vi.value], connection)# añadimos su segundo elemento a la linkedlist del grafo en la posicion del vertice

            add(graph[current_arista.value.vi.value], current_arista.value.vi) #esto nos deja el vertice que estabamos analizando siempre en el head
        else:
            insert(graph[current_arista.value.vi.value], connection, 1) #esto nos deja el vertex en primera posicion
        current_arista = current_arista.nextNode
             
    return graph #devolvemos el grafo

def createVertex(value): #crea un objeto de la clase vertex con la value especificada en el parametro y lo retorna
    vertex = Vertex()
    vertex.value = value
    return vertex

def createWeightedArista(vertice1, vertice2, peso): #crea una Arista() que tiene como vi a vertice1, como vj a vertice2, como weigth a peso y la retorna
    arista = Aristas()
    arista.vi = vertice1
    arista.vj = vertice2
    arista.weight = peso
    return arista


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! funciones de impresion !!!!!!!!!!!!!!!!!!!!!!!!!!!!
