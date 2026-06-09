# KMP algorithm for string matching 
#LEVEL 4 OF UNIT 3
#KEY TAKEAWAYS: KMP ALGORITM 

mainString = "AAADAAACAAAA"
subSting = "AAACAAAA"

class kmpAlgorithm:
    def __init__(self, mainString, subString):
        self.mainString = mainString
        self.subString = subString

    def findLPS(self):
        if self.subString == "": return 0
        lpsArr = [0] * len(self.subString)

        prevLPS, i = 0, 1

        while i < len(self.subString):
            if self.subString[i-1] == self.subString[i]:
                lpsArr[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            else:
                if prevLPS == 0:
                    lpsArr[i] = 0
                    i += 1
                else:
                    prevLPS = lpsArr[prevLPS - 1]
        return lpsArr
    
    def KmpAlgorithm(self):
        i, j = 0, 0 
        lps = self.findLPS()
        while i < len(self.mainString):
            if self.mainString[i] == self.subString[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j -1]
            if j == len(self.subString):
                return i - j
        return -1

stringMatch = kmpAlgorithm(mainString, subSting)
print(stringMatch.KmpAlgorithm())


