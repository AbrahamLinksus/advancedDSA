#LEETCODE: 684
edges = [[1,2],[1,3],[2,3]]

class unionFind:
    def __init__(self, edges):
        self.set1 = [-1 for _ in range(len(edges) + 1)]
        self.edges = edges

    def find(self, x):
        while self.set1[x] != -1:
            x = self.set1[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return False
        self.set1[x] = y
        return True
    
    def findOddOne(self):
        for i in self.edges:
            if not self.union(i[0], i[1]): return i

object1 = unionFind(edges)
print(object1.findOddOne())