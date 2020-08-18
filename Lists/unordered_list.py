from node import Node
from collections import Counter


class UnorderedList:
    #Nb NodeObj.set_next() and set_data() can be simply be written as NodeObj.next since in the Node class the variables are not private
    #Same goes for get_next() and get_data()
    def __init__(self):
        self.head = None
        self.length = 0
    
    def __str__(self):
        return str(self.head)

    def is_empty(self):
        return self.head == None

    def add(self, item):
        new_node = Node(item)
        #Note the order of the following two lines
        #Exchanging them will lead to lose of data since the head is the only externa reference to the nodes
        #All of the original nodes will be lost and can no longer be accessed
        new_node.set_next(self.head)
        self.head = new_node
        self.length = self.length + 1

    def print_items(self):
        current = self.head
        index =0

        while current != None: 
            #Same with- while current:           
            print("index:",index,"value:",current.get_data())
            current = current.get_next()
            index = index +1
    
    def size(self):
        current = self.head
        count = 0

        while current != None:
            current = current.get_next()
            count = count +1
        
        return count

    def search(self,item):
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        
        return found

    def remove(self,item):
        current = self.head
        prev = None
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                #Note prev is first set to the current then the current is moved ahead.
                #if the inverse could happen both the current and prev would point to the same object 
                #and the algorithmn would not work. This process is called inch-worming                 
                prev = current
                current = current.get_next()

        if found:
            if prev == None:
                self.head = current.get_next()
            else:
                prev.set_next(current.get_next())
        else:
            print("Item not found!!")

    def remove_at_pos(self,index):
        prev = None
        current = self.head
        i = 0

        while current != None and i<index:
            prev = current
            current = current.get_next()
            i += 1

        if index == i:            
            if prev == None:
                self.head = current.get_next()
            else:
                prev.set_next(current.get_next())
        else:
            print('Index not found')


    def remove_duplicates(self):
        prev = None
        current = self.head
        counter_dict = Counter()

        while current:
            current_data = current.get_data()
            if counter_dict[current_data] == 0:
                counter_dict[current_data] = 1
            else:
                prev.set_next(current.get_next())
                                    
            prev = current
            current = current.get_next()
        print(counter_dict)

    def append(self,item):
        new_node = Node(item)
        current = self.head
        prev = None  

        if current is None:
            self.head = new_node         
        else:
            while current:
                prev = current
                current = current.get_next()

            if current == None:
                prev.set_next(new_node)
                new_node.set_next(None) 
    
   

if __name__ == "__main__":
    mylist = UnorderedList()
    mylist.add(20)
    mylist.add(77)
    mylist.add(23)
    mylist.add(434)
    mylist.add(24)
    mylist.add(24)
    mylist.add(77)
    mylist.add(24)
    mylist.append(2)
    #mylist.remove_at_pos(0)
    mylist.print_items()  
    # print("Initial size:",mylist.size())
    # print("Removing duplicates!!")
    # mylist.remove_duplicates()
    # mylist.size()     
    
    print("Finalsize:",mylist.size())

