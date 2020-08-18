from collections import deque

#Initiate a graph
graph = dict()
graph['A'] = ['B', 'G', 'D']
graph['B'] = ['A', 'F', 'E']
graph['C'] = ['F', 'H']
graph['D'] = ['F', 'A']
graph['E'] = ['B', 'G']
graph['F'] = ['B', 'D', 'C']
graph['G'] = ['A', 'E']
graph['H'] = ['C']

def breadth_first_search(graph, root):
    #Initiate an empty list that will hold the visited nodes;a queue that will be used for traversal that will initialy
    # contain the first node to be traversed(root). Then append this root to the visited_vertices list.
    visited_vertices = list()
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root

    while len(graph_queue) > 0:
        #Get the next node to be traversed by dequeing it
        node = graph_queue.popleft()
        #Get all its adjacent nodes/vertices
        adj_nodes = graph[node]

        #Get the adjacent nodes that are not already visited(visited_vertices) by using the difference operator. 
        remaining_nodes = set(adj_nodes).difference(set(visited_vertices))
        if remaining_nodes:
            # loop through the sorted remaining nodes
            for elem in sorted(remaining_nodes):
                #add all these remaining nodes the visited_vertices list
                visited_vertices.append(elem)
                #add all these nodes to the queue
                graph_queue.append(elem)

    return visited_vertices

print(breadth_first_search(graph,"A"))