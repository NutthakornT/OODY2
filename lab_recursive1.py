def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    pass
inp = input("Enter Number : ")
print(f"fibo({int(inp)}) = {fibo(int(inp))}")