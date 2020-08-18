def sum_of_list(ls):
    if len(ls) == 1:
        return ls[0]
    else:
        return ls[0] + sum_of_list(ls[1:])


print(sum_of_list([1,2,3,4,5]))