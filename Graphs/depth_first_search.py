graph = dict()
graph['A'] = ['B', 'S']
graph['B'] = ['A']
graph['S'] = ['A','G','C']
graph['D'] = ['C']
graph['G'] = ['S','F','H']
graph['H'] = ['G','E']
graph['E'] = ['C','H']
graph['F'] = ['C','G']
graph['C'] = ['D','S','E','F']

def depth_first_search(graph, root):
     #Initiate an empty list that will hold the visited nodes;a stack that will be used for traversal that will initialy
    # contain the first node to be traversed(root). 
    visited_vertices = list()
    #This regular list will act as our stack
    graph_stack = list()
    graph_stack.append(root)
    node = root

    if node not in visited_vertices:
        #If node is not in the list of visited nodes, we add it.
        visited_vertices.append(node)
        #get its adjacent nodes
        print(node, end=" ")
        adj_nodes = graph[node]

        #If all the adjacent nodes have been visited, we pop that node
        #from the stack and set node to graph_stack[-1].
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            if len(graph_stack) > 0:
                node = graph_stack[-1]           
            
        else:
            remaining_nodes = set(adj_nodes).difference(set(visited_vertices))
            first_adj_node = sorted(remaining_nodes)[0]
            node = first_adj_node

    #return visited_vertices

depth_first_search(graph,"A")
#print(depth_first_search(graph,"A"))
        

