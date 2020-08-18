def move(n ,src ,dest ,temp):
    #O(n) = O(n ^ 2) exponential
    if n >= 1 :
        move(n-1 ,src ,temp ,dest)
        print( f"Move {src} -> {dest}" )
        move(n-1 ,temp ,dest ,src)

move(4 ,"A","C", "B")

