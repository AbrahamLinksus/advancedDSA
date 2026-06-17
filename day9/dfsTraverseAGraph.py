# to traverse a graph using DFS method

class graph:
    def __init__(self, n):
        self.graph = [[0 for _ in range(n)] for _ in range(n)]
        self.visited = [-1] * n
        self.n = n

    def createGraph(self, dataArray):
        if len(dataArray) < 2: return
        val1 = dataArray.pop(0) - 1 
        val2 = dataArray.pop(0) - 1
        self.graph[val1][val2] = 1
        self.graph[val2][val1] = 1
        self.createGraph(dataArray)


    def DFSTRaverse(self):
        if self.graph == []: return []
        dfsOrder = []
        for start in range(self.n):
            if self.visited[start] != -1:
                continue
            stack = [start]
            self.visited[start] = 1
            while stack:
                current = stack.pop()
                dfsOrder.append(current)
                self.visited[current] = 1
                for index in range(self.n):
                    if self.graph[current][index] == 1 and self.visited[index] == -1:
                        self.visited[index] = 1
                        stack.append(index)
        return dfsOrder
    
graph1 = graph(5)
graph1.createGraph([1,2,1,3,2,4,2,5,4,5])
print(graph1.DFSTRaverse())


