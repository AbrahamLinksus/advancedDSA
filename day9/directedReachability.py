# follow edges from source to find every node reaechable from an input S

class graph:
    def __init__(self, dataArray):
        self.N = dataArray.pop(0)
        dataArray.pop(0)
        self.dataArray = dataArray
        self.graph = [[0 for _ in range(self.N)] for _ in range(self.N)]
        self.visited = [-1 for _ in range(self.N)]

    def createGraph(self):
        if len(self.dataArray) < 2: return
        val1 = self.dataArray.pop(0)
        val2 = self.dataArray.pop(0)
        self.graph[val1][val2] = 1
        self.graph[val2][val1] = 1
        self.createGraph()

    def inBoundary(self, val):
        return (val > -1 and val <= self.N)

    def findReachability(self, start):
        if self.graph == []: return
        queue = [start]
        bfsOrder = [start]
        reachable = 0
        while queue:
            current = queue.pop(0)
            for index in range(self.N):
                if self.graph[current][index] == 1 and self.visited[index] == -1:
                    self.visited[index] = 1
                    reachable += 1
                    queue.append(index)
                    if index not in bfsOrder: bfsOrder.append(index)
        return bfsOrder, reachable
    
graph1 = graph([5, 4, 0, 1, 0, 2, 1, 3, 1, 4, 0])
graph1.createGraph()
print(graph1.findReachability(0))
                

