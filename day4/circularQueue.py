class createQueue:
    def __init__(self, size):
        self.array = ['val'] * size
        self.head = 0
        self.tail = 0
        self.n = 0
        self.size = size
    
    def enqueue(self, data):
        if self.head == self.tail and self.n == self.size: return "queue overflow"
        self.array[self.tail] = data
        self.tail = (self.tail + 1) % self.size
        self.n += 1
        return self.array
    def dequeue(self):
        if self.head == self.tail and self.n == 0:
            return "Array Empty"
        self.array[self.head] = 'val'
        self.head = (self.head + 1) % self.size
        self.n -= 1
        return self.array
    

n = 6
queue = createQueue(n)
print(queue.enqueue(1))
print(queue.enqueue(2))
print(queue.enqueue(3))
print(queue.enqueue(4))
print(queue.enqueue(5))
print(queue.enqueue(7))
print(queue.dequeue())
print(queue.dequeue())
print(queue.enqueue(6))