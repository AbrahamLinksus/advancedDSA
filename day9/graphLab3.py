# DFS search on a graph, with the number of islands

class graph:
    def __init__(self, n) -> None:
        self.graph = [[0 for _ in range(n)] for _ in range(n)]
        self.visited = [[-1 for _ in range(n)] for _ in range(n)]

    def createGraph(dataArray):
        if not dataArray: return
        val1 = dataArray.pop(0)
        val2 = dataArray.pop(0)
        self.graph[val1][val2] = 1
        createGraph(dataArray)

    def dfsSearch(self, n):
        stack = [(0, 0)]

