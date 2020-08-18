from node import Node

class OrderedList():
    def __init__(self):
        self.head = None
    
    def __str__(self):
        return str(self.head)

    #Nb is-empty(), size() and remove() are implemented the same way as unordered list.
    #serach() and add()  only need traversal upto where the current > item

    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0

        while current != None:
            current = current.get_next()
            count = count +1
        
        return count
    
    def print_items(self):
        current = self.head
        index =0

        while current:            
            print("index:",index,"value:",current.get_data())
            current = current.get_next()
            index = index +1

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
            print("Index not found!!")


    def remove_at_pos(self,index):
        prev = None
        current = self.head
        i = 0

        while current and i<index:
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
            
    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.get_data() ==item:
                found = True
            
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def add(self,item):
        current = self.head
        prev = None
        stop = False

        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            
            else:
                prev = current
                current = current.get_next()
        
        temp = Node(item)
        if prev == None:
            temp.set_next(self.head)
            self.head = temp
        
        else:
            temp.set_next(current)
            prev.set_next(temp)
            



    

if __name__ == "__main__":
    mylist = OrderedList()
    mylist.add(20)
    mylist.add(39)
    mylist.add(5)
    mylist.add(77)
    mylist.add(46)
    mylist.add(66)
    mylist.remove_at_pos(0)       
    mylist.print_items()    
    print(mylist.size())