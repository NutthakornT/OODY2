def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    return 



def find_weight_purify(n,weight):
    # base case 
    if n == 1:
        if weight>0:
            return weight
        else:
            return -1
        
    ck = fibo(n-1)
    

    #(a+b+ck)//2 = weight --> a+b = weight * 2 - ck
    start_min = weight*2 - ck # min a+b
    end_max = ((weight*2) - ck) + 1 #max a+b
    a = end_max//2
    b = end_max - a
    pw_a = find_weight_purify(n-1,a)
    pw_b = find_weight_purify(n-1,b) 
    if pw_a == -1 or pw_b == -1: #from base case
        return -1
    
    stone_weight = pw_a + pw_b
    return stone_weight
    pass

n,w = input("Purity and Weight needed: ").split(" ")
print(f"Total weight of used minerals with Purity 1 : {find_weight_purify(int(n),int(w))}")

# แร่จะมีน้ำหนักเป็นจำนวนเต็มบวกเสมอ    

