# hashset, open addressing and linear probes 

#KEY TAKEAWAYS : OPEN ADDRESSING/ LINEAR PROBING

def HASH(key, capacity):
    return (key % 5) % capacity

class hashSet:
    def __init__(self):
        self.capacity = 8
        self.array = [-1] * self.capacity
        self.counter = 0
        self.load = self.counter / self.capacity

    def loadFactor(self):
        self.load = self.counter / self.capacity

    def ADD(self, key):
        self.counter += 1
        i = hash = HASH(key, self.capacity)
        if self.array[hash] == -1 or self.array[hash] == -2:
            self.array[hash] = key
            print(self.array)
            return "added element"
        else:
            probe = 1
            hash = (i + probe) % self.capacity
            while hash != i:
                hash = (i + probe) % self.capacity
                if self.array[hash] == -1 or self.array[hash] == -2:
                    self.array[hash] = key
                    print(self.array)
                    return "added element probe"
                probe += 1
        self.RESIZE()
        self.ADD(key)
    
    def REMOVE(self, key):
        self.counter -= 1
        i = index = HASH(key, self.capacity)
        if self.array[index] == key:
            self.array[index] = -2
            print(self.array)
            return "element replaced with -2, begin"
        else:
            probe = 1
            hash = (i + probe) % self.capacity
            while hash != i:
                hash = (i + probe) % self.capacity
                if self.array[hash] == key:
                    self.array[hash] = -2
                    print(self.array)
                    return "element deleted"
                probe += 1
        print(self.array)
        return "array element not found"
    
    def CONTAINS(self, key):
        i = index = HASH(key, self.capacity)
        if self.array[index] == key:
            return "Found first try"
        else:
            probe = 1
            hash = (i + probe) % self.capacity
            while hash != i:
                hash = (i + probe) % self.capacity
                if self.array[hash] == key:
                    return "element found 2nd try"
                probe += 1
        return "element not found"
    
    def RESIZE(self): # pending resize
        self.capacity *= 2
        newArray = self.array
        self.array = [-1] * self.capacity
        for element in self.array:
            if element not in [-1, -2]:
                self.ADD(element)


newSet = hashSet()

print(newSet.ADD(2))
print(newSet.ADD(3))
print(newSet.ADD(4))
print(newSet.ADD(5))
print(newSet.ADD(6))
print(newSet.ADD(7))
print(newSet.ADD(8))

print(newSet.REMOVE(7))
print(newSet.REMOVE(8))
print(newSet.REMOVE(2))

print(newSet.ADD(2))
print(newSet.ADD(3))
print(newSet.ADD(4))
print(newSet.ADD(5))
print(newSet.ADD(6))
print(newSet.ADD(7))
print(newSet.ADD(8))




        