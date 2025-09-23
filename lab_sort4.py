def get_char(s):
    
    for ch in s:
        if 'a' <= ch <= 'z':
            return ch
    return None

def bubble_sort(arr):
    
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if get_char(arr[j]) > get_char(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


data = input("Enter Input : ").split()
result = bubble_sort(data)
print(" ".join(result))
