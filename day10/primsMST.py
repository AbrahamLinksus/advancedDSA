# to find the MST using prims algorithm 
import heapq

val1 = [4, 5, 0, 1, 1, 0, 2, 3, 1, 2, 1, 1, 3, 4, 2, 3, 2]
class mstWithPrims:
    def __init__(self, dataArray):
        self.n = dataArray.pop(0)
        dataArray.pop(0)
        self.graph = [[] for _ in range(self.n)]
        self.visited = [-1 for _ in range(self.n)]
        self.dataArray = dataArray

    def createGraph(self):
        if len(self.dataArray) < 3: return
        val1 = self.dataArray.pop(0)
        val2 = self.dataArray.pop(0)
        val3 = self.dataArray.pop(0)
        self.graph[val1].append((val2, val3))
        self.graph[val2].append((val1, val3))
        self.createGraph()
        return self.graph
    
    def primsMST(self):
        if self.graph == []: return
        heap = []
        mstSum = 0
        mstOrder = []
        heapq.heappush(heap, (0, -1, 0))
        while heap:
            w, parent, u = heapq.heappop(heap)
            if self.visited[u] == -1:
                self.visited[u] = 1
                mstOrder.append((parent, u))
                mstSum += w
            for dest, weight in self.graph[u]:
                if self.visited[dest] == -1:
                    heapq.heappush(heap, (weight, u, dest))
        return mstOrder, mstSum

graph1 = mstWithPrims(val1)
print(graph1.createGraph())
print(graph1.primsMST())
    