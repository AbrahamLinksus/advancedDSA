# to find some metrics of a graph 

class graph:
    def __init__(self, dataArray):
        self.n = dataArray.pop(0)
        self.m = dataArray.pop(0)
        self.weightSum = 0
        self.minEdge = float('inf')
        self.maxEdge = float('-inf')
        self.totalNoOfEdges = 0
        self.dataArray = dataArray

    def findMetrics(self):
        if len(self.dataArray) < 3: return
        val1 = self.dataArray.pop(0)
        val2 = self.dataArray.pop(0)
        val3 = self.dataArray.pop(0)
        self.totalNoOfEdges += 1
        self.minEdge = min(self.minEdge, val2)
        self.maxEdge = max(self.maxEdge, val2)
        self.weightSum += val2
        self.findMetrics()
        return self.n, self.m, self.minEdge, self.maxEdge, self.totalNoOfEdges, self.weightSum
    

graph1 = graph([4,5,0,1,1,0,2,3,1,2,1,1,3,4,2,3,2])
n, m, minEdge, maxEdge, totalEdges, weightSum = graph1.findMetrics()
print(n)
print(m)
print(minEdge)
print(maxEdge)
print(weightSum)