def quick_sort(arr):
    """Sorts a list using the Quick Sort algorithm."""
    _quick_sort_recursive(arr, 0, len(arr) - 1)

def _quick_sort_recursive(arr, left, right):
    """Recursive helper function for quick_sort."""
    if left < right:
        # Partition the array and get the pivot's final index
        pivot_index = partition(arr, left, right)
        # Recursively sort the two sub-arrays
        _quick_sort_recursive(arr, left, pivot_index - 1)
        _quick_sort_recursive(arr, pivot_index + 1, right)

def partition(arr, left, right):
    """Partitions the array and returns the pivot's final index."""
    # --- Median of Three Pivot Selection ---
    center = (left + right) // 2
    # Sort the left, center, and right elements
    if arr[left] > arr[center]:
        arr[left], arr[center] = arr[center], arr[left]
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[center] > arr[right]:
        arr[center], arr[right] = arr[right], arr[center]

    # Place the median (at arr[center]) at the start to act as the pivot
    arr[left], arr[center] = arr[center], arr[left]
    pivot = arr[left]

    # --- Partitioning ---
    i = left + 1  # Left pointer
    j = right     # Right pointer

    while i <= j:
        # Find element on left that should be on right
        while i <= j and arr[i] <= pivot:
            i += 1
        # Find element on right that should be on left
        while i <= j and arr[j] >= pivot:
            j -= 1
        # Swap elements if pointers haven't crossed
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot into its final sorted position
    arr[left], arr[j] = arr[j], arr[left]
    return j  # Return the pivot's index

# --- Test the Quick Sort implementation ---
if __name__ == "__main__":
    # Input list from your example
    my_list = [5, 1, 4, 9, 6, 3, 8, 2, 7, 0]
    
    print(f"Original list: {my_list}")
    
    # Sort the list
    quick_sort(my_list)
    
    print(f"Sorted list:   {my_list}")