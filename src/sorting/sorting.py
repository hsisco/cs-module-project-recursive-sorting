# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    merged_arr = [] # * elements            # instantiate new array for values
    a, b = 0, 0                             # set each array item to 0 to start

    while a < len(arrA) and b < len(arrB):  # while the item key is within the array length for both arrays (meaning it can exist within the array):
        if arrA[a] < arrB[b]:               # if the item from A is greater than the item from B:
            merged_arr.append(arrA[a])      # add it to the new array
            a += 1                          # go to the next item
        else:
            merged_arr.append(arrB[b])      # add it to the new array
            b += 1                          # go to the next item
#       Basically, just add them all
    while a < len(arrA):                    # if the item can exist within the array:
        merged_arr.append(arrA[a])          # add it to the new array
        a += 1                              # go to the next item

    while b < len(arrB):                    # if the item can exist within the array:
        merged_arr.append(arrB[b])          # add it to the new array
        b += 1                              # go to the next item

    return merged_arr                       # Ta-Da! new array

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2                 # find the starting point
        l = arr[:mid]                       # separate the array into 2 sides
        r = arr[mid:]

        l = merge_sort(l)                   # create increasingly smaller groups to run merge_sort
        r = merge_sort(r)

        arr = merge(l,r)                    # merge them together

    return arr                              # Ta-Da! new array

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here