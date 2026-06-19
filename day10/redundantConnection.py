# to find the redundant edge in an undirected graph 
#LEETCODE : 684
edge1 = [[1,2], [1,3], [2,3]]
edge2 = [[1,2],[2,3],[3,4],[1,4],[1,5]]
class unionFind():
    def __init__(self, edges):
        self.edges = edges
        self.array = [-1] * (len(edges) + 1)

    def find(self, x):
        while self.array[x] != -1:
            x = self.array[x]
        return x
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.array[x] = y
            return True
        return False

    def findVal(self):
        for element in self.edges:
            if not self.union(element[0], element[1]): return element


find1 = unionFind(edge2)
print(find1.findVal())