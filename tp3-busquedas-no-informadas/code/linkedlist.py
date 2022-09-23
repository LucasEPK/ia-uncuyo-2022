#modulo que implementa una lista enlazada
class LinkedList:
  head=None

class Node:
  value=None
  nextNode=None


#L= LinkedList()
def add(L, element):
  nodo_sucesivo= L.head #esto sirve para copiar el nodo que va a ir despues del nodo que agregamos
  nodo1= Node()
  L.head= nodo1 #sustituimos el nodo que estaba por uno nuevo
  nodo1.value= element
  nodo1.nextNode= nodo_sucesivo #metemos el nodo que estaba en la primera posicion despues de nuestro nuevo nodo

def search(L, element):

  current= L.head 
  counter=0
  position=-1 #position es igual a -1 porque la posicion -1 no existe, entonces se evitan errores
  while current != None and position == -1: #esto es para saber cuando se llegó al final de la lista o si ya se encontró la posicion

    if current.value == element: #acá es donde se fija si en esa posicion está el elemento buscado
      position= counter

    counter= counter+1
    current= current.nextNode

  if position != -1:
    return position #se devuelve la posicion donde se encontraba el elemento
  else:
    return None

def insert(L, element, position):

  nodoA= Node()
  nodoA.value= element
  current= L.head

  if position > 1: #esto evita errores

    for counter in range(0, position-1): #esto nos va a posicionar en el lugar de la lista anterior a donde queremos ingresar el elemento
      if current != None: #esto es para que no se haga current.nextNode cuando current no sea un nodo
        current= current.nextNode
  
  if current == None:
    if position == 0: #esto se hace porque que la posicion sea 0 es igual a hacer add()
      add(L, element)
      return position
    else:
      return None #si current es igual a None y la posicion no es 0 eso significa que la posicion en la que se quiere insertar está afuera de los elementos de la lista
  else:

    if position == 0: #esto sucede porque puede pasar que la posicion 0 sea diferente de None y se quiera insertar un elemento en 0
      add(L, element)
    else:

      nodoA.nextNode= current.nextNode #copiamos el nodo de la posicion donde queremos insertar el nuevo nodo para que se re-vincule despues
      current.nextNode= nodoA #insertamos el nuevo nodo en posicion
    return position

def delete(L, element):
  position= search(L, element) #encuentra la posicion donde se encuentra el elemento con la funcion search
  current= L.head
  if position != None:

    if position > 1:
      for counter in range(0, position-1): #esto nos va a posicionar en el lugar de la lista anterior a donde queremos eliminar el elemento
        current= current.nextNode
    
    if position != 0:
      current.nextNode= current.nextNode.nextNode #se remplaza el elemento de la lista que queriamos eliminar por el proximo elemento, desviculandolo
    else:
      L.head= current.nextNode #esto pasa porque el primer elemento no tiene una posicion anterior, entonces hay que eliminarlo de esta manera

    return position
  else: #esto significa que no se encontró el elemento en la lista
    return None

def length(L):
  current=L.head
  counter=0
  while current != None:
    counter= counter + 1 #sumamos 1 despues de que se verifique que no sea None
    current= current.nextNode
  return counter

def access(L, position):

  current= L.head
  counter=0
  if position > 0:
    for counter in range(1, position+1): #empieza de 1 porque ya en la primer vuelta del bucle nos vamos a encontrar en el lugar 1 de la lista
      if current != None:
        current= current.nextNode
  
  if current != None: #cuando current es diferente de None significa que existe la posicion que se nos indico en la lista
    return current.value
  else:
    return None

def update(L, element, position):
  
  current= L.head
  if position > 0:

    for counter in range(1, position+1): #empieza de 1 porque ya en la primer vuelta del bucle nos vamos a encontrar en el lugar 1 de la lista
      if current != None:
        current= current.nextNode
  
  if current != None: #cuando current es diferente de None significa que existe la posicion que se nos indico en la lista
    current.value= element 
    return position
  else:
    return None

def move(LinkedList, position_orig, position_dest):
  element= access(LinkedList, position_orig)

  #lo siguiente se hace para evitar problemas con la funcion delete() ya que esta, si hay 2 numeros iguales, elimina siempre el primero
  current= LinkedList.head
  if position_orig != None:

    if position_orig > 1:
      for counter in range(0, position_orig-1): #esto nos va a posicionar en el lugar de la lista anterior a donde queremos eliminar el elemento
        current= current.nextNode
    
    if position_orig != 0:
      current.nextNode= current.nextNode.nextNode #se remplaza el elemento de la lista que queriamos eliminar por el proximo elemento, desviculandolo
    else:
      LinkedList.head= current.nextNode #esto pasa porque el primer elemento no tiene una posicion anterior, entonces hay que eliminarlo de esta manera

  insert(LinkedList, element, position_dest)

def printLinkedList(L):
  for pos in range(0, length(L)):
    print(access(L, pos)) #esto mejora el triple sin access

def copyList(L):
  copia = LinkedList()
  for pos in range(0, length(L)):
    insert(copia, access(L, pos), pos)
  return copia

def listEqualsNO(L1, L2): #devuelve si la lista 1 es igual a la lista 2 pero no en mismo orden, verdadero, sino falso
  longitud_L1 = length(L1)
  longitud_L2 = length(L2)

  if longitud_L1 == longitud_L2:#Si las longitudes son diferentes entonces L1 y L2 son diferentes, no tiene sentido revisar
    #buscamos todos los elementos de L1 en L2
    for i in range(0, longitud_L1): 

      for j in range(0, longitud_L2):
        if access(L1, i) == access(L2, j): #encontramos el elemento de L1 en L2
          e_encontrado = True

      if not e_encontrado: #si llegamos hasta acá sin encontrar el elemento entonces tal elemento no existe en L2, lo que hace las listas diferentes
        return False
  else: #longitudes diferentes de las listas
    return False

  return True #si llegamos hasta acá es porque nunca devolvimos falso, osea que las dos listas tienen los mismos elementos
