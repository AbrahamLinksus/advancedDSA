# shortest path from begin word to end word 
#brute force 

beginword = "hit"
endword = "cog"
wordlist = ["hot", "dot", "dog", "lot", "log", "cog"]
setlist = set(wordlist)
options = "abcdefghijklmnopqrstuvwxyz"
queue = [(beginword, 0)]
print(queue)
while queue:
    currentWord, level = queue.pop(0)
    tempWord = currentWord
    for i in range(len(currentWord)):
        for j in options:
            newWord = currentWord[:i] + j + currentWord[i+1:]
            if newWord == endword:
                    print(level + 1)
            if newWord in setlist:
                queue.append((newWord, level+1))
                print(queue)
                setlist.discard(newWord)
                
                    
            


