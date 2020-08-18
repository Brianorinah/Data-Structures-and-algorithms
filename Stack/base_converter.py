from stack import Stack

def base_converter(dec_number, base):
    s = Stack()
    digits = "0123456789ABCDEF"

    while dec_number >0:
        rem = dec_number % base
        s.push(rem)
        dec_number = dec_number // 2
    
    new_str = ""

    while not s.is_empty():
        new_str = new_str + digits[s.pop()]

    return new_str
print(base_converter(25, 2))
print(base_converter(25, 16))