def bubble_sort(a):
    last_index = len(a) - 1  # array size = n
    swapped = True

    while last_index >= 1 and swapped:
        swapped = False
        i = 0
        while i < last_index:
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]  # swap
                swapped = True
            i += 1
        last_index -= 1


# Example usage
arr = [5, 3, 8, 4, 2]
bubble_sort(arr)
print("Sorted array:", arr)