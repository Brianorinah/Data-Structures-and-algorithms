def exp(x,n):
    #O(n) = O(log n) logarithmic
        return 1
    
    result = exp(x * x, n //2)

    if n % 2 ==0:
        return result
    else:
        return x * result

print(exp(2,4))