"""This function receives a two-dimensional list of 0's and 1's that represents a square maze, a tuple (row, column)
for the starting tile and a tuple(row, column) for the goal tile, and a boolean variable predermined to True indicating
if one can travel diagonally between two adjacent tiles or not. It returns a list of tuples (row, column) of all
the tiles that form the path between the start and the goal; None is returned if no path is found. """
import math

def bellmanFord(maze, startTuple, endTuple, diagonalsAllowed=True):
    if maze[startTuple[0]][startTuple[1]] == 1 or maze[endTuple[0]][endTuple[1]] == 1:
        return []

    distances = {}
    predecessor = {}
    edges = {}
    print("Coords")
    width = len(maze)
    length = len(maze[0])
    for i in range(width):
        for j in range(length):
            if maze[i][j] == 0:
                tuple = (i,j)
                distances[tuple] = math.inf
                predecessor[tuple] = None
                edges[tuple] = getAdjacentSquares(maze, tuple, False)

    print(getAdjacentSquares(maze, (0,1),False))
    distances[startTuple] = 0
    for _ in range(1, width*length):
        print("ITER")
        for key in distances:
            if distances[key] == math.inf:
                continue
            for edge in edges[key]:
                print(key, ":", edge)
                if distances[key] + 1 < distances[edge]:
                    distances[edge] = distances[key] + 1
                    print(distances[edge])
                    predecessor[edge] = key


    print(predecessor)
    print(distances)

    print("HELLO")
    prev = predecessor[endTuple]
    path = [endTuple]
    while not prev == startTuple:
        if prev == None:
            return []
        path.append(prev)
        print(prev)
        prev = predecessor[prev]


    print(path)

    return path

def getAdjacentSquares(maze, currentSquare, diagonalsAllowed, includeObstacles = False):
    width, length = len(maze), len(maze[0])
    row, col = currentSquare[0], currentSquare[1]
    assert col >= 0 and col < length and row >= 0 and row < width
    adjacent = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            newCol = col + i
            newRow = row + j
            if newCol >= 0 and newCol < length and newRow >=0 and newRow < width:
                if not(i == 0 and j == 0):
                    if (i * j != 0 and diagonalsAllowed) or i * j == 0:
                        if maze[newRow][newCol] == 0 or includeObstacles:
                            adjacent.append((newRow, newCol))
    return adjacent
