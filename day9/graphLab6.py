# Cycle Detection and Bipartite check

class graph:
    def __init__(self, n) -> None:
        self.graph = [[0 for _ in range(n)] for _ in range(n)]
        self.visited = [-1 for _ in range(n)]

    def createGraph(self, dataArray):
        if len(dataArray) < 2: return
        val1 = dataArray.pop(0)
        val2.dataArray.pop(0)
        self.graph[val1][val2] = 1
        self.graph

    def checkCycles(self):

