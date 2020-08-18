def shell_sort(a_list):
    increment= len(a_list) // 2
    while increment> 0:
        for start_position in range(increment):
            gap_insertion_sort(a_list, start_position, increment)
        print("After increments of size", increment, "The list is", a_list)

        increment= increment// 2

def gap_insertion_sort(a_list, start, gap):
    for index in range(start + gap, len(a_list), gap):
        current_value = a_list[index]
        current_position = index

        while current_position > 0 and a_list[current_position-1] > current_value:
            a_list[current_position] = a_list[current_position - 1]
            current_position = current_position - 1

        a_list[current_position] = current_value

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a_list)
print(a_list)

