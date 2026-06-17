# To output a set of all connected components 

class graph:
    def __init__(self, n) -> None:
        self.graph =[[0 for _ in range(n)] for _ in range(n)]
        self.visited = [-1 for _ in range(n)]
        self.n = n 
    
    def createGraph(self, dataArray):
        if len(dataArray) < 2: return
        val1 = dataArray.pop(0)
        val2 = dataArray.pop(0)
        self.graph[val1][val2] = 1
        self.graph[val2][val1] = 1
        self.createGraph(dataArray)

    def _isInBoundary(self, i, j):
        if (i < 0 or i >= self.n or j < 0 or j >= self.n): return False
        return True

    def connectedComponents(self):
        if self.graph == []: return []
        components = []
        for start in range(self.n):
            if self.visited[start] != -1:
                continue
            component = []
            self.visited[start] = 1
            queue = [start]
            while queue:
                current = queue.pop(0)
                component.append(current)
                for index in range(self.n):
                    if self.graph[current][index] == 1 and self.visited[index] == -1:
                        self.visited[index] = 1
                        queue.append(index)
            components.append(component)
        return components

graph1 = graph(7)
graph1.createGraph([0, 1, 1, 2, 2, 3, 4, 5])
print(graph1.connectedComponents())

    
