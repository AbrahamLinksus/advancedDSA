# To read an undirected graph into an adjacency list and report its basic stats 

class graph:
    def __init__(self, n) -> None:
        self.graph = [[0 for i in range(n)] for _ in range(n)]
        self.visited = [[-1 for i in range(n)]for _ in range(n)]

    def createGraph(self, dataArray):
        if len(dataArray) == 0: return
        val1 = dataArray.pop(0)
        val2 = dataArray.pop(0)
        self.graph[val1][val2] = 1
        self.createGraph(dataArray)

    def printGraph(self):
        return self.graph

    def findVertices(self):
        return len(self.graph)

    def findEdges(self):
        noOfEdges = 0
        for i in range(len(self.graph)):
            for j in range(len(self.graph[0])):
                if self.graph[i][j] == 1:
                    noOfEdges += 1
        return noOfEdges

    def findDegree(self, n):
        res = [0] * n
        maxDegree = float('-inf')
        for i in range(len(self.graph)):
            for j in range(len(self.graph[0])):
                if self.graph[i][j] == 1:
                    res[i] += 1
                if self.graph[j][i] == 1:
                    res[i] += 1
            maxDegree = max(res[i], maxDegree)
        return res, maxDegree
    
    
graph1 = graph(6)
graph1.createGraph([5,5,0,1,0,2,1,2,1,3,3,4])
print(graph1.printGraph())
print(graph1.findVertices())
print(graph1.findEdges())
print(graph1.findDegree(6))

