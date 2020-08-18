class Deque:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)
    
    def add_rear(self, item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

if __name__ == "__main__":
    d= Deque()
    d.add_rear(4)
    d.add_rear("brian")
    d.add_rear(12)
    d.add_front(7)
    d.remove_front()
    d.remove_rear()
    print(d.items)
    print(d.size())
    print(d.is_empty())

