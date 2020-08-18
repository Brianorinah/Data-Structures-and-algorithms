def binary_search(a_list, item):
    pos = 0
    last_index = len(a_list) -1
    first_index = 0
    found = False
    index = -1

    while first_index <= last_index and not found:
        midpoint = (first_index + last_index) // 2

        if item == a_list[midpoint]:
            index = midpoint
            found = True
        else:
            if item < a_list[midpoint]:
                last_index = midpoint -1
            else:
                first_index = midpoint + 1
    
        
    return index

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 17))
print(binary_search(test_list, 66))