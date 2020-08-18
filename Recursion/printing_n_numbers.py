def number_printer(n):
    if n > 0:        
        number_printer(n-1)
        print(n)
        
        #printing in descending order(Invert the two statements)
        #print(n)
        #number_printer(n-1)

number_printer(4)