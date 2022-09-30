#modulo que configura una cola con prioridad invertida(el que menos valor tiene va primero)
from linkedlist import *

class PriorityQueue:
  head= None

class PriorityNode:
  value= None
  nextNode= None
  priority= None

def enqueue_priorityReverse(Q, element, priority): #en esta funcion encolamos para que el nodo en el head sea el nodo con valor de prioridad menor
  #nodo_sucesivo= Q.head #esto sirve para copiar el nodo que va a ir despues del nodo que agregamos
  nodo1= PriorityNode()
  nodo1.value= element
  nodo1.priority= priority
  
  currentNode = Q.head

  if currentNode == None:
    Q.head = nodo1
    return

  if nodo1.priority <= currentNode.priority:
    nodo1.nextNode= currentNode #metemos el nodo que estaba en la primera posicion despues de nuestro nuevo nodo
    Q.head= nodo1 #sustituimos el nodo que estaba por uno nuevo
    return

  while currentNode.nextNode != None:
    if nodo1.priority <= currentNode.nextNode.priority:
      nodo1.nextNode = currentNode.nextNode
      currentNode.nextNode = nodo1
      return
    currentNode = currentNode.nextNode

  currentNode.nextNode = nodo1

  return 

def dequeue_priority(Q):
  nodo_prioridad = Q.head
  Q.head= nodo_prioridad.nextNode

  return nodo_prioridad.value

def isEmpty(Q): #devuelve verdadero si la cola esta vacia y sino falso
  if Q.head == None:
    return True
  return False
  
def printPriorityQ(Q):
  current=Q.head
  print("[", end='')
  while current != None:
    print(current.value, end=', ')
    current = current.nextNode

  print("]")
