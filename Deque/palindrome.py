from deque import Deque

def pal_checker(a_string):
    d = Deque()

    for char in a_string:
        d.add_rear(char)   
    

    is_same = True
    while d.size() > 1 and is_same:
        front = d.remove_front()
        rear = d.remove_rear()
        if  front != rear:
            is_same = False
        
    return is_same

print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))