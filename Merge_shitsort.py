def merge_sort(arr):
    # Base case: if the list is of length 0 or 1, it’s already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point
    mid = len(arr) // 2

    # Recursively divide and sort both halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    i = j = 0

    # Compare elements and build the merged list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:   
            merged.append(right[j])
            j += 1

    # Add any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# Example usage:
numbers = [5, 3, 6, 1, 2, 7, 8, 4]
print("Before sorting:", numbers)
sorted_numbers = merge_sort(numbers)
print("After sorting: ", sorted_numbers)
