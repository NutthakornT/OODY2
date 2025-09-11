def lucky_number(num,counter = 1):
    sum = summing(num)
    
    if sum < 10:
        print(f"Lucky Number: {sum}")
    else:
        print(f"Sum #{counter} : {sum}")
        
        return lucky_number(sum,counter+1)
        pass
        

    pass

def summing(num,carry = 0): #sum each digit
    if num < 10:
        return num + carry
        pass
    else:
        carry += num % 10 # 6 
        num = num // 10     #66
        return summing(num,carry)   
        pass


inp = input("Enter Input: ")
lucky_number(int(inp))