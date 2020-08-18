def fibonnacci_using_loops(n):
    #O(n) = O(n) linear    
    ls = [1,1]    

    for num in range(2,n):
        number= ls[num-1] + ls[num-2]
        ls.append(number)
    # ls[-1] is same as ls[len(ls)-1]
    print(ls[-1])

fibonnacci_using_loops(8)