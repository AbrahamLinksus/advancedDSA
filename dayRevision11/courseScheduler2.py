# LEETCODE : 210

from collections import deque

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

graph = [[] for _ in range(numCourses)]
inDegree = [0] * numCourses
for course, dependency in prerequisites:
    graph[dependency].append(course)
    inDegree[course] += 1
ordering = []
queue = [i for i in range(numCourses) if inDegree[i] == 0]
queue = deque(queue)
while queue:
    current = queue.popleft()
    ordering.append(current)
    for neighbour in graph[current]:
        inDegree[neighbour] -= 1
        if not inDegree[neighbour]: queue.append(neighbour)
if len(ordering) == numCourses: 
    print(ordering)
else:
    print([])