# ALIEN SORT : GeeksForGeeks

word = ["baa", "abcd", "abca", "cab", "cad"]
graph = []

set1 = set()
for element in word:
    for j in element:
        set1.add(j)

length = len(set1)
i = 0
j = 1
while j < len(word):
    len1 = len(word[i])
    len2 = len(word[j])