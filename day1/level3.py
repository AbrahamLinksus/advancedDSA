# to use 2 pointers find shortest window of flash-sale days reaching target

# KEY TAKEAWAY = SLIDING WINDOW

array = [2, 3, 1, 2, 4, 3, 1, 5]
class findWindows:
      def __init__(self, array):
          self.inputArray = array

      def find(self, k):
          lptr = 0
          windowSum = 0
          minLen = float('inf')
          for rptr in range(len(self.inputArray)):
              windowSum += self.inputArray[rptr]
              while windowSum > k:           
                  windowSum -= self.inputArray[lptr]
                  lptr += 1
              if windowSum == k:
                  minLen = min(minLen, rptr - lptr + 1)
          return minLen if minLen != float('inf') else "no such sum"

window = findWindows(array)
print(window.find(7)) 
            
