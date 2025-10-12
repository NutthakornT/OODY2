def find_index_max(arr,start_index,end_index,current_index_max=None,i=None):
    if i is None:
        i = start_index #0
        current_index_max = start_index
    if i > end_index:
        return current_index_max # found
    if arr[i] > arr[current_index_max]: #find max
        current_index_max = i
    
    return find_index_max(arr,start_index,end_index,current_index_max,i+1)
def selection_sort(arr,end_index=None):
    if end_index is None: #set up end index
        end_index = len(arr)-1
    if end_index <=0: 
        print(arr)
        return
    
    index_max= find_index_max(arr,0,end_index)
    
    if index_max != end_index:
        a, b = arr[end_index], arr[index_max]
        arr[end_index],arr[index_max] = arr[index_max],arr[end_index] 
        print(f"swap {a} <-> {b} : {arr}")
    selection_sort(arr,end_index-1)
    return


inp = input("Enter Input : ")
inp = list(map(int,inp.split(" ")))
selection_sort(inp)
# print(inp)
# min swap kub first