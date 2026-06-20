beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

if endWord not in wordList: print(0)
allowedWord = [set() for _ in range(len(beginWord))]
for element in wordList:
    for i in range(len(beginWord)):
            