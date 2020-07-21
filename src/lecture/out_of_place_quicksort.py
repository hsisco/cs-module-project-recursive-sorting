'''
Out-of-place Quicksort
'''
def partition(data):
    # Partition the data
    # choose a pivot (choose the first item in the list)
    pivot = data[0]
    # create storage for L and R
    left = []
    right = []

    # loop through each item
    for current in data[1:]:
        # if item is smaller or equal, append to L
        if current <= pivot:
            left.append(current)
        # if item is bigger, append to R
        else:
            right.append(current)

    return left, right, pivot

'''
    What kind of input will we get? 
        We expect a list
'''
def quicksort(data):
    # check if data has 1 or 0 elements
    # (base case) a side only contains a single element
    if len(data) <= 1:
        return data

    left, right, pivot = partition(data)

    # (recursive case) Recursively Quick Sort L and R until
    return quicksort(left) + [pivot] + quicksort(right)

quicksort([2,5,7,1,3,4,6,9,8])