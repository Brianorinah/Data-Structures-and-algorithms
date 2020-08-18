def bubble_sort(a_list):
    #O(n) = O(n^2)
    did_change_pos = True
    pass_num = len(a_list) -1

    while pass_num > 0 and did_change_pos:
        did_change_pos = False
        for i in range(pass_num):
            if a_list[i] > a_list[i+1]:
                did_change_pos = True
                a_list[i] , a_list[i+1] = a_list[i+1] ,a_list[i]

                #unpythonic exchange using temporary position                
                # temp = a_list[i]
                # a_list[i] = a_list[i+1]
                # a_list[i+1] =temp
                
        pass_num = pass_num - 1

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(a_list)
print(a_list)
                 