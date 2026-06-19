# to find the minimum cost to connect houses with its weight being the 
# manhattan distance between the coordinates

class MSTprims:
    def __init__(self, houses):
        self.houses = houses  
        self.n = len(houses)   

    def weight(self, u, v):
        x1, y1 = self.houses[u]
        x2, y2 = self.houses[v]
        return abs(x1 - x2) + abs(y1 - y2)

    def primsMST(self):
        visited = [0] * self.n
        minDist = [float('inf')] * self.n
        minDist[0] = 0
        total = 0

        for _ in range(self.n):
            best_dist = float('inf')
            u = -1
            for i in range(self.n):
                if not visited[i]:    
                    if minDist[i] < best_dist:  
                        best_dist = minDist[i]
                        u = i         
            visited[u] = 1
            total += minDist[u]
            for v in range(self.n):
                if not visited[v]:
                    minDist[v] = min(minDist[v], self.weight(u, v))

        return total
    
findHouses = MSTprims([[0,7],[0,9],[20,7],[30,7],[40,70]])
print(findHouses.primsMST())

