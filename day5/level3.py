# palindrome checker with finalDqueue
from finalDqueue import dequeue

class checkPalindrome:
    def __init__(self):
        self.dequeue = dequeue()

    def check(self, string):
        l, r = 0, len(string) - 1
        while l < r:
            self.dequeue.pushFront(string[l])
            b = self.dequeue.pushBack(string[r])
            l += 1
            r -= 1
        return b
    
find = checkPalindrome()
print(find.check("abcba"))