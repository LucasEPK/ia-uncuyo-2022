# Algoritmo Genetico que aprende a jugar un videojuego

## Codigo Proyecto: GASKI

### Lucas Moyano

## 1. Descripcion
![](skiings_image.PNG)

La idea de este proyecto es programar un algoritmo genetico para el juego de atari **Skiing** implementado usando la api de openai gym, observar el mejor puntaje que obtiene y fijarse como compara con el world record humano.

## 2. Objetivos:

- Cruzar todas las banderas 
- No chocar contra ningun obstaculo (arboles, banderas)
- Minimizar la perdida de velocidad (cruzar todas las banderas no asegura el mejor tiempo)

## 3. Alcance:

El algoritmo puede aprender a jugar Skiing de una manera optima aunque  los obstaculos cambien de posición

## 4. Limitaciones:

- El tiempo de ejecución, el algoritmo genetico podria tardarse mucho en llegar a un tiempo optimo ya que al principio todas las acciones son elegidas al azar.
- No sabemos cual es el mejor tiempo posible en el que una maquina puede completar el nivel.
	
## 5. Metricas:
- Numero de banderas cruzadas por el player durante la partida 
- Numero de obstaculos chocados por el player durante la partida
- Tiempo final del player al cruzar la ultima bandera/terminar el recorrido

Ademas de comparar el algoritmo genetico con el world record, voy a compararlo con un algoritmo de redes neuronales como actividad tentativa.

## 6. Propuesta algoritmo genetico:

Para lograr esto la idea es ejecutar el juego y que de manera random 10 players en contemporaneo vayan yendo a la derecha,a la izquierda o no haga nada hasta llegar al final. 
### 6.1 Representacion
Mientras el juego se está ejecutando se creará una lista de python para cada player, que va a guardar la acción que se ha realizado (0 si no se hace nada, 1 si se va a la derecha, 2 si se va a la izquierda) en la posicion que representa el segundo en que se hizo (Por ejemplo si se fue a la izquierda cuando el timer dice 0:40:34 se va a guardar en la posicion [403] un 2, descartamos el ultimo numero porque tanta precision no nos sirve). 
Despues de esto vamos a aplicar el algoritmo genetico que según la funcion de fitness **(6.2)** va a elegir pares de miembros de la poblacion y los va a reproducir usando cruzamiento, mutacion y elitismo **(6.3)**.
### 6.2 Funcion fitness del algoritmo
La función fitness va a ser las unidades por segundo recorridas por el player a la cual se le va a restar algunos segundo por las banderas no cruzadas.
### 6.3 Operadores 
Como operadores vamos a implementar:

- *elitismo*: guardamos los 2 primeros individuos como estan y los pasamos a la proxima generacion, para no perder buenas soluciones.
- *cruzamiento*: tomando dos listas, elegimos un punto al azar dividiendolas y tomamos la primera parte de una lista y la segunda de otra creando así el hijo, esto da buenos resultados en general.
- *mutación*: tenemos una cierta probabilidad de modificar 1 o más acciones de la lista del hijo, esto lo hacemos para que haya diversidad y no se quede solo con las acciones generadas al principio.


## 7. Justificacion
Como es un juego en tiempo real el entorno va cambiando cada segundo, haciendo que se haga dificil programarlo de manera tradicional, de esta forma podemos llegar a un algoritmo que llegue al mejor tiempo aunque cambiemos la posicion de los obstaculos (Osea el environment). El algoritmo genetico quizas no sea el más eficiente pero dandole el tiempo necesario da muy buenos resultados.

## 8. Listado de actividades a realizar
1. Aprender a usar la api de openai gym y ver como funciona más en profundidad [2 dias]
2. Programar las bases de como va a funcionar el algoritmo genetico [3 dias]
3. Implementar el algoritmo genetico con la api de openai gym [7 dias]
4. Hacer que la parte visual coincida con el algoritmo [3 dias]
5. **extra** Recolectar info sobre redes neuronales [4 dias]
6. **extra** Programar las bases de una red neuronal e implementarlas [10 dias]
7. Ejecucion del codigo y bugfixing [2 dias]
8. Analisis de los resultados [2 dias]
9. Escritura informe final [5 dias]

## 9. Cronograma estimado de actividades
![](diagrama_gantt.PNG)
## 10. Bibliografia
[AIMA 3rd edition](https://zoo.cs.yale.edu/classes/cs470/materials/aima2010.pdf)