class RingBuffer:
    def __init__(self, capacity):
        self.capacity= capacity
        self.data = []
        current = self.head


    def append(self, item):
        while current:
        if len(self.data) == self.data:
            self.data.pop(current)
            self.data.insert(current, item)
        
            # remove head
            # insert new item into head

    def get(self):
        return self.data

