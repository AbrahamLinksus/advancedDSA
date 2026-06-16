# DFS search on a graph, with the number of islands

class graph:
    def __init__(self, n) -> None:
        self.n = n
        self.graph = [[0 for _ in range(n)] for _ in range(n)]
        self.visited = [-1 for _ in range(n)]

    def createGraph(self, dataArray):
        if len(dataArray) < 2: return
        val1 = dataArray.pop(0)
        val2 = dataArray.pop(0)
        self.graph[val1][val2] = 1
        self.graph[val2][val1] = 1
        self.createGraph(dataArray)

    def dfsSearch(self, start=0):
        n = self.n
        dfsOrder = []
        self.visited[start] = 1
        stack = [start]
        while stack:
            current = stack.pop()
            dfsOrder.append(current)
            for index in range(n):
                if self.graph[current][index] == 1 and self.visited[index] == -1:
                    self.visited[index] = 1
                    stack.append(index)

        return dfsOrder


graph1 = graph(6)
graph1.createGraph([0,1,1,2,3,4])
print(graph1.dfsSearch())
