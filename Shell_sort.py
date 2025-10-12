def shell(l, dIncrements):
    for inc in dIncrements:  # for each diminishing increment
        for i in range(inc, len(l)):  # insertion sort
            iEle = l[i]  # element to insert

            for j in range(i, -1, -inc):
                if j >= inc and l[j - inc] > iEle:
                    l[j] = l[j - inc]
                else:
                    l[j] = iEle
                    break


l = [10, 11, 1, 13, 2, 6, 4, 12, 5, 8, 7, 9, 3]
dIncrements = [5, 3, 1]
shell(l, dIncrements)
print(l)

def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # start with a big gap, then reduce it

    # Keep reducing the gap until it becomes 0
    while gap > 0:
        # Perform a gapped insertion sort
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # Put temp (the original arr[i]) in its correct location
            arr[j] = temp

        gap //= 2  # reduce the gap

# Example usage:
numbers = [9, 8, 3, 7, 5, 6, 4, 1]
print("Before sorting:", numbers)
shell_sort(numbers)
print("After sorting: ", numbers)
