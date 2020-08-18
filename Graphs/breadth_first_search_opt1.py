#O(n) = O(V + E)
# It checks and appends the starting node to the visited list and the queue.
# Then, while the queue contains elements, it keeps taking out nodes from the queue, appends the neighbors of that node to the queue if they are unvisited, and marks them as visited.
# This continues until the queue is empty.
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

def breadth_first_search(graph, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        current_item = queue.pop(0)
        #print(current_item, end=" ")

        for neighbour in graph[current_item]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited
            
print(breadth_first_search(graph,"A"))
