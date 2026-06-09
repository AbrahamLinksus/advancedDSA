from finalDqueue import dequeue

class createSchedule:
    def __init__(self):
        self.queue = dequeue()
    
    def VIP(self, id):
        print(self.queue.pushFront(id))
    
    def REGULAR(self, id):
        print(self.queue.pushBack(id))
    
    def BOARD(self):
        print(self.queue.popFront())
    
    def QUIT(self):
        print(self.queue.popBack())
    
schedule = createSchedule()
schedule.REGULAR(1)
schedule.REGULAR(2)
schedule.VIP(3)
schedule.BOARD()
schedule.QUIT()
schedule.REGULAR(4)
schedule.BOARD()