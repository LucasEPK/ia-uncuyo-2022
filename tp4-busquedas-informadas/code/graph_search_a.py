#modulo que ayuda a encontrar una solucion para el problema del agente informado en un laberinto a travez de grafos y algoritmos de busqueda A*
from math import trunc
from linkedlist import *
from f_matrices import *
from mypriorityqueue import dequeue_priority, enqueue_priorityReverse, isEmpty


#!!!!!!!!!!!!!!!!!!!!!!!!!!!estrucuras de datos!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class Aristas: #clase aristas con dos elementos, porque la aristas son relaciones de 2 vertices
    vi = None
    vj = None
    weight = None #acá vamos a poner el peso de la arista

class Connection:#clase connection que nos sirve para almacenar el peso de pasar de un vertice a otro en el grafo
    value = None
    weight = None

class Vertex: #clase vertex
    value = None #value codificada del vertex (ejemplo la posicion [0,1] de la grilla codificada es 100)
    color = 0 #WHITE es 0
    action = None #accion realizada por el nodo padre para llegar hasta aca
    path_cost = 0 #costo para llegar hasta acá
    parent = None #padre del vertice

    def actions(self, value, graph, filas_grilla): #funcion que dado un value, el grafo y el n de filas de la grilla devuelve las acciones que se pueden hacer desde ese value con sus respectivos pesos en una lista de python
        UP= 0
        LEFT = 1
        DOWN = 2
        RIGHT= 3

        actions = []
        nodo = access(graph[value], 0)

        #acá nos fijamos con quien está conectado nuestro nodo del grafo, y ademas vemos si corresponde a arriba abajo izq o der
        for i in range(1, length(graph[value])): #empezamos desde 1 porque el primer elemento del grafo es su vertex

            action= Connection() #definimos accion como connection porque no es util como notacion
            current_connection = access(graph[value], i) #tomamos los vertices(connection) que estan connectado a nuestro nodo
            if current_connection.value == nodo.value - filas_grilla: #arriba
                action.value = UP
                action.weight = current_connection.weight #peso de realizar esta acción
                actions.append(action)
            elif current_connection.value == nodo.value -1: #izquierda
                action.value = LEFT
                action.weight = current_connection.weight
                actions.append(action)
            elif current_connection.value == nodo.value + filas_grilla: #abajo
                action.value = DOWN
                action.weight = current_connection.weight
                actions.append(action)
            elif current_connection.value == nodo.value +1: #derecha
                action.value = RIGHT
                action.weight = current_connection.weight
                actions.append(action)

        return actions


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Funciones de search!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  

def aStar(graph, v_buscado, v_inicial, frontier, filas_grilla): #funcion de busqueda A* que recibe un grafo (por lista de adyacencia), dos vertex que son el nodo goal y el inicial, una pila con prioridad(frontier) y el numero de filas del laberinto como parametros y devuelve las acciones a seguir en una linkedlist
    GRAY = 1
    BLACK = 2
    nodos_explorados = 0 #esto variable nos sirve para el informe

    if graph[v_inicial.value] == None: #esta excepcion pasa cuando la grilla inicial está encerrada completamente desde el principio sin dejar espacio para moverse
        print("FAILURE: la casilla inicial está encerrada")
        return None
    node = access(graph[v_inicial.value], 0) #tomamos el vertex de la posicion inicial del grafo
    funcion_h = f(node, v_buscado, filas_grilla) #calculamos funcion heuristica

    enqueue_priorityReverse(frontier, v_inicial, funcion_h) #empezamos la cola frontier
    node.color = GRAY #pintamos de gris el nodo a expandir

    while not isEmpty(frontier): #mientras que tengamos nodos que expandir

        node = dequeue_priority(frontier)#sacamos el nodo que está primero en la cola
        node.color = BLACK #pintamos de negro el nodo porque lo vamos a expandir ahora
        nodos_explorados += 1

        if node.value == v_buscado.value: #encontramos la solucion si esto es igual
            print("nodos_explorados:", nodos_explorados)
            return solution(node)

        for action in node.actions(node.value, graph, filas_grilla): #para cada accion que se puede hacer desde el nodo hacemos:
            child = child_node(node, action, graph, filas_grilla, frontier, v_buscado) #determinamos sus nodos hijos
            if child.color != GRAY and child.color != BLACK: #si sus nodos hijos no se han expandido o explorado:
                funcion_h = f(child, v_buscado, filas_grilla) #calculamos funcion heuristica
                enqueue_priorityReverse(frontier, child, funcion_h) #ponemos en la cola a los nodos hijos
                child.color = GRAY #pintamos de gris el nodo a explorar

    print("FAILURE: no se puede llegar a la meta")
    return None


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Funciones auxiliares!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def f(n, p_final, filas):#funcion heuristica, toma como parametros 2 vertex y un numero de filas de la grilla del problema, evalua nodos combinando g(n), el costo de llegar al nodo, y h(n), el costo de llegar desde el nodo hasta el final
    
    return g(n) + manhattan_distance(n, p_final, filas)

