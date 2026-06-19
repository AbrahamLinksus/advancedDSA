# min heap 

class minHeap:
    def __init__(self):
        self.heapStructure = []

    def insert(self, value):
        self.heapStructure.append(value)
        index = len(self.heapStructure) - 1
        while index > 0 and self.heapStructure[(index - 1) // 2] > self.heapStructure[index]:
            self.heapStructure[index], self.heapStructure[(index-1) // 2] = self.heapStructure[(index-1) // 2], self.heapStructure[index]  
            index = (index - 1) // 2
        return self.heapStructure

    def sift(self):
        start = x = 0
        left = 2 * start + 1
        right = 2 * start - 2
        if left < len(self.heapStructure) and 
        return
    
    def getMinElement(self):
        deletedVal = self.heapStructure[0]
        newVal = self.heapStructure.pop()
        self.heapStructure[0] = newVal
        self.sift()
        return deletedVal