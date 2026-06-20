#LEETCOE : 200
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

def dfsSearch(x, y, grid, visited, components):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]): return
    if grid[x][y] == "0" or visited[x][y] == 1: return
    components.append([x,y])
    visited[x][y] = 1
    dfsSearch(x + 1,y ,grid, visited, components)
    dfsSearch(x - 1,y ,grid, visited, components)
    dfsSearch(x ,y + 1,grid, visited, components)
    dfsSearch(x ,y - 1,grid, visited, components)
    return components, visited


def search(grid):
    component = 0
    visited = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    if grid == []: return
    for start in range(len(grid)):
        for next in range(len(grid[0])):
            if grid[start][next] == "1" and visited[start][next] == -1:
                dfsSearch(start, next, grid, visited, [])
                component += 1
        
    return component

print(search(grid))