def g(n): #costo de llegar al nodo, más que nada para que se entienda
    return n.path_cost

def manhattan_distance(p_inicial, p_final, filas):#calcula el numero minimo de casillas a recorrer del punto inicial al final sin moverse en diagonal y sin tener en cuenta los obstaculos

    p_decodificado= decodificador(p_inicial.value, filas)
    p_inicialY= p_decodificado[0]
    p_inicialX= p_decodificado[1]
    p_decodificado= decodificador(p_final.value, filas)
    p_finalY= p_decodificado[0]
    p_finalX= p_decodificado[1]

    casillas_minimas= abs(p_inicialY - p_finalY)+abs(p_inicialX - p_finalX)

    return casillas_minimas

def decodificador(value, filas): #decodifica el value y retorna su correspondiente x e y en la grilla a travez de una lista de python

    valueY = trunc(value/filas)
    valueX = round((value/filas - valueY)*filas) #hacemos round porque se pierde precision a hacer estos calculos

    value_decodificado = [valueY, valueX]
    return value_decodificado

def child_node(parent, actionC, graph, filas_grilla, frontier, p_final): #funcion que toma como parametros un padre, una accion(connection), el grafo, el n de filas de la grilla, la cola de prioridad frontier y el vertex goal y devuelve el vertex hijo (guardando padre y accion) al ejecutar la accion desde el padre

    GRAY = 1
    BLACK = 2

    weight = actionC.weight
    child = result(parent, actionC.value, graph, filas_grilla)

    if child.color != GRAY and child.color != BLACK: #no se ha explorado el nodo

        child.parent = parent
        child.action = actionC.value
        child.path_cost = parent.path_cost + weight
    elif child.color == GRAY:#si pasa esto significa que llegamos a un nodo que todavia no se expande pero hemos llegado a travez de una conexion, tenemos que fijarnos si el costo para llegar a el que acabamos de encontrar es menor al que encontramos

        funcion_h = f(child, p_final, filas_grilla) #funcion heuristica del child con el peso de cuando se habia llegado a ese nodo en el pasado

        child_copy = Vertex() #child_copy es el child pero con una nueva heuristica calculada con el nuevo costo del camino que acabamos de llegar
        child_copy.value = child.value
        child_copy.path_cost = parent.path_cost + weight
        funcion_h_nueva = f(child_copy, p_final, filas_grilla)

        if funcion_h > funcion_h_nueva:
        
            delete(frontier, child)

            child.parent = parent
            child.action = actionC.value
            child.path_cost = parent.path_cost + weight

            funcion_h=f(child, p_final, filas_grilla) #calculamos funcion heuristica (que va a ser igual a la nueva)

            enqueue_priorityReverse(frontier, child, funcion_h)

    return child

def result(node, action, graph, filas_grilla): #funcion que recibe un vertex, una acción, el grafo y el n de filas de la grilla y retorna el vertex al ejecutar esa accion en el nodo padre

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

def createGraph(l_vertices, l_aristas): #creamos el grafo como lista de adyacencia y lo devolvemos con return
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

            add(graph[current_arista.value.vi.value], current_arista.value.vi) #en la primera posicion de cada lista del grafo dejamos el vertex que representa ese vertice
        else:
            insert(graph[current_arista.value.vi.value], connection, 1) #esto hace que el vertex se mantenga en primera posicion
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
