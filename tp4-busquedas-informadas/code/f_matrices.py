#modulo para crear y mostrar matrices de forma simple

def crear_matriz(filas, columnas): #crea una matriz vacia con las filas y columnas indicadas y la devuelve

    matriz= []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(None)

    return matriz

def print_matriz(matriz): #imprime las matrices en pantalla

    filas = len(matriz)
    for i in range(filas):
        columnas = len(matriz[i])
        for j in range(columnas):
            print(matriz[i][j], end=' ')
        print()

def llenar_matriz(matriz, relleno):
    filas = len(matriz)
    for i in range(filas):
        columnas = len(matriz[i])
        for j in range(columnas):
            matriz[i][j]= relleno
            