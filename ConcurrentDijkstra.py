"""This function receives a two-dimensional list of 0's and 1's that represents a square maze, a tuple (row, column)
for the starting tile and a tuple(row, column) for the goal tile, and a boolean variable predermined to True indicating
if one can travel diagonally between two adjacent tiles or not. It returns a list of tuples (row, column) of all
the tiles that form the path between the start and the goal; None is returned if no path is found. """

def concurrentDijkstra(maze, startTuple, endTuple, diagonalsAllowed=True):
    return """List of tuples of the path's tiles """

import random
import sys

def main():
    #maze = generateRandomMaze(3, 4, 0.5)
    maze = [[0, 0, 1],
            [0, 1, 0],
            [1, 0, 0]]
    printMaze(maze)
    path = dijkstraSequential(maze, (0,0), (2,2), False)
    print(path)

def generateRandomMaze(length, width, obstaclesConcentrationIndex):
    maze = []
    for i in range(width):
        row = []
        for j in range(length):
            if random.random() <= obstaclesConcentrationIndex:
                row.append(1)
            else:
                row.append(0)
        maze.append(row)
    return maze

def printMaze(maze):
    for row in maze:
        for cell in row:
            print(cell, end = " ")
        print()

def getAdjacentSquares(maze, currentSquare, diagonalsAllowed):
    width, length = len(maze), len(maze[0])
    col, row = currentSquare[0], currentSquare[1]
    assert col >= 0 and col < length and row >= 0 and row < width
    adjacent = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            newCol = col + i
            newRow = row + j
            if newCol >= 0 and newCol < length and newRow >=0 and newRow < width:
                if not(i == 0 and j == 0):
                    if (i * j != 0 and diagonalsAllowed) or i * j == 0:
                        adjacent.append((newCol, newRow))
    return adjacent

def getDistance(tuple1, tuple2):
    x1, y1 = tuple1[0], tuple1[1]
    x2, y2 = tuple2[0], tuple2[1]

    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def dijkstraSequential(maze, startTuple, endTuple, diagonalsAllowed):
    # Check that the startNode and endNode are not obstacles
    if maze[startTuple[1]][startTuple[0]] == 1 or maze[endTuple[1]][endTuple[0]] == 1:
        return []

    # Create a list with all (row, col) tuples of the non-obstacle tiles in the maze
    nodeList = []
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] != 1:
                nodeList.append((col, row))

    visited = {}
    unvisited = {node: sys.maxsize for node in nodeList}
    previous = {node : None for node in nodeList}
    print("unvisited ", unvisited)
    current = startTuple
    unvisited[current] = 0

    ## lo siguiente guarda, compara, y seleccciona distancias como candidatos. neighbor nunca so ocupa guardar y solo se usa en esa instacio por lo cual no ocupa una variable declarada
    while True:
        adjacent = getAdjacentSquares(maze, current, diagonalsAllowed)
        for neighbour in adjacent:
            if neighbour not in unvisited: continue
            newDistance = unvisited[current] + getDistance(current, neighbour)
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
                previous[neighbour] = current

        # Mark the current node as visited and remove it form the unvisited dictionary
        visited[current] = unvisited[current]
        del unvisited[current]

        # End main loop if all nodes were checked
        if len(unvisited) == 0 or current == endTuple:
            break

        # Get the node with the lowest total distance from the unvisited ones
        current = min(unvisited, key = lambda item : unvisited[item])

    #print(visited)
    #print(previous)

    # Reconstruct path from the dictionary previous, traversing backwards from the endNode
    path = []
    currentTuple = endTuple
    while True:
        parent = previous[currentTuple]
        path.insert(0, currentTuple)
        currentTuple = parent
        if parent == None:
            break

    # Verify there is a path connecting the starting and ending nodes
    if path[0] != startTuple:
        return []
    else:
        return path

if __name__ == "__main__":
    main()
