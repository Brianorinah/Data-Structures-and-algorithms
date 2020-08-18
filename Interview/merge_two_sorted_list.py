def merger(ls1,ls2):
    result= []
    i=0
    j=0
    k=0
    for i in range(len(ls1)+len(ls2)):
        result.append(i)
    
    while i < len(ls1) and j < len(ls2):
        if ls1[i] < ls2[j]:
            result[k] = ls1[i]
            i = i + 1
        else:
            result[k] = ls2[j]
            j = j + 1
        k = k + 1
    
    while i < len(ls1):
        result[k] = ls1[i]
        i = i + 1
        k = k + 1
        
    while j < len(ls2):
        result[k] = ls2[j]
        j = j + 1
        k = k + 1
        
    return result

print(merger([4, 5, 6], [-2, -1, 0, 7]))