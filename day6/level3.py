#trading order book 

#KEY TAKEAWAYS: SortedDict

from sortedcontainers import SortedDict

class orderBook:
    def __init__(self):
        self.buyDict = SortedDict()
        self.sellDict = SortedDict()
        
    def ADD(self, price, volume, side):
        temp = 0
        if side.lower() == "buy":
            if self.buyDict.setdefault(price) is None:
                self.buyDict.update(price, volume)
                return "buy side added", self.buyDict
            self.buyDict.update(price, self.buyDict.setdefault(price)+volume)
            return "buy side added 2", self.buyDict
        if side.lower() == "sell":
            if self.sellDict.setdefault(price):
                self.sellDict.update(price, volume)
                return "sell side added"
            self.sellDict.update(price, self.sellDict.update(price)+volume)
            return "sell side added 2", self.sellDict
    
createOrder = orderBook()
print(createOrder.ADD("24500", 40, "buy"))
print(createOrder.ADD("24000", 30, "sell"))
print(createOrder.ADD("25000", 50, "buy"))
print(createOrder.ADD("24500", 40, "buy"))
