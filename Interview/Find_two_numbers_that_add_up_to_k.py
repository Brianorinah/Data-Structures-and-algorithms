def binary_search(ls,k):
    first = 0
    last = len(ls) -1
    found = False
    index = -1

    while first <= last and not found:
        midpoint = (first + last) // 2
        if k == ls[midpoint]:
            index = midpoint
            found = True
            return index
        else:
            if k < ls[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    
    return index

def findSum(lst, k):
    s = set()

    for i in range(len(lst)):
        temp = k - lst[i]
        if temp in s:
            print (lst[i],temp)
        s.add(lst[i])

    # lst.sort()

    # for j in range(len(lst)):
    #     found_index = binary_search(lst,k-lst[j])
    #     if found_index != -1 and found_index != j:
    #         print([lst[j],k-lst[j]])
    

#print(findSum([1, 5, 3], 2))

findSum([1, 2, 3, 4, 5, 7], 5)
