# to find the minimum number of moves from start to end state 

class graph:
    def __init__(self, limit):
        self.visited = [-1] * (limit + 1)
        self.start = 1
        self.end = 11
        self.limit = limit

    def performOperation(self, var):
        op1 = var + 1
        op2 = var - 1
        op3 = var * 2
        return op1, op2, op3
    
    def inBoundary(self, var):
        return (var > -1 and var < self.limit)

    def reachTarget(self):
        if self.start > self.limit: return
        queue = [self.start]
        distanceCounter = 0
        while queue:
            for index in range(len(queue)):
                current = queue.pop(0)
                if self.visited[current] != -1:
                    continue
                if current == self.end:
                    return distanceCounter, "reachable"
                val1, val2, val3 = self.performOperation(current)
                self.visited[current] = 1
                if self.inBoundary(val1): queue.append(val1)
                if self.inBoundary(val2): queue.append(val2)
                if self.inBoundary(val3): queue.append(val3)
            distanceCounter += 1

        return "element not found"
    
graph1 = graph(12)
print(graph1.reachTarget())


