# practice for the dijkstras algorithm 

import heapq
graph = {
    'A': [('B', 2), ('D', 8)],
    'B': [('A', 2), ('D', 5), ('E', 6)],
    'D': [('A', 8), ('B', 5), ('E', 3), ('F', 2)],
    'E': [('B', 6), ('D', 3), ('F', 1), ('C', 9)],
    'F': [('D', 2), ('E', 1), ('C', 3)],
    'C': [('E', 9), ('F', 3)]
}
n = len(graph)
dijkstrasMap = {i:[float('inf'), None] for i in graph.keys()}
dijkstrasMap['A'] = [0, None]



