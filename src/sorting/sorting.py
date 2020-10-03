# merge sort
# **********
# [5, 9, 3, 7, 2, 8, 1, 6]
# split it in 2
# Phase 1: calling down the recursion
# [5, 9, 3, 7] [2, 8, 1, 6]
# [5, 9] [3, 7] [2, 8] [1,6]
# [5] [9] [3] [7] [2] [8] [1] [6]
# Phase 2: Merge them back together
# [5] [9] [3] [7] [2] [8] [1] [6]
# [5, 9] [3, 7] [2, 8] [1, 6]
# [3, 5, 7, 9] [1, 2, 6, 8]
# [1, 2, 3, 5, 6, 7, 8, 9]

# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    counter_1 = 0
    counter_2 = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range(0, elements):
        if counter_1 >= len(arrA):  # all elements in arrA have been merged
            merged_arr[i] = arrB[counter_2]
            counter_2 += 1
        elif counter_2 >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[counter_1]
            counter_1 += 1
        elif arrA[counter_1] < arrB[counter_2]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[counter_1]
            counter_1 += 1
        else:
            merged_arr[i] = arrB[counter_2]
            counter_2 += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    # If the array has 1 item, it's already sorted - return the array
    if len(arr) == 1:
        return arr
    # if the array has more than 1 item, split it in 2
    if len(arr) > 1:
        # get the middle of the array
        middle = len(arr) // 2
        # slice from index 0 to the middle
        left = merge_sort(arr[0:middle])
        # slice from middle to the last index
        right = merge_sort(arr[middle:])
        # arr = left + right - use helper to merge these together
        arr = merge(left, right)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#
#
# def merge_sort_in_place(arr, l, r):
#     # Your code here
