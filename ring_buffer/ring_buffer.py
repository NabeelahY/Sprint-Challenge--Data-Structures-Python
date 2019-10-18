class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        if len(self.storage) >= self.capacity:
            if self.current >= len(self.storage):
                self.current = 0
                self.storage[self.current] = item
                self.current += 1
            else:
                self.storage[self.current] = item
                self.current += 1
        else:     
            self.storage.append(item)
            self.current += 1

    def get(self):
        if self.storage.count(None) == self.capacity:
            return self.storage
        if self.storage.count(None) == 0:
          return self.storage
        if self.storage.count(None) < self.capacity:
            self.storage.remove(None)
            return self.storage