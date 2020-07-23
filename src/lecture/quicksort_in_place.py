def quick_sort(data, low, high):
    # base case
    if low >= high:
        return data
    # recursive case
    else:
        # divide
        pivot_index = low
        # for each element in subarray
        for i in range(low, high):
            if data[i] < data[pivot_index]:
                # double swap to move smaller elements to correct index
                # move current element to R of pivot
                temp = data[pivot_index+1]
                data[pivot_index+1] = data[i]
                data[i] = temp

                # swap pivot with element on R
                temp = data[pivot_index]
                data[pivot_index] = data[pivot_index+1]
                data[pivot_index+1] = temp
                pivot_index += 1

        # conquer
        # Quick Sort everything L of pivot
        data = quick_sort(data, low, pivot_index)
        # Quick Sort everything R of pivot
        data = quick_sort(data, pivot_index+1, high)

        return data