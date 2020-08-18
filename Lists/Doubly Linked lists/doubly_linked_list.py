from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head =None
        self.tail = None
        self.size = 0

    #Good alternative for iterating the list
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def append(self,item):       

        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.size += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def delete(self,item):
        current = self.head
        node_deleted= False

        if current is None:
            node_deleted = False
        elif current.data == item:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        elif self.tail.data == item:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current:
                if current.data == item:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                    current = current.next
        
        if node_deleted:
            self.size -= 1
        else:
            print("Item was not found!!")

    def contains(self,item):
        # current = self.head
        # found = False

        # while current:
        #     if current.data == item:
        #         found = True
        #     else:
        #         current = current.next

        # return found

        #Better way using the iter() generator

        for node_data in self.iter():
            if data == node_data:
                return True
            return False

    def clear(self):
        self.head = None
        self.tail = None
                




if __name__ == "__main__":
    
    doublylist = DoublyLinkedList()
    doublylist.append(5)
    doublylist.append(22)
    doublylist.append(44)
    
    #Looping through the iter() function to print all items in the list. 
    for item in doublylist.iter():
        print(item)