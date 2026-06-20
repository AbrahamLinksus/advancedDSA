import heapq

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

def weight(points, x, y):
    x1, y1 = points[x]
    x2, y2 = points[y]
    return abs(x1 - x2) + abs(y1 - y2)

visited = [False for _ in range(len(points))]
minDist = [float('inf') for _ in range(len(points))]
minDist[0] = 0
total = 0

for _ in range(len(points)):
    heap = []
    
    u = i         
    visited[u] = 1
    total += minDist[u]
    for v in range(len(points)):
        if not visited[v]:
            minDist[v] = min(minDist[v], weight(points, u, v))