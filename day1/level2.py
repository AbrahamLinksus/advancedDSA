# to find the k best selling products

#KEY TAKEAWAY = COMPARISON SORT : simultaneously have an array of itemName sorted

class sellingItems:
    def __init__(self):
        self.itemWithQuantity = {}
        self.sortedIndex = []

    def addItems(self, itemName, itemQuantity):
        self.itemWithQuantity[itemName] = itemQuantity
        if self.sortedIndex == []:
            self.sortedIndex.append(itemName)
            
        elif self.itemWithQuantity[itemName] < self.itemWithQuantity[self.sortedIndex[-1]]:
            self.sortedIndex.append(itemName)
           
        elif self.itemWithQuantity[itemName] > self.itemWithQuantity[self.sortedIndex[0]]:
            self.sortedIndex.insert(0, itemName)
            
        else:
            i = 0
            while itemQuantity <= self.itemWithQuantity[self.sortedIndex[i]]:
                i += 1
            self.sortedIndex.insert(i, itemName)
            
        return 

    def findKBestSellers(self, k):
        if k > len(self.sortedIndex): return "K is greater than number of items"
        for index in range(k):
            itemName = self.sortedIndex[index]
            print(itemName,self.itemWithQuantity[itemName], sep=": ")
        return "good day"
    
createItems = sellingItems()
createItems.addItems("Apple", 120)
createItems.addItems("Banana", 300)
createItems.addItems("Cherry", 300)
createItems.addItems("Date", 50)
createItems.addItems("Elder", 210)
print(createItems.findKBestSellers(3))