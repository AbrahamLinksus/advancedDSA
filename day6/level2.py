#fraud detection engine using hashset and frequency maps 

#KEY TAKEAWAYS:

class paymentObject:
    def __init__(self, key):
        self.paymentPerson = key[0]
        self.TransactionID = key[1]
        self.accountNumber = key[2]
        self.timeStamp = key[3]
        self.amount = key[4]

class fraudDetect:
    def __init__(self):
        self.set = {}
        self.counter = 0
    
    def insertElement(self, transactionID, UserID, recipient, amount, timeStamp):
        

        
