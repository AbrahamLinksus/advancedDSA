# to find the minimum spanning tree using Kruskals algorithm 
from unionFind import unionFind

class graph:
    def __init__(self, dataArray):
        self.n = dataArray.pop(0)
        self.m = dataArray.pop(0)
        self.dataArray = dataArray
        self.set1 = unionFind(self.n)

    def kruskalsMST(self):
        data = []
        while len(self.dataArray) > 2:
            data.append((self.dataArray.pop(0), self.dataArray.pop(0), self.dataArray.pop(0)))
        mstWeight = 0
        connections = []
        Connected = "no"
        sortedData = sorted(data, key=lambda e: (e[2], e[0], e[1]))
        for element in sortedData:
            if self.set1.union(element[0], element[1]):
                connections.append((element[0], element[1]))
                mstWeight += element[2]
        if self.n - 1 == len(connections):
            Connected = "yes"
        return mstWeight, connections, Connected
    
val1 = [4,5,0,1,1,0,2,3,1,2,1,1,3,4,2,3,2]
val2 = [3,3,0,1,1,1,2,2,0,2,3]
graph1 = graph(val1)
print(graph1.kruskalsMST())