# to find the minimum spanning tree and maximum spanning tree 
from unionFind import unionFind

val1 = [4,5,0,1,1,0,2,3,1,2,1,1,3,4,2,3,2]
class graph:
    def __init__(self, dataArray):
        self.n = dataArray.pop(0)
        self.m = dataArray.pop(0)
        self.setMin = unionFind(self.n)
        self.setMax = unionFind(self.n)
        self.dataArray = dataArray

    def minKruskals(self):
        temp = list(self.dataArray)
        connections = []
        data = []
        totalWeight = 0
        while len(temp) > 2:
            newData = (temp.pop(0), temp.pop(0), temp.pop(0))
            data.append(newData)
        sortedData = sorted(data, key=lambda e: (e[2], e[0], e[1]))
        for element in sortedData:
            if self.setMin.union(element[0], element[1]):
                connections.append([element[0], element[1]])
                totalWeight += element[2]
        return totalWeight, connections
    
    def maxKruskals(self):
        temp = list(self.dataArray)
        connections = []
        data = []
        totalWeight = 0
        while len(temp) > 2:
            newData = (temp.pop(0), temp.pop(0), temp.pop(0))
            data.append(newData)
        sortedData = sorted(data, key=lambda e: (e[2], e[0], e[1]), reverse=True)
        for element in sortedData:
            if self.setMax.union(element[0], element[1]):
                connections.append([element[0], element[1]])
                totalWeight += element[2]
        return totalWeight, connections
    
    
    
graph1 = graph(val1)
print(graph1.minKruskals())
print(graph1.maxKruskals())
