from stack import Stack

def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '({[':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced =False
            else:
                top = s.pop()

                if not matches(top,symbol):
                    balanced =False
        index = index + 1
        
    if s.is_empty() and balanced:
        return True
    else:
        return False

def matches(top,symbol):
    opens= '({['
    closings =')}]'

    if opens.index(top) == closings.index(symbol):
        return True
    else:
        return False


str1 ='{{([][])}()}'
str2 ='[{()]'
print(par_checker(str1))
print(par_checker(str2))


# def isValidSource( srcfile ):
#     s = Stack()
#     for line in srcfile :
#         for token in line :
#             if token in "{[(" :
#                 s.push( token )
#             elif token in "}])" :
#                 if s.isEmpty() :
#                     return False
#             else :
#                 left = s.pop()
#                 if (token == "}" and left != "{") or \
#                 (token == "]" and left != "[") or \
#                 (token == ")" and left != "(") :
#                     return False

#     return s.isEmpty()

# This C++ file is the srcfile
# int sumList( int theList[], int size )
# {
# int sum = 0;
# int i = 0;
# while( i < size ) {
# sum += theList[ i ];
# i += 1;
# }
# return sum;
# }