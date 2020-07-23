# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start <= end:
        mid = (end + start) // 2                            # find the middle so you can start with L & R sides
        if arr[mid] == target:                              # if the target is in the mid, great luck! stop.
            return mid
        elif arr[mid] < target:                             # if the target is LESS than mid:
            return binary_search(arr, target, mid+1, end)   # search again, moving around on the R side
        else:                                               # if the target is GREATER than mid:
            return binary_search(arr, target, start, mid-1) # search again, moving around on the L side 
        
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here