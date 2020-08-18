class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        self.items.pop()
    
    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)



if __name__ == "__main__":
    q = Queue()
    q = Queue()
    q.enqueue('hello')
    q.enqueue('dog')
    q.enqueue('aa')
    q.enqueue(3)
    q.dequeue()
    print(q.items)