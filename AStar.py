"""This function receives a two-dimensional list of 0's and 1's that represents a square maze, a tuple (row, column)
for the starting tile and a tuple(row, column) for the goal tile, and a boolean variable predermined to True indicating
if one can travel diagonally between two adjacent tiles or not. It returns a list of tuples (row, column) of all
the tiles that form the path between the start and the goal; None is returned if no path is found. """

from heapq import * #This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.

def heuristica(a, b): #Measuring the heuristic
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def astar(array, start, end, diagonal): #A Star using the start and the goal to create a path.
    if diagonal == True:
        vecinos= [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    else:
        vecinos = [(0,1),(0,-1),(1,0),(-1,0)]
##    array= np.array(array)
    mi_set = set()
    visitados = {}
    g = {start:0}
    f = {start:heuristica(start, end)}
    heap = []
    heappush(heap, (f[start], start))
    
    while heap:
        actual = heappop(heap)[1]
        if actual == end:
            path = []
            while actual in visitados:
                path.append(actual)
                actual = visitados[actual]
            path.append(start)
            return path
        mi_set.add(actual)
        for i, j in vecinos:
            vecino = actual[0] + i, actual[1] + j            
            tentativo= g[actual] + heuristica(actual, vecino)
            if 0 <= vecino[0] < len(array): #Checa cuantas rows hay
                if 0 <= vecino[1] < len(array[0]): #Checa cuantas columnas hay
                    if array[vecino[0]][vecino[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue   
            if vecino in mi_set and tentativo >= g.get(vecino, 0):
                continue  
            if  tentativo < g.get(vecino, 0) or vecino not in [i[1]for i in heap]:
                visitados[vecino] = actual
                g[vecino] = tentativo
                f[vecino] = tentativo + heuristica(vecino, end)
                heappush(heap, (f[vecino], vecino))    
    return False

