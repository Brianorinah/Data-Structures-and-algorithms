import sys

class Graph():
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for row in range(vertices)] for column in range(vertices)]

    def min_val(self, dist,visited_list):
        min = sys.maxsize

        for x in range(self.v):
            if visited_list[x] == False and dist[x]< min:
                min = dist[x]
                min_index = x
        return min_index


    def dijkstra(self,src):
        dist=[sys.maxsize] * self.v
        dist[src] = 0
        visited_list = [False] * self.v

        for edge in range(self.v):

            i = self.min_val(dist,visited_list)
            visited_list[i] = True

            for j in range(self.v):
                if self.graph[i][j] > 0 and visited_list[j] == False and dist[j] > dist[i] + self.graph[i][j]:
                    dist[j] = dist[i] + self.graph[i][j]
        
        self.print_solution(dist)

    def print_solution(self, dist):
        for node in range(self.v):
            print(node, "distance" , dist[node])

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

g.dijkstra(0)