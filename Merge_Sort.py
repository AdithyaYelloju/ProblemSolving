'''
Input array of number
Find mid element
find mid index, divide array into two
Merge both the arrays, have two pointers 
iterate through the arrays and add lower element to new array

Time complexity: O(n logn) and Space O(n)
'''

import sre_constants


def merge(left_array, right_array):
    sorted_array = []

    left_array_length = len(left_array)
    right_array_length = len(right_array)
    i = 0
    j = 0

    while(i < left_array_length and j < right_array_length):
        if(left_array[i] < right_array[j]):
            sorted_array.append(left_array[i])
            i += 1
        else:
            sorted_array.append(right_array[j])
            j += 1
    
    sorted_array.extend(left_array[i:])
    sorted_array.extend(right_array[j:])

    return sorted_array


def merge_sort(array, left, right):

    if(left == right):
        return array[left:left+1]
    
    mid = (left+right)//2

    left_sorted = merge_sort(array, left, mid)
    right_sorted = merge_sort(array, mid+1, right)

    print(array[left: right+1], left, right, mid, left_sorted, right_sorted)

    return merge(left_sorted, right_sorted)


array = [5,2,4,7,1,9,6]
print(merge_sort(array, 0, len(array)-1))
