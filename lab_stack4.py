class Stack:
    def __init__(self, list=None):
        if list == None:
            self.item = []
        else:
            self.item = list

    def push(self, data):
        return self.item.append(data)
        pass

    def pop(self, that_item=None):
        if that_item is None:
            return self.item.pop()
        else:
            return self.item.remove(that_item)

        pass

    @property
    def peek(self):
        return self.item[-1]
        pass

    @property
    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def __str__(self):
        pass

    def copy(self):
        return Stack(self.item.copy())


print("*****Big leg on the right side*****")
inp = input("Enter input: ")
num = list(map(int, [i for i in inp.split(" ")]))
out = [-1 for _ in range(len(num))]
top_stack = Stack()
# [5, 4, 3, 2, 1, 0, 6]
for i in range(len(num)):  # i = 0 1 2 3...
    # print(i)
    if (
        top_stack.isEmpty
        or num[top_stack.peek]
        >= num[i]  # num[0] >= num[1] ? 5 >= 4 --> still not the num we need
    ):  # find num[i] that more than num[top_stack]
        top_stack.push(i)
        print(f"Stack push {i} index of {num[i]}")
    # found the number that is more than
    # top_stack = [0, 1, 2, 3, 4, 5]
    # i = 6
    while not top_stack.isEmpty and num[top_stack.peek] < num[i]:
        print(
            f"input[{i}]({num[i]}) is greater than input[top of stack]({num[top_stack.peek]})"
        )
        print("Stack pop")
        out[top_stack.pop()] = num[i]  # out[5] = num[6](6)

        print(f"Output: {out}")

        if i != len(num) - 1:  # ถ้าไม่ใช่ตัวท้ายให้ push ไปไม่งั้นมันข้่าม index i
            top_stack.push(i)
            print(f"Stack push {top_stack.peek} index of {num[top_stack.peek]}")
        pass

    pass
    # last line
    if top_stack.isEmpty and i == len(num) - 1:  # last i
        top_stack.push(i)
        print(f"Stack push {i} index of {num[i]}")
        pass

    # print(top_stack.item)

print(f"Output: {out}")

# print(top_stack.item)
