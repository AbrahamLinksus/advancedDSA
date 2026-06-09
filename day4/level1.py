#queue from 2 stacks 

class queueByStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,val):
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        
        self.stack1.append(val)
        return self.stack1
    
    def dequeue(self):
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())

        self.stack2.pop()
        return self.stack2
    
queueByStack = queueByStacks()
print(queueByStack.enqueue(1))
print(queueByStack.enqueue(3))
print(queueByStack.enqueue(5))
print(queueByStack.dequeue())