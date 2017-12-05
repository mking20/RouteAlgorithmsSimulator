"""This function receives a two-dimensional list of 0's and 1's that represents a square maze, a tuple (row, column)
for the starting tile and a tuple(row, column) for the goal tile, and a boolean variable predermined to True indicating
if one can travel diagonally between two adjacent tiles or not. It returns a list of tuples (row, column) of all
the tiles that form the path between the start and the goal; None is returned if no path is found. """

def bellmanFord(maze, startTuple, endTuple, diagonalsAllowed=True):
    return """List of tuples of the path's tiles """
 Python program to find single source shortest paths
# for Directed Acyclic Graphs Complexity : OV(V+E)
from collections import defaultdict
 
# Graph is represented using adjacency list. Every
# node of adjacency list contains vertex number of
# the vertex to which edge connects. It also contains
# weight of the edge
class Graph:
    def __init__(self,vertices):
 
        self.V = vertices # No. of vertices
 
        # dictionary containing adjacency List
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph[u].append((v,w))
 
 
    # A recursive function used by shortestPath
    def topologicalSortUtil(self,v,visited,stack):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        if v in self.graph.keys():
            for node,weight in self.graph[v]:
                if visited[node] == False:
                    self.topologicalSortUtil(node,visited,stack)
 
        # Push current vertex to stack which stores topological sort
        stack.append(v)

    ''' The function to find shortest paths from given vertex.
        It uses recursive topologicalSortUtil() to get topological
        sorting of given graph.'''
    def shortestPath(self, s):
 
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack =[]
 
        # Call the recursive helper function to store Topological
        # Sort starting from source vertice
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(s,visited,stack)
 
        # Initialize distances to all vertices as infinite and
        # distance to source as 0
        dist = [float("Inf")] * (self.V)
        dist[s] = 0
 
        # Process vertices in topological order
        while stack:
 
            # Get the next vertex from topological order
            i = stack.pop()
 
            # Update distances of all adjacent vertices
            for node,weight in self.graph[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight
 
        # Print the calculated shortest distances
        for i in range(self.V):
            print ("%d" %dist[i]) if dist[i] != float("Inf") else  "Inf" ,
g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)
 
# source = 1
s = 1
 
print ("Following are shortest distances from source %d " % s)
g.shortestPath(s)
 
# This code is contributed by Neelam Yadav
