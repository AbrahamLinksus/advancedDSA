#ask for intution!!

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
options = "abcdefghijklmnopqrstuvwxyz"
wordList = set(wordList)
queue = [(beginWord, 1)]
res = temp = []
while queue:
    current, level = queue.pop(0)
    for i in range(len(current)):
        for j in options:
            newWord = current[:i] + j + current[i+1:]
            if newWord == endWord:
                res.append(temp)
                continue
            if newWord in wordList: 
                queue.append((newWord, level+1))
                wordList.

