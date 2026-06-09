class staticArray:
      def __init__(self):
          self.front = 7
          self.back = 0
          self.readFront = 0
          self.data = [None] * 8

class dequeue:
      def __init__(self):
          self.front = 0
          self.back = 1
          self.frontArray = staticArray()
          self.backArray = staticArray()
          self.dynamicArray = [self.frontArray, self.backArray]
          self.size = 8
          self.counter = 0

      def pushFront(self, data):
          currentArray = self.dynamicArray[self.front]
          if currentArray.front == -1:
              newArray = staticArray()
              newArray.data[newArray.front] = data
              newArray.front -= 1
              self.dynamicArray.insert(0, newArray)
              self.back += 1
              return newArray.data
          currentArray.data[currentArray.front] = data
          currentArray.front -= 1
          self.counter += 1
          return currentArray.data

      def pushBack(self, data):
          currentArray = self.dynamicArray[self.back]
          if currentArray.back == 8:
              newArray = staticArray()
              newArray.data[newArray.back] = data
              newArray.back += 1
              self.dynamicArray.append(newArray)
              self.back += 1
              return newArray.data
          currentArray.data[currentArray.back] = data
          currentArray.back += 1
          self.counter += 1
          return currentArray.data

      def popFront(self):
          self.counter -= 1
          currentArray = self.dynamicArray[self.front]
          while currentArray.front == 7 and currentArray.back == 0 and len(self.dynamicArray) > 1:
              self.dynamicArray.pop(0)
              self.back -= 1
              currentArray = self.dynamicArray[self.front]
          if currentArray.front == 7:
              toDeleteElement = currentArray.data[currentArray.readFront]
              currentArray.data[currentArray.readFront] = None
              currentArray.readFront += 1
              return toDeleteElement
          toDeleteElement = currentArray.data[currentArray.front + 1]
          currentArray.data[currentArray.front + 1] = None
          currentArray.front += 1
          if currentArray.front == 7 and currentArray.back == 0 and len(self.dynamicArray) > 1:
              self.dynamicArray.pop(0)
              self.back -= 1

          return toDeleteElement

      def popBack(self):
          self.counter -= 1
          currentArray = self.dynamicArray[self.back]
          if currentArray.back == 0:
              self.dynamicArray.pop(len(self.dynamicArray) - 1)
              self.back -= 1
              currentArray = self.dynamicArray[self.back]
          toDeleteElement = currentArray.data[currentArray.back - 1]
          currentArray.data[currentArray.back - 1] = None
          currentArray.back -= 1
          if currentArray.back == 0 and len(self.dynamicArray) > 1:
              self.dynamicArray.pop(len(self.dynamicArray) - 1)
              self.back -= 1
          return toDeleteElement

      def peekFront(self):
          currentArray = self.dynamicArray[self.front]
          if currentArray.front == 7 and currentArray.back == 0 and len(self.dynamicArray) > 1:
              currentArray = self.dynamicArray[self.front + 1]
          if currentArray.front == 7:
              return currentArray.data[currentArray.readFront]
          return currentArray.data[currentArray.front + 1]

      def peekBack(self):
          return self.dynamicArray[self.back].data[self.dynamicArray[self.back].back
  - 1]