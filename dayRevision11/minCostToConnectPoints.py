# LEETCODE : 1584

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

def weight(x,y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

minArray = [float('inf') for _ in range(len(points))]
minArray[0] = 0
visitedArray = [False for _ in range(len(points))]
total = 0

for i in range(len(points)):
    bestDistance = float('inf')
    u = -1
    for j in range(len(points)):
        if not visitedArray[j]:
            if minArray[j] < bestDistance:
                bestDistance = minArray[j]
                u = j
    visitedArray[u] = True
    total += minArray[u]
    for i in range(len(points)):
        if not visitedArray[i]:
            minArray[i] = min(minArray[i], weight(points[u], points[i]))
print(total)