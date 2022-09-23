#modulo que define funciones para una cola (FIFO)
from linkedlist import *

def enqueue(Q, element):
  add(Q, element)

def dequeue(Q):
  if Q.head != None:
    element= access(Q, length(Q)-1)
    delete(Q, element)
    return element
  else:
    return None

def isEmpty(Q): #devuelve verdadero si la cola esta vacia y sino falso
  if Q.head == None:
    return True
  return False