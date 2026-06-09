# HashMap with Open Addressing and linear probing 

# KEY TAKEAWAYS = OPEN ADDRESSING/ PROBING

def HASH(key, capacity):
    return (key % 5) % capacity

class myHashMap:
    def __init__(self):
        self.capacity = 8
        self.myMap = [-1] * self.capacity
        self.counter = 0
        self.loadFactor = self.counter / self.capacity
    
    def loadFactor(self):
        return self.counter / self.capacity 
    
    def __RESIZE():return

    def PUT(self, key, value):
        self.counter += 1
        i = index = HASH(key, self.capacity)
        if self.myMap[index] == -1 or self.myMap[index] == -2:
            self.myMap[index] = (key, value)
            return "item added first try", self.myMap  
        else:
            probe = 1
            hash = (i + probe) % self.capacity
            while hash != i:
                if self.myMap[hash] == -1 or self.myMap[hash] == -2:
                    self.myMap[hash] = (key, value)
                    return "item added by probing", self.myMap
                probe += 1
                hash = (hash + probe) % self.capacity
        if self.loadFactor > 0.7:
            self.__RESIZE()

myMap = myHashMap()
print(myMap.PUT(11,100))
print(myMap.PUT(21,100))
print(myMap.PUT(31,100))
print(myMap.PUT(41,100))
print(myMap.PUT(51,100))
print(myMap.PUT(5,100))
print(myMap.PUT(6,100))



