class createGraph:
    def __init__(self) -> None:
        self.graph = [[1,1,0,0], [1,0,0,1], [0,1,1,1], [1,0,0,1]]
        self.visited = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]

    def _inBoundary(self, i, j, n):
        if i > -1 and i < n and j > -1 and j < n: return True
        return False

    def dfsTraverse(self, i, j, n):
        if self._inBoundary(i, j, n) is False or self.graph[i][j] == 0 or self.visited[i][j] == 1: return
        self.visited[i][j] = 1
        self.dfsTraverse(i-1, j, n) # move up 
        self.dfsTraverse(i+1, j, n) # move down
        self.dfsTraverse(i, j-1, n) # move left
        self.dfsTraverse(i, j+1, n) # move right 
        return

    def findIslands(self, n):
        noOfIslands = 0
        for i in range(n):
            for j in range(n):
                if self.graph[i][j] == 1 and self.visited[i][j] != 1:
                    noOfIslands += 1
                    self.dfsTraverse(i, j, n)
        return noOfIslands

mainGraph = createGraph()
print(mainGraph.findIslands(4))
