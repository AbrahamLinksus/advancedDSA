# implement a crowd window monitor using monotonic dequeues 
from finalDqueue import dequeue

class windowMonitor:
    def __init__(self):
        self.array = [5, 1, 3, 9, 2, 8, 4, 6]
        self.k = 3
        self.minDequeue = dequeue()
        self.maxDequeue = dequeue()
        self.front = 0
        self.res = []
        self.max = self.array[0]
        self.min = self.array[0]

    def findMaxima(self):
        self.front = 0
        self.res = []
        for index, element in enumerate(self.array):
            if element > self.max:
                self.max = element
            while self.maxDequeue.counter > 0 and self.array[self.maxDequeue.peekBack()] < element:
                self.maxDequeue.popBack()
            self.maxDequeue.pushBack(index)
            if self.maxDequeue.peekFront() <= index - self.k:
                self.maxDequeue.popFront()
            if index >= self.k - 1:
                self.res.append(self.array[self.maxDequeue.peekFront()])
        return self.res
    
    def findMinima(self):
        self.front = 0
        self.res = []
        for index, element in enumerate(self.array):
            if element < self.min:
                self.min = element
            while self.minDequeue.counter > 0 and self.array[self.minDequeue.peekBack()] > element:
                self.minDequeue.popBack()
            self.minDequeue.pushBack(index)
            if self.minDequeue.peekFront() <= index - self.k:
                self.minDequeue.popFront()
            if index >= self.k - 1:
                self.res.append(self.array[self.minDequeue.peekFront()])
        return self.res
            
    def findSpread(self):
        return self.max - self.min

monitor = windowMonitor()
print("Window Minima: ",monitor.findMaxima())
print("Window Minima: ", monitor.findMinima())
print("Max spread:", monitor.findSpread())