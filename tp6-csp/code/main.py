from n_queens import *

for i in range(5):
    if i == 0:
        size = 4
    elif i == 1:
        size = 8
    elif i == 2:
        size = 10
    elif i == 3:
        size = 12
    elif i == 4:
        size = 15

    print("!!!!!!!!!!!!RESOLUCION PROBLEMA DE ", size, "REINAS!!!!!!!!!!!!!!!")
    env = Environment(size)
    env.crear_csp()
    agente = Agent()
    print("RESOLUCION POR BACKTRACKING:")
    agente.solve_by_Backtracking(env)

    print("RESOLUCION POR FORWARD CHECKING:")
    agente.solve_by_Forward_Checking(env)
    print("")
