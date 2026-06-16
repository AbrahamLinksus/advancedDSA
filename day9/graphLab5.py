# To find the grid Shortest Path

class graph:
    def __init__(self, n) -> None:
        self.n = n
        self.graph = [[1 for _ in range(n)] for _ in range(n)]
        self.visited = [[-1 for _ in range(n)] for _ in range(n)]

    def createGraph(self, dataArray):
        if len(dataArray) < 2: return 
        val1 = dataArray.pop(0)
        val2 = dataArray.pop(0)
        self.graph[val1][val2] = 0
        
        self.createGraph(dataArray)
        return self.graph

    def findShortestPath(self, start=0):
        distance = [0] * self.n
        queue = [start]
        while queue:
            current = queue.pop(0)
            for index in range(self.n):
                if self.graph[current][index] == 1 and self.visited[current][index] != -1:
                    queue.append(index)
                if (current, index) == (self.n-1, self.n-1):
                    print("reached")
            distance[current] = distance[current-1] + 1

        return distance

graph1 = graph(3)
print(graph1.createGraph([0,0,0,1,1,1,2,1,2,2]))
print(graph1.findShortestPath())
