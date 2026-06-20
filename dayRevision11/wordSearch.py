# LEETCODE : 79

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
visited = [[False] * len(board[0]) for _ in range(len(board))]
def dfs(x, y, word):
    if not word: return True
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]): return False
    if board[x][y] != word[0] or visited[x][y] == True: return False
    visited[x][y] = True
    foundVal = (dfs(x + 1, y, word[1:]) or dfs(x -1, y, word[1:]) or dfs(x, y + 1, word[1:]) or dfs(x, y -1 , word[1:]))
    visited[x][y] = False
    return foundVal
returnVal = False
for i in range(len(board)):
    for j in range(len(board[0])):
        if dfs(i, j, word): 
            returnVal = True
            print(returnVal)