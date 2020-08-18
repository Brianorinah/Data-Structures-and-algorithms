def quick_sort(a_list):
    #O(n) is O(nlogn) but may degrade to O(nlogn) if the pivot point is completely skewed to either the left or the right
    quick_sort_helper(a_list,0, len(a_list)-1)

def quick_sort_helper(a_list , first, last):
    #begins with the same base case as the merge sort. If the length of the
    # list is less than or equal to one, it is already sorted. If it is greater, then it can be partitioned and
    # recursively sorted.
    if first < last:
        #Get the split value
        split_point = partition(a_list,first,last)

        #splitting the two lists on the split value
        quick_sort_helper(a_list,first, split_point -1)
        quick_sort_helper(a_list, split_point + 1 , last)

#getting the split value
def partition(a_list, first, last):
    pivot_value = a_list[first]

    left_mark = first + 1
    right_mark = last
    done = False

    while not done:

        #Find a value bigger than the pivot value
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark +1

        #Find a value smaller than the pivot value
        while right_mark >= left_mark and a_list[right_mark] >= pivot_value:
            right_mark = right_mark -1

        #Exit the loop if the right index becomes smaller than the left index
        if right_mark < left_mark:
            done = True
        
        #Exchenge the right_mark(smaller than the pivot value) with the left_mark(bigger than the pivot value)
        else:
            a_list[right_mark] ,a_list[left_mark] = a_list[left_mark], a_list[right_mark]

    #move the pivot value to the split point
    a_list[first] , a_list[right_mark] =a_list[right_mark] , a_list[first] 

    return right_mark

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)