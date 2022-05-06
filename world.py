import numpy as np
from robot import *

class Graph():
    def __init__(self, nb_vertices):
        self.vertices = nb_vertices
        self.graph = np.zeros((nb_vertices,nb_vertices))

def print_robots_distances(graph,list):
    print('Robot id \t distance from selected Robot')
    for i in range(graph.vertices):
        print(i,'\t\t',list[i])


def dijkstra(graph, V0):
    inf = 1e7
    V = graph.vertices
    dist = [inf] * V
    dist[V0] = 0
    Bool_arr = [False] * V

    for i in range(V):
        min = 1e7
        for j in range(V):
            if(dist[j] < inf and Bool_arr[j] == False):
                min = dist[j]
                min_index = j
        u = min_index
        Bool_arr[u] = True
        
        for v in range(graph.vertices):
            if(graph.graph[u][v] > 0 and Bool_arr[v] == False
               and dist[v] > dist[u] + graph.graph[u][v]):
                dist[v] = dist[u] + graph.graph[u][v]
        print_robots_distances(graph,dist)


def test_dijkstra():
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
            ]

    dijkstra(g,0)

def star_graph():
    g = Graph(NUM_OF_ROBOTS)
    g.graph = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 3, 6, 1, 0, 2, 1, 3, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],]
    return g

def test_star_graph():
    g = star_graph()
    dijkstra(g,4)


test_dijkstra()
