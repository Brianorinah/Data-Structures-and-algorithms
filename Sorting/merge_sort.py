
def merge_sort(a_list):
    #O(n) = O(nlogn)
    if len(a_list) > 1 :
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        #splitting the list
        merge_sort(left_half)
        merge_sort(right_half)

        #joining the two sorted lists
        merge_sorted_lists(left_half,right_half ,a_list)

def merge_sorted_lists(left_half,right_half ,a_list):
        i = 0
        j = 0
        k = 0 

        #Merge the two lists together until one is empty.
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1
        
        #If left_half contains more items, append them to a_list.
        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        #or if right_half contains more items, append them to a_list.
        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
        
        print("Merging ", a_list)
        
        return a_list


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)





        