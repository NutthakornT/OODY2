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

    def peek(self):
        return self.item[-1]
        pass

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def __str__(self):
        pass

    def copy(self):
        return Stack(self.item.copy())

    def turn_back(self):

        count = 0
        max_height = 0

        for h in reversed(self.item):
            if h > max_height:
                count += 1
                max_height = h
        return count

    def bro_is_drunk(self):
        new_list = Stack()
        minimum_height = 1
        # print(self.item)
        for i in self.item:
            if i == minimum_height:

                new_list.push(i)
            elif i % 2 == 0:
                i -= 1

                new_list.push(i)
            elif i % 2 == 1:
                i += 2

                new_list.push(i)
        # print(new_list.item)
        self.item = new_list.item
        # print(self.item)
        pass


# count = 0
trees_stack = Stack()
inp = input("Enter Input : ")
inp = inp.split(",")

for i in inp:
    if i[0] == "A":
        _, num = i.split(" ")
        trees_stack.push(int(num))
    elif i == "B":
        print(trees_stack.turn_back())
        pass
    elif i == "S":
        trees_stack.bro_is_drunk()
        pass
# print(trees_stack.item) # ['4', '3', '5', '8']
