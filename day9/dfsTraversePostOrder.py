# To traverse a graph DFS, by using postfix 

class graph:
    def __init__(self, n) -> None:
        self.graph = [[0 for _ in range(n)] for _ in range(n)]
        self.visited = [-1] * n
        self.n = n

    def createTree(self, dataArray):
        if len(dataArray) < 2: return 
        val1 = dataArray.pop(0)
        val2 = dataArray.pop(0)
        self.graph[val1][val2] = 1
        self.graph[val2][val1] = 1
        self.createTree(dataArray)

    def dfsTraversePostFix(self):
        if self.graph == []: return []
        res = []
        for start in range(self.n):
            if self.visited[start] != -1:
                continue
            self.visited[start] = 1
            stack = [start]
            while stack:
               current = stack.pop()
               for index in range(self.n):
                   if self.graph[current][index] == 1 and self.visited[index] == -1:
                       stack.append(index)
                       self.visited[index] = 1
                       res.append(index)
        return res
    
graph1 = graph(5)
graph1.createTree([1,2,3,4,2])
print(graph1.dfsTraversePostFix())