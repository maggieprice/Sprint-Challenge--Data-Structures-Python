class RingBuffer:
    def __init__(self, capacity):
        self.capacity= capacity
        self.data = []
        

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
            return self.data
        else: 
            if len(self.data) == self.capacity:
                self.data.pop(0)
                self.append(item)
            
            # remove head
            # insert new item into head

    def get(self):
        return self.data
