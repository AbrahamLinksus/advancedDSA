# to find the shortest path from source to destination using Dijkstra's algorithm 
import heapq

class dijkstraFind:
    def __init__(self, dataArray):
        self.n = dataArray.pop(0)
        self.m = dataArray.pop(0)
        self.dataArray = dataArray
        self.adjList = [[] for _ in range(self.n)]
        self.distanceMap = [[False, float('inf'), -1] for _ in range(self.n)]

    def createGraph(self):
        if len(self.dataArray) < 3: return
        val1 = self.dataArray.pop(0)
        val2 = self.dataArray.pop(0)
        val3 = self.dataArray.pop(0)
        self.adjList[val1].append((val2, val3))
        self.createGraph()
        print(self.adjList)

    def performDijkstra(self,dest, source=0):
        if self.adjList == []: return
        self.distanceMap[source] = [False, 0, -1]
        heap = []
        heapq.heappush(heap, (0, source))
        while heap:
            print(heap)
            currentWeight, node = heapq.heappop(heap)
            if self.distanceMap[node][0]:
                continue
            self.distanceMap[node][0] = True
            if node == dest:
                return currentWeight, self.distanceMap
            for neighbor, weight in self.adjList[node]: 
                newDist = currentWeight + weight
                if not self.distanceMap[neighbor][0] and newDist < self.distanceMap[neighbor][1]:
                    self.distanceMap[neighbor][1] = newDist
                    heapq.heappush(heap, (newDist, neighbor))
            
        return "Not found"

data = [5, 6, 0, 1, 4, 0, 2, 1, 1, 2, 2, 2, 3, 5, 3, 4, 3]
graph1 = dijkstraFind(data)
graph1.createGraph()
print(graph1.performDijkstra(4))