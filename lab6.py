class Calculator:

    def __init__(self, number):
        self.number = number
        pass

    ### Enter Your Code Here ###
    # เรียง
    def __add__(self, other):
        return self.number + other.number
        ###Enter Your Code For Add Number###

    def __sub__(self, other):
        return self.number - other.number
        ###Enter Your Code For Sub Number###

    def __mul__(self, other):
        return self.number * other.number
        ###Enter Your Code For Mul Number###

    def __truediv__(self, other):
        return self.number / other.number
        ###Enter Your Code For Div Number###


x, y = input("Enter num1 num2 : ").split(",")

x, y = Calculator(int(x)), Calculator(int(y))

print(x + y, x - y, x * y, x / y, sep="\n")
