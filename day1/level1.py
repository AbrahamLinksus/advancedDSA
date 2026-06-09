# create a program to count the total using hashmap 

#kEY TAKEAWAY = USEAGE OF HASHMAPS

class cartLookup:
    def __init__(self):
        self.items = {}
        self.cart = {}
    
    def addItems(self, itemId, itemPrice):
        self.items[itemId] = itemPrice
    
    def addToCart(self, itemId, itemQuantity):
        self.cart[itemId] = itemQuantity
    
    def findCartTotal(self):
        total = 0
        for id, quantity in self.cart.items():
            if self.items[id]:
                total += self.items[id] * quantity
        return total
    
makeCart = cartLookup()
makeCart.addItems("SKU1",100)
makeCart.addItems("SKU2",250)
makeCart.addItems("SKU3",75)
makeCart.addItems("SKU4",500)

makeCart.addToCart("SKU2", 2)
makeCart.addToCart("SKU4", 1)
makeCart.addToCart("SKU1", 3)

print("Cart Total: ",makeCart.findCartTotal())