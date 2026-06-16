# BFS Traversal and distances 

class graph:
    def __init__(self, n) -> None:
        self.graph = [[0 for _ in range(n)]for _ in range(n)]
        self.visited = [[-1 for _ in range(n)] for _ in range(n)]

    def createTree(self, dataArray):
        if not dataArray: return 
        val1 = dataArray.pop(0)
        val2 = dataArray.pop(0)
        self.graph[val1][val2] = 1
        self.createTree(dataArray)
    
    def _inBoundary(i, j, n):
        if i > -1 or i < n or j > -1 or j < n: return True
        return False

    def BFSTraverse(self, n):
        queue = [(0, 0)]
        distance = [0] * n
        bfsOrder = []
        while queue:
            length = len(queue)
            for index in range(length):
                i, j = queue.pop(0)
                i += 1
                if self._inBoundary(i, j, n): 
                    queue.append((i, j))
                    self.visited[i][j] = 1
                i -= 2
                if self._inBoundary(i, j, n): 
                    queue.append((i, j))
                    self.visited[i][j] = 1
                i += 1
                j +=1 
                if self._inBoundary(i, j, n): 
                    queue.append((i, j))
                    self.visited[i][j] = 1
                j -= 2
                if self._inBoundary(i, j, n): 
                    queue.append((i, j))
                    self.visited[i][j] = 1
            bfsOrder.append(i)
        return bfsOrder

graph1 = graph(5)
graph1.createTree([0, 1, 0, 2, 1,3,2, 3, 3, 4, 0])
print(graph1.BFSTraverse((5)))
