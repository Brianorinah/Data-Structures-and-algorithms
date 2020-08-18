def binary_search(a_list, item):    
    #Nb binary_search using recursion can only be used to return True/False 
    #when an item is present but not its index because every binary_search recursive call passes in a new list with new indeces
    found = False    

    if len(a_list) == 0:
        return found
    else:
        midpoint = len(a_list) // 2
        if item == a_list[midpoint]:
            found = True
            
            return found
        else:
            if item < a_list[midpoint]:
                return binary_search(a_list[:midpoint],item)
            else:
                return binary_search(a_list[midpoint+1:],item)

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 19))
print(binary_search(test_list, 136))