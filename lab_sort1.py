inp = input("Enter Input : ")
check = True
inp = list(map(int,inp.split(" ")))

def check_sort(lst):
    ascen = True
    desen = True

    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]: #des
            ascen = False
       
        if lst[i] < lst[i+1]: #asc
            desen = False
        
    return ascen or desen #if both flase = boom!
print("No" if not check_sort(inp) else "Yes")