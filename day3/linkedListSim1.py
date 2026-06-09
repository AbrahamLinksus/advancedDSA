n = 5
arr = [10, 20, 30, 40, 50]

class Node:
    def __init__(self, data):
        self.data = data
        self.npx = 0

class XORLinkedList:
    def __init__(self):
        self.head = None
        self.memory = {}
        self.prevNode = None

    def createLL(self, arr, n):
        for index in range(n):
            newNode = Node(arr[index])
            self.memory[id(newNode)] = newNode

            if self.head is None:
                self.head = newNode
                self.prevNode = newNode
                break

            





        

    
        
    


LL1 = XORLinkedList()
LL1.append(10)