# build levels for a DAG

class graph:
    def __init__(self, dataArray):
        self.n = dataArray.pop(0)
        self.m = dataArray.pop(0)
        self.dataArray = dataArray
        self.graph = [[] for _ in range(self.n)]
        self.visited = [-1 for _ in range(self.n)]
        self.inDegree = {}
            
    def findInDegree(self):
        self.inDegree = {i: [] for i in range(self.n)}
        for index, element in enumerate(self.graph):
            for i in element:
                self.inDegree[i].append(index)
        return self.inDegree

    def removeFromIndegree(self, toDelete):
        for index, element in self.inDegree.items():
            self.inDegree[index] = [val for val in element if val != toDelete]

    def createGraph(self):
        if len(self.dataArray) < 2: return
        val1 = self.dataArray.pop(0)
        val2 = self.dataArray.pop(0)
        self.graph[val1].append(val2)
        self.createGraph()

    def buildLevel(self):
        queue = []
        for index, element in self.inDegree.items():
            if element == []: queue.append(index)
        levels = []
        while queue:
            levelSize = len(queue)
            currentLevel = []
            for _ in range(levelSize):
                current = queue.pop(0)
                if self.visited[current] != -1:
                    continue
                self.visited[current] = 1
                currentLevel.append(current)
                self.removeFromIndegree(current)
                for neighbor in self.graph[current]:
                    if self.visited[neighbor] == -1 and self.inDegree[neighbor] == []:
                        queue.append(neighbor)
            levels.append(currentLevel)
        return levels


graph1 = graph([6, 6, 0, 1, 0, 2, 1, 3, 2, 3, 3, 4, 3, 5])
graph1.createGraph()
graph1.findInDegree()
print(graph1.buildLevel())

