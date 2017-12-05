"""This function receives a two-dimensional list of 0's and 1's that represents a square maze, a tuple (row, column)
for the starting tile and a tuple(row, column) for the goal tile, and a boolean variable predermined to True indicating
if one can travel diagonally between two adjacent tiles or not. It returns a list of tuples (row, column) of all
the tiles that form the path between the start and the goal; None is returned if no path is found. """

import random
import sys
from graphics import *
import time

OBSTACLE = 1
FREE_TILE = 0;
COLORS = ["#ff0000", "#ff1a75", "#ff33cc", "#cc33ff", "#6666ff", "#0066ff", "#00ccff", "#00ff99", "#1aff1a", "#ccff66", "#ffff00", "#ff6600"]

def main():
    # For testing only
    
    maze = generateRandomMaze(15, 16, 0.2)
    window, rectangles_dict = generateGraphicBoard(maze)

    cluster_dict, path_list = dijkstraParallel(maze, (2,3), (11, 8), False)
    for clusterNum, cluster in cluster_dict.items():
        drawCluster(window, rectangles_dict, cluster, COLORS[clusterNum % len(COLORS)])
        time.sleep(1)

    for tile in path_list:
        rectangles_dict[tile].setFill("#DD2C00")
    window.getMouse()
    #path = dijkstraSequential(maze, (0,0), (2,2), False)
    #print(path)

def generateGraphicBoard(maze):
    NUMBER_SQUARES = max(len(maze), len(maze[0]))

    # Initializing Window
    window = GraphWin("Finding optimal route", 500, 500)
    window.setCoords(-0.5, -0.5, NUMBER_SQUARES + 0.5, NUMBER_SQUARES + 0.5)

    # List of rectangles that can be used to change their colors later
    rectangles_dict = {}

    for rowNum in range(len(maze)):
        for colNum in range(len(maze[rowNum])):
            # Drawing the tile of the maze
            newRect = Rectangle(Point(colNum, rowNum), Point(colNum + 1, rowNum + 1))

            # Checking if it is a free tile or an obstacle
            if maze[rowNum][colNum] == FREE_TILE:
                newRect.setFill("white")
            else:
                newRect.setFill("black")

            # Drawing the rectangle/tile in the window
            newRect.draw(window)

            # Adding the rectangle to the rectangles list
            rectangles_dict[(colNum, rowNum)] = newRect

    return window, rectangles_dict

def drawCluster(window, rectangles_dict, cluster, color):
    for tile in cluster:
        graphics_rectangle = rectangles_dict[tile].setFill(color)

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
    for rowNum in range(len(maze) - 1, -1, -1):
        for cell in maze[rowNum]:
            print(cell, end = " ")
        print()

def getAdjacentSquares(maze, currentSquare, diagonalsAllowed, includeObstacles = False):
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
                        if maze[newRow][newCol] == FREE_TILE or includeObstacles:
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

def dijkstraParallel(maze, startTuple, endTuple, diagonalsAllowed):
    if maze[startTuple[1]][startTuple[0]] == OBSTACLE or maze[endTuple[1]][endTuple[0]] == OBSTACLE:
        return {}, []

    # Initialize a boolean dictionary that stores the visited state of the nodes
    # and another one that stores the nearest parent of each tile
    visited = {}
    parent = {}
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            tile = maze[i][j]
            if tile == FREE_TILE:
                visited[(j, i)] = False
                parent[(j, i)] = None

    visited[startTuple] = True
    cluster = {0:[startTuple]}
    clusterNumber = 0

    while len(cluster[clusterNumber]) != 0:
        # Initialize the list of tiles of the next outer cluster
        cluster[clusterNumber + 1] = []

        # Find all tiles adjacent to the current outer cluster
        for tile in cluster[clusterNumber]:
            adjacent_tiles = getAdjacentSquares(maze, tile, diagonalsAllowed)
            for cluster_candidate in adjacent_tiles:
                if visited[cluster_candidate] == False:
                    # Add the new tile to the new cluster being created
                    cluster[clusterNumber + 1].append(cluster_candidate)
                    visited[cluster_candidate] = True

                    # Set the cluster_candidate's parent
                    #if cluster_candidate[0] - tile[0] == 0 or cluster_candidate[1] - tile[1] == 0:
                        # The  is not diagonally adjacent, so cluster_candidate's parent should be tile
                    parent[cluster_candidate] = tile
                    #else:
                        # The cluster_candidate is diagonally adjacent, so check if it is cross adjacent to
                        # another tile in the current cluster
                        #for

        # Increment current cluster number by 1
        clusterNumber += 1

        # Check if the endNode was found already
        if parent[endTuple] != None:
            print("Found")
            break

    # TODO: Find the path from the start node to the end node
    if parent[endTuple] == None:
        return cluster

    path = [endTuple]
    current_tile = parent[endTuple]
    while current_tile != None:
        path.insert(0, current_tile)
        current_tile = parent[current_tile]

    return cluster, path



if __name__ == "__main__":
    main()
