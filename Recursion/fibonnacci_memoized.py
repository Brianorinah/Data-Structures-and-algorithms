lookup_list = [None]*(100)

def fib(n , lookup):
    if lookup[n] is None:
        if n <= 2:
            lookup[n] = 1
        else:
            lookup[n] = fib(n-1 ,lookup) + fib(n-2 ,lookup)

    return lookup[n]

print(fib(40,lookup_list))
print("lookup_list:",lookup_list)

