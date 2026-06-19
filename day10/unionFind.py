# disjoint set with union and find operations 

class unionFind:
    def __init__(self, n):
        self.array = [-1 for _ in range(n)]

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
    
    def query(self, x, y):
        x = self.find(x)
        y = self.find(y)
        return True if x == y else False
  


    
