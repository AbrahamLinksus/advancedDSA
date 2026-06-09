mainString = "AAADAAACAAAACAAAA"
subString = "AAACAAAA"

if subString == "": print(-1)
lps = [0] * len(subString)
prevLPS, i = 0, 1

while i < len(subString):
    if subString[i-1] == subString[i]:
        lps[i] = prevLPS + 1
        prevLPS += 1
        i += 1
    else:
        if prevLPS == 0:
            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS - 1]

i, j = 0, 0
while i < len(mainString):
    if mainString[i] == subString[j]:
        i += 1
        j += 1
    else:
        if j == 0:
            i += 1
        else:
            j = lps[j - 1]
    if j == len(subString):
        print("found in index, ", i - j)
        j = lps[j -1]
