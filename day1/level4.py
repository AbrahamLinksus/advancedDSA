# prefix sum hashmap to count sum of a list 

# KEY TAKEAWAYS = PREFIX SUM HASHMAPS 

array = [3, 4, 7, -3, 3, 1]
class continuousTransactions:
    def __init__(self, array):
        self.array = array
        self.prefixSum = [0] * len(self.array)

    def createPrefixSum(self):
        counter = 0
        sum = 0
        for index, element in enumerate(self.array):
            sum += element
            self.prefixSum[index] = sum
        return self.prefixSum

    def findTransactions(self, k):
        counter = 0
        for element in self.createPrefixSum():
            if element % k == 0:
                counter += 1
        return counter
    

tracker = continuousTransactions(array)
print(tracker.findTransactions(7))