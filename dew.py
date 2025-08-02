class Stack:
    def __init__(self, list_item=None):
        if list_item == None:
            list_item = []
        self.items = list_item
        self.size = len(self.items)

    def push(self, item):
        self.items.append(item)

    @property
    def pop_item(self):
        if len(self.items):
            return self.items.pop()
        print("Can't Pop It's Out of Range")
        return None

    @property
    def peek(self):
        return self.items[-1]

    @property
    def isEmpty(self):
        return len(self.items) == 0

    @property
    def size_list(self):
        return len(self.items)

    def __str__(self):
        s = "stack's size is " + str(self.size_list) + "\nlist :"
        for i in self.items:
            s += str(i) + " "
        return s + "\n"

    @property
    def sum(self):
        sum = 0
        try:
            for i in self.items:
                sum += i
            return sum
        except:
            # print("This is not pure Numberic Stack")
            return 0

    def reset(self, re_list=None):
        if re_list == None:
            re_list = []
        self.items = re_list.copy()

    def copy(self, stack: "Stack"):
        self.reset()
        store_stack = Stack()
        while stack.notEm:
            store_stack.push(stack.pop_item)
        while store_stack.notEm:
            self.push(store_stack.peek)
            stack.push(store_stack.pop_item)
        return self.items

    def sort(self):
        self.items.sort()

    @property
    def stack_re(self):
        a = Stack()
        while self.size_list > 0:
            a.push(self.pop_item)
        self.copy(a)

    @property
    def IsFloat(self):
        for i in self.items:
            if is_float(str(i)):
                return 1
        return 0

    @property
    def notEm(self):
        return not (self.isEmpty)


print("*****Big leg on the right side*****")
input = input("Enter input: ")
num = [int(i) for i in input.split(" ")]
out = [-1 for i in range(len(num))]
index_list = [j for j in range(len(num) - 1, -1, -1)]
purpeech = 1
stack = Stack()
for i in range(len(num)):
    # print(i)
    purpeech = 1
    if (
        stack.isEmpty or num[stack.peek] >= num[i]
    ):  # input < top stack == push # ตัวก่อน > ตัวหลัง ??
        stack.push(i)  # จนกว่าจะเจอตัวมากสุด
        print(f"Stack push {stack.peek} index of {num[stack.peek]}")
        purpeech = 0

    while (  #
        stack.notEm and num[stack.peek] < num[i]
    ):  # if input > stack ==pop util input < top of stack
        print(
            f"input[{i}]({num[i]}) is greater than input[top of stack]({num[stack.peek]})"
        )
        print("Stack pop")

        out[stack.pop_item] = num[i]

        print(f"Output: {out}")

        if (
            i != len(num) - 1
        ):  # กันไม่ให้มัน pop ไปเรื่อยๆ จนมัน หมด stack แล้วเขียน กรณีสุดท้ายไว้เป็นกรณีพิเศษปรับตามค่า purpeech
            stack.push(i)
            print(f"Stack push {stack.peek} index of {num[stack.peek]}")

    if purpeech and (
        (stack.isEmpty and i == len(num) - 1)
        or (num[stack.peek] >= num[i] and i == len(num) - 1)
    ):  # ถ้าตัว
        stack.push(i)
        print(f"Stack push {stack.peek} index of {num[stack.peek]}")
        print(f"Output: {out}")


if purpeech == 0:
    print(f"Output: {out}")
