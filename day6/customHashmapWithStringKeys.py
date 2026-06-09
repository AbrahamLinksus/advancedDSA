def HASH(key, capacity):
      hash = 0
      for ch in key:
          hash = (hash * 31 + ord(ch)) % capacity
      return hash


class myHashMap:
      def __init__(self):
          self.capacity = 8
          self.array = [None] * self.capacity
          self.counter = 0

      def _load_factor(self):
          return self.counter / self.capacity

      def PUT(self, key, value):
          index = HASH(key, self.capacity)
          if self.array[index] is None:
              self.array[index] = [(key, value)]
          else:
              for i, (k, v) in enumerate(self.array[index]):
                  if k == key:
                      self.array[index][i] = (key, value)
                      return index, value
              self.array[index].append((key, value))
          self.counter += 1
          if self._load_factor() > 0.74:
              self.__RESIZE()
          return index, value

      def __RESIZE(self):
          self.capacity *= 2
          newArray = [None] * self.capacity
          for bucket in self.array:
              if bucket is None:
                  continue
              for key, value in bucket:
                  index = HASH(key, self.capacity)
                  if newArray[index] is None:
                      newArray[index] = [(key, value)]
                  else:
                      newArray[index].append((key, value))
          self.array = newArray

      def GET(self, key):
          index = HASH(key, self.capacity)
          if self.array[index] is None:
              return -1
          for k, v in self.array[index]:
              if k == key:
                  return v
          return -1

      def REMOVE(self, key):
          index = HASH(key, self.capacity)
          if self.array[index] is None:
              return "Invalid"
          filtered = [(k, v) for k, v in self.array[index] if k != key]
          if len(filtered) == len(self.array[index]):
              return "Invalid"  # key wasn't there
          self.array[index] = filtered if filtered else None
          self.counter -= 1
          return "Deleted"
      

hashMap = myHashMap()
print(hashMap.PUT("apple", 3))
print(hashMap.PUT("banana", 2))
print(hashMap.PUT("mango", 5))
print(hashMap.GET("apple"))
print(hashMap.GET("mango"))
print(hashMap.GET("banana"))