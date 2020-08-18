graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['E','A']
graph['C'] = ['A', 'B', 'E','F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']

#The length of the keys is used to provide the dimensions of the matrix which are stored in
#cols and rows.
matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)

#We then set up a cols by rows matrix, filling it with zeros.
adjancency_matrix = [[0 for x in range(cols)] for y in range(rows)]
# The edges_list variable will
# store the tuples that form the edges of in the graph. For example, an edge between node A
# and B will be stored as (A, B). And fill the array of tuple using a nested loop.
edges_list= []
for key in matrix_elements:
    for neighbour in graph[key]:
        edges_list.append((key,neighbour))

# fill  our multidimensional array(matrix) by using 1 to mark the
# presence of an edge with the line
for edge in edges_list:
    index_of_first_vertex = matrix_elements.index(edge[0])
    index_of_second_vertex = matrix_elements.index(edge[1])
    adjancency_matrix[index_of_first_vertex][index_of_second_vertex] = 1

print(adjancency_matrix)
