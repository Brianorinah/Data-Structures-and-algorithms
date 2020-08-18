def merge_sort(ls):  
    if len(ls) > 1:  
        midpoint = len(ls) // 2

        first_half = ls[:midpoint]
        second_half = ls[midpoint:]

        merge_sort(first_half)
        merge_sort(second_half)

        merger(first_half,second_half,ls)

def merger(ls1,ls2,result):       
    i=0
    j=0
    k=0
        
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

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)