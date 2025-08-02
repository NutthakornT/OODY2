class Stack:
    def __init__(self, list=None):
        if list == None:
            self.item = []
        else:
            self.item = list
        pass

    def push(self, data):
        return self.item.append(data)

    def pop(self, that_item=None):
        if that_item == None:
            return self.item.pop()
        else:
            return self.item.pop(that_item)

    def peek(self):
        return self.item[-1]

    def is_Empty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def __str__(self):
        s = ""
        for ele in self.item:
            s += str(ele) + " "
        return s
        pass


# print("***Always 5 or 10***")
# str_lst = input("Enter Input : ")
# numbers = list(map(int, str_lst.split()))
# stack = []


# for num in numbers:
#     if len(stack) == 0:
#         stack.append(num)
#     else:
#         top = stack[-1]
#         if (
#             abs(top - num) == 5
#             or top + num == 10
#             or top + num == 5
#             or abs(top - num) == 10
#         ):
#             stack.append(num)

# print("Output : ", end="")
# for i in stack:
#     print(i, end=" ")

print("***Always 5 or 10***")
str_lst = input("Enter Input : ")
numbers = list(map(int, str_lst.split()))
# print(numbers)
stack = Stack()
for num in numbers:
    if stack.is_Empty():
        stack.push(num)
    else:
        top = stack.peek()
        if (
            abs(top - num) == 5
            or top + num == 5
            or abs(top - num) == 10
            or top + num == 10
        ):
            stack.push(num)

print(stack)
# print(stack.item)
