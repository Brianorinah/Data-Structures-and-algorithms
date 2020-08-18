def fib(n):
    #O(n^2) Exponential
    #Nb looping is actually faster O(n)
    
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))