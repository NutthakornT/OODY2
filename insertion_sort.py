def insertion_sort(arr):
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i] #strat from arr[1]
        j = i - 1 #left side number

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j] #shift right until find spot
            j -= 1 # check next left num

        arr[j + 1] = key  #place that num
# Example usage:
numbers = [12, 11, 13, 5, 6]
print("Before sorting:", numbers)
insertion_sort(numbers)
print("After sorting: ", numbers)
# if i = 3 (5)
# j = 2 , arr[j] > key
# [11, 12, 13, 13, 6] shift
# j = 1 , arr[j] > key
#[11, 12, 12, 13, 6] shift
# j = 0, arr[j] > key
#[11, 11, 12, 13, 6]
# now j = -1 , j >= 0 , break
#arr[-1+1](0) then = key
#[5, 11, 12, 13, 6]


