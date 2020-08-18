from stack import Stack

def divide_by_2(dec_number):
    s = Stack()

    while dec_number > 0:
        rem = dec_number%2
        s.push(rem)
        dec_number = dec_number //2
    
    binary_str = ""

    while not s.is_empty():
        binary_str = binary_str + str(s.pop())
    
    return binary_str

print(divide_by_2(42))