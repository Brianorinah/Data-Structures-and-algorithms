class Stack():     
    def __init__(self):
        self.items =[]
    
    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return self.items == []

if __name__ == "__main__":
    s =Stack()
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    #print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
        
        
    