def get_num(s):
    num = ""
    for n in s:
        
        if n.isdigit():  
            num += n
        
    if num:
        return (0, int(num), s)  #if equal = compare next
    else:
        return (1, 0, s)
    
    
    pass
def get_first(card):
    #priority
    c = 1
    d = 2
    h = 3
    s = 4
    if card[0] == "C":
        return c
    elif card[0]   == "D":
        return d
    elif card[0] == "H":
        return h
    elif card[0] == "S":
        return s
    
     
    
    pass
def find_index_max(arr,start_index,sort_by,end_index,current_index_max=None,i=None):
    if i is None:
        i = start_index
        current_index_max = start_index
    if i > end_index:
        return current_index_max
    
    if sort_by == "num":
        if get_num(arr[i]) > get_num(arr[current_index_max]): #find max
            current_index_max = i
    elif sort_by == "symbol":
        if get_first(arr[i]) > get_first(arr[current_index_max]): #find max
            current_index_max = i

    return find_index_max(arr,start_index,sort_by,end_index,current_index_max,i+1)
def selection_sort(arr,sort_by,end_index=None):
    if end_index is None:
        end_index = len(arr)-1
    if end_index <=0:
        # print(f"Sorted cards : {" ".join(arr)}")
        if sort_by == "symbol":
            for i in range(len(arr)-2):
                if arr[i][0] == arr[i+1][0]:
                    if arr[i][1].isdigit() and arr[i+1][1].isdigit():
                        if int(arr[i][1]) > int(arr[i+1][1]):
                            arr[i], arr[i+1]= arr[i+1],arr[i]
                        # print(f"Sorted cards : {" ".join(arr)}")
                        print("Sorted cards : ",end="")
                        for i in arr:
                            print(i,end=" ")
                        return
                        pass
                    elif (arr[i][1].isalpha() and arr[i+1][1].isdigit()) :
                        if ord(arr[i][1]) > int(arr[i+1][1]):
                            arr[i], arr[i+1]= arr[i+1],arr[i]
                        # print(f"Sorted cards : {" ".join(arr)}")
                        print("Sorted cards : ",end="")
                        for i in arr:
                            print(i,end=" ")
                        return
                        pass 
                    elif (arr[i][1].isdigit() and arr[i+1][1].isalpha()):
                        if int(arr[i][1]) > ord(arr[i+1][1]):
                            arr[i], arr[i+1]= arr[i+1],arr[i]
                        # print(f"Sorted cards : {" ".join(arr)}")
                        print("Sorted cards : ",end="")
                        for i in arr:
                            print(i,end=" ")
                        return
                        pass
                    elif (arr[i][1].isalpha() and arr[i+1][1].isalpha()):
                        if ord(arr[i][1]) > ord(arr[i+1][1]):
                            arr[i], arr[i+1]= arr[i+1],arr[i]
                        # print(f"Sorted cards : {" ".join(arr)}")
                        print("Sorted cards : ",end="")
                        for i in arr:
                            print(i,end=" ")
                        return
                        pass
        else:
            # print(f"Sorted cards : {" ".join(arr)}")
            print("Sorted cards : ",end="")
            for i in arr:
                print(i,end=" ")
            return


    
        
        return
    
    index_max= find_index_max(arr,0,sort_by,end_index)
    
    if index_max != end_index:
        # a, b = arr[end_index], arr[index_max]
        
               
        arr[end_index],arr[index_max] = arr[index_max],arr[end_index] 
        # print(arr)
        
    selection_sort(arr,sort_by,end_index-1)
    return

print("Have fun with sort card")
inp = input("Enter Input: ")
inp,sort_by = inp.split("/")
if not inp or not sort_by:
    print("No valid cards to sort.")
    quit()
inp = list(map(str,inp.split(",")))
# print(sort_by)

arr = []
for i in inp:
    if i in arr:
        print(f"Error: Duplicate card found - {i}")
    elif i[1].isalpha() and i[1] in "KAQJT" and i[0] in "CDHS":
        arr.append(i)
        continue
    elif len(i) > 2 or (i[0] not in "CDHS") or int(i[1]) > 9 or int(i[1])<2 :   
        print(f"Error: {i} is an invalid card")
    else:
        arr.append(i)

# print(arr)
if arr == []:
    print("No valid cards to sort.")
else:
    selection_sort(arr,sort_by)





        

