# to create a hashMap with chaining an LL per bucket 

#KEY TAKEAWAYS: HASHING WITH CHAINING

class paymentObject:
    def __init__(self, key, value):
        self.upiID = key[0]
        self.accountNumber = key[1]
        self.transationID = key[2]
        self.IFSCCode = key[3]
        self.value = value
        self.next = None

class myPaymentHashMap:
    def __init__(self):
        self.counter = 0
        self.capacity = 16
        self.array = [None] * self.capacity
        self.loadFactor = self.counter/ self.capacity
    
    def __loadfactor(self):
        self.loadFactor = self.counter / self.capacity
        return self.loadFactor
    
    def matchObjects(self, current, key):
        if (current.upiID == key[0] and current.accountNumber == key[1] and current.transationID == key[2] and current.IFSCCode == key[3]): return True
        return False

    
    def resize(self):
        old_array = self.array
        self.capacity *= 2
        self.array = [None] * self.capacity
        self.counter = 0 
        
        for head in old_array:
            current = head
            while current is not None:
                self.put((current.upiID, current.accountNumber, 
                          current.transationID, current.IFSCCode), current.value)
                current = current.next
    
    def hashTransation(self, paymentItem):
        def hash(string, offset):
            initial = 1
            for i, element in enumerate(str(string)):
                initial = initial * (offset**i) + ord(element)
            return initial
        upiVar, accountNumberVar, paymentVar, IFSCcodeVar = paymentItem
        upiVar = hash(upiVar, 31)
        accountNumberVar = hash(accountNumberVar, 509)
        paymentVar = hash(paymentVar, 13)
        IFSCcodeVar = hash(IFSCcodeVar, 21)
        totalHash = upiVar + accountNumberVar + IFSCcodeVar + paymentVar
        totalHash %= self.capacity
        return totalHash
    
    def put(self, key, value):
        index = self.hashTransation(key)
        if self.array[index] is None: 
            self.counter += 1
            self.array[index] = paymentObject(key, value)
            return "added"
        
        current = self.array[index]

        while current is not None:
            if self.matchObjects(current, key):
                current.value = value
                return "already exists"
            if current.next is None:
                break
            self.counter += 1
            current = current.next
        current.next = paymentObject(key, value)
        self.__loadfactor()
        if self.loadFactor > 0.74:
            self.resize()
        return "added 2"
    
    def get(self, key):
        index = self.hashTransation(key)
        current = self.array[index]
        if current is None:
            return "value does not exist"
        else:
            if self.matchObjects(current, key): return current.value, "2"
            else:
                while self.matchObjects(current, key):
                    current = current.next
                return current.value, "3"
    
    def remove(self, key):
        index = self.hashTransation(key)
        current = self.array[index]
        prev = None
        
        while current is not None:
            if self.matchObjects(current, key):
                if prev is None:
                    self.array[index] = current.next
                else: 
                    prev.next = current.next
                self.counter -= 1
                return "removed"
            prev = current
            current = current.next
        return "not found"
    
    def size(self):
        return self.counter
    
    def isEmpty(self):
        return self.counter == 0
    
    def clear(self):
        self.array = [None] * self.capacity
        return "cleared"

payment = myPaymentHashMap()
print(payment.put(("jake@hdfc", "1234556", "1X2A3W", "CBSE2021F"), 50000))
print(payment.put(("jake@hdfc", "2546789", "1Y2B3W", "CBSE2021F"), 100000))
print(payment.put(("jake@hdfc", "9283746", "1T2U3W", "CBSE2021F"), 150000))
print(payment.get(("jake@hdfc", "1234556", "1X2A3W", "CBSE2021F")))