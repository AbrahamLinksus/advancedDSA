#LEETCODE : 547

isConnected = [[1,1,0],[1,1,0],[0,0,1]]

visited = [False] * len(isConnected)

def dfs(node):
    visited[node] = True
    for neighbour in range(len(isConnected)):
        if isConnected[node][neighbour] == 1 and not visited[neighbour]:
            dfs(neighbour)
counter = 0
for main in range(len(isConnected)):
    if not visited[main]: 
        dfs(main)
        counter += 1
print(counter)