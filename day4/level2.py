#min stack price tracker 

class minPriceTracker:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def PUSH(self, val):
        self.stack1.append(val)
        if len(self.stack2) > 0:
            self.stack2.append(min(val, self.stack2[-1]))
            return
        self.stack2.append(val)

    def MIN(self):
        print("MIN =",self.stack2[-1])

    def POP(self):
        self.stack2.pop()
        self.stack1.pop()
        return

    
    def SIZE(self):
        print("SIZE =",len(self.stack1))
    
price = minPriceTracker()
price.PUSH(5)
price.PUSH(3)
price.MIN()
price.PUSH(7)
price.MIN()
price.POP()
price.POP()
price.MIN()
price.SIZE()