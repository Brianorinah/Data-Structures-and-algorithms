def insertion_sort(a_list):
    for index in range(1,len(a_list)):
        current_value = a_list[index]
        current_position = index
        while current_position > 0 and a_list[current_position-1] > current_value:
            a_list[current_position] = a_list[current_position - 1]
            current_position = current_position - 1

        a_list[current_position] = current_value

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print(a_list)