from node import Node

class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self,item):
        new_node = Node(item)
        tail = self.tail

        if tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
        #Making it circular
        self.tail.next =self.head
        self.size += 1

    def delete(self, item):
        current = self.head
        prev = self.head
        is_deleted = False

        #stop iteration when we reach the tail node
        while prev == current or prev != self.tail:
            if current.data == item:
                is_deleted = True
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                if current == self.tail:
                    prev.next = self.head
                    self.tail = prev
                else:
                    prev.next = current.next
                self.size -= 1
                return
            else:
                prev = current
                current = current.next
        
        if not is_deleted:
            print("Item was not found!!")

    def print_items(self):
        current = self.head
        prev = None
        index =0

        while current and prev != self.tail:            
            print("index:",index,"value:",current.get_data())
            prev = current
            current = current.get_next()
            index = index +1


if __name__ == "__main__":
    circularList = CircularList()
    circularList.append(5)
    circularList.append(67)
    circularList.append(70)
    circularList.append(45)
    circularList.append(23)    
    circularList.delete(23)
    circularList.print_items()
    