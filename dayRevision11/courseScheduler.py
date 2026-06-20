# LEETCODE: 207
from collections import deque

numCourses = 2
prerequisites = [[1,0]]

graph = [[] for _ in range(numCourses)]
inDegree = [0] * numCourses

for course, dependency in prerequisites:
    graph[dependency].append(course)
    inDegree[course] += 1

queue = [i for i in range(numCourses) if inDegree[i] == 0]
queue =deque(queue)
processed = 0
print(graph, inDegree)

while queue:
    current = queue.popleft()
    processed += 1
    for neighbour in graph[current]:
        inDegree[neighbour] -= 1
        if inDegree[neighbour] == 0: queue.append(neighbour)
    
print(processed == numCourses)
