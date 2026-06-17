# to topo sort using reverse Post Orders 

class graph:
    def __init__(self, dataArray):
        self.n = dataArray.pop(0)
        self.m = dataArray.pop(0)
        self.dataArray = dataArray
        self.visited = [-1 for _ in range(self.n)]
        self.graph = [[0 for _ in range(self.n)] for _ in range(self.n)]

    def createGraph(self):
        if len(self.dataArray) < 2: return
        val1 = self.dataArray.pop(0)
        val2 = self.dataArray.pop(0)
        self.graph[val1].append(val2)
        self.createGraph()

    def topoSort(self):
        if self.graph == []: return
        for start in range(self.n):
            queue = [start]
            