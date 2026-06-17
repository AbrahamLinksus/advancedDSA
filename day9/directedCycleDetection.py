# to find cycles in a graph and the number of sources 

class graph:
    def __init__(self, dataArray):
        self.N = dataArray.pop(0)
        self.M = dataArray.pop(0)
        self.dataArray = dataArray
        self.visited = [-1] * self.N
        self.graph = [[] for _ in range(self.N)]
        self.degree = {}

    def createGraph(self):
        if len(self.dataArray) < 2: return 
        val1 = self.dataArray.pop(0)
        val2 = self.dataArray.pop(0)
        self.graph[val1].append(val2)
        self.createGraph()

    def createInDegree(self):
        self.degree = {i: [] for i in range(self.N)}
        for index, element in enumerate(self.graph):
            for i in element:
                self.degree[i].append(index)
        return self.degree

    def removeFromIndegree(self, toDelete):
        for index, element in self.degree.items():
            self.degree[index] = [val for val in element if val != toDelete]

    def findCycleAndSources(self):
        if self.graph == []: return
        queue = []
        for index, element in self.degree.items():
            if len(element) == 0:
                queue.append(index)
        sources = list(queue)
        visitedCount = 0
        while queue:
            for index in range(len(queue)):
                current = queue.pop(0)
                if self.visited[current] != -1:
                    continue
                self.visited[current] = 1
                visitedCount += 1
                self.removeFromIndegree(current)
                for neighbor in self.graph[current]:
                    if self.visited[neighbor] == -1 and len(self.degree[neighbor]) == 0:
                        queue.append(neighbor)
        hasCycle = visitedCount != self.N
        return {"sources": sources,"hasCycle": hasCycle}


graph1 = graph([3,3,0,1,1,2,2,0])
graph1.createGraph()
graph1.createInDegree()
print(graph1.findCycleAndSources())
    
