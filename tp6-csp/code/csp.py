#modulo que define 2 algoritmos csp, backtracking y encadenamiento hacia delante
import copy
class CSP:
    variables= None

class Variables:
    value = None
    domain = None

def forward_checking_search(csp): #funcion wrapper
    assignment = []
    n_variables=len(csp.variables)
    for i in range(n_variables):
        assignment.append(None)
        
    estados_recorridos = [0]
    resultado = forward_checking(assignment, csp, estados_recorridos)
    print("Estados recorridos:",estados_recorridos[0])
    return resultado

def forward_checking(assignment, csp, estados_recorridos): #assignment va a ser el tablero y csp el csp con todas las variables y dominios
    failure = 0

    pos = select_unassigned_variable(assignment)

    if pos == -1: #assignment complete
        return assignment

    for value in order_domain_values(pos, csp):
        estados_recorridos[0] += 1
        if consistent(value, assignment, pos): #si no hay problemas en posicionar la reina en esa posicion entonces:
            assignment[pos]= value #colocamos la reina en el assignment
            inferences = inference(csp, pos, assignment) #inferences va a ser un array que va a contener clases variables, va a ser las variables con sus dominios antes de ser modificados por inference
            if inferences != failure: 
                result = forward_checking(assignment, csp, estados_recorridos)
                if result != failure:
                    return result
            else: #si se produce un error en las inferencias deshacemos lo que hicimos en la funcion
                csp.variables = inferences
        #removemos inferencias y el var=value (porque si llegamos acá estamos haciendo backtracking)
        csp.variables = inferences
        assignment[pos]= None

    return failure


def backtracking_search(csp):#funcion wrapper
    assignment = []
    n_variables=len(csp.variables)
    for i in range(n_variables):
        assignment.append(None)
    
    estados_recorridos = [0]
    resultado= backtracking(assignment, csp, estados_recorridos)
    print("Estados recorridos:",estados_recorridos[0])
    return resultado

def backtracking(assignment, csp, estados_recorridos): #assignment va a ser el tablero y csp el csp con todas las variables y dominios
    failure = 0

    pos = select_unassigned_variable(assignment)

    if pos == -1: #assignment complete
        return assignment

    for value in order_domain_values(pos, csp):
        estados_recorridos[0] += 1
        if consistent(value, assignment, pos): #si no hay problemas en posicionar la reina en esa posicion entonces:
            assignment[pos]= value #colocamos la reina en el assignment
            result = backtracking(assignment, csp, estados_recorridos)

            if result != failure:
                return result

        #removemos el var=value (porque si llegamos acá estamos haciendo backtracking)
        assignment[pos]= None

    return failure

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!funciones auxiliares!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def consistent(value, assignment, pos): #funcion que toma como parametros la fila el tablero y la columna (en ese orden) de una reina que queremos asignar, se fija si es posible ubicar una reina en la posicion dada sin que este amenazada por otra, si es posible retorna True sino False
    len_assignment=len(assignment)
    for i in range(len_assignment):
        if assignment[i] == value: #chequea reinas en la misma fila
            return False

        if i != pos and assignment[i] != None: #chequea diagonales de las reinas
            if (assignment[i]-i) + pos == value or (assignment[i]+i) - pos == value:
                return False

    return True #si llegamos hasta acá sin haber retornado false significa que no hay conflictos en posicionar la reina en la columna pos y en la fila value

def select_unassigned_variable(assignment): #hacemos simplemente static ordering, osea que vamos en orden de las variables no asignadas
    len_assignment = len(assignment)
    for i in range(len_assignment):
        if assignment[i] == None:
            return i
    return -1

def order_domain_values(pos, csp): #no la ordenamos de ninguna manera ya que hacer least constraining value no funciona
    return csp.variables[pos].domain

def inference(csp, pos, assignment): #esta funcion aplica la arco consistencia a todas las variables del csp adectadas por el nuevo assignment y devuelve las variables sin modificar el dominio para que se pueda revertir el cambio
    variables_copy = copy.deepcopy(csp.variables)
    
    len_variables = len(csp.variables)
    for i in range(len_variables):
        if i > pos:
            j=0
            while j < len(csp.variables[i].domain):
                value1 = csp.variables[i].domain[j]
                if not consistent(value1, assignment, i):
                    csp.variables[i].domain.remove(value1)
                    j-=1
                j+=1

    return variables_copy

# def order_domain_values(pos,assignment, csp): #usamos un algoritmo least constraining value
#     value_mayor = 0
#     len_domain = len(csp.domain)
#     l_values_ordenadas = []

#     domain = copy.deepcopy(csp.domain)
#     while len(l_values_ordenadas) < len_domain:
#         for i in range(len_domain):
#             value = domain[i]
#             if value != None:
#                 h= ((len_domain-1)-pos)+((len_domain-1)-value)+value #heuristica least constraining value
#                 if h >= value_mayor:
#                     i_guardado = i
                
#         l_values_ordenadas.append(domain[i_guardado])
#         domain[i_guardado] = None

#     return l_values_ordenadas