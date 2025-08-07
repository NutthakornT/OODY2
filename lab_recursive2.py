def lucky_number(num,counter = 1):
    sum = summing(num)
    
    if sum < 10:
        print(f"Lucky Number: {sum}")
    else:
        print(f"Sum #{counter} : {sum}")
        counter += 1
        return lucky_number(sum,counter)
        pass
        

    pass

def summing(num,carry = 0):
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