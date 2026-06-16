# BFS Traversal and distances 

class graph:
    def __init__(self, n) -> None:
        self.n = n
        self.graph = [[0 for _ in range(n)]for _ in range(n)]
        self.visited = [-1 for _ in range(n)]

    def createTree(self, dataArray):
        if len(dataArray) < 2: return
        val1 = dataArray.pop(0)
        val2 = dataArray.pop(0)
        self.graph[val1][val2] = 1
        self.graph[val2][val1] = 1
        self.createTree(dataArray)

    def BFSTraverse(self, start=0):
        n = self.n
        distance = [-1] * n
        bfsOrder = []
        queue = [start]
        self.visited[start] = 1
        distance[start] = 0
        while queue:
            node = queue.pop(0)
            bfsOrder.append(node)
            for neighbor in range(n):
                if self.graph[node][neighbor] == 1 and self.visited[neighbor] != 1:
                    self.visited[neighbor] = 1
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
        return bfsOrder, distance

graph1 = graph(6)
graph1.createTree([ 0, 1, 0, 2, 1,3,2, 3, 3, 4, 0])
order, distance = graph1.BFSTraverse(0)
print("BFS order:", order)
print("Distances from 0:", distance)
