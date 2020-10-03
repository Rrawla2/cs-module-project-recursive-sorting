# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if end >= start:
        middle = (start + end) // 2

        # checks if the middle happens to be the value we're searching for and returns it
        if arr[middle] == target:
            return middle
        # checks if the middle is bigger than the target
        # if it is run binary_search again decreasing by 1 to set a new end value
        elif arr[middle] > target:
            return binary_search(arr, target, start, middle - 1)  # set new end here
        # otherwise the middle is smaller than the target
        # run binary_search again increasing by 1 to set a new start value
        else:
            return binary_search(arr, target,  middle + 1, end)  # set new start here
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here
