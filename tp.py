class Queue:
    def __init__(self, list=None):
        if list == None:
            self.item = []
        else:
            self.item = list

    def dequeue(self):
        return self.item.pop(0)

    def enqueue(self, data):
        return self.item.append(data)

    def is_Empty(self):
        return self.item == []

    def peek(self):
        if len(self.item) == 0:
            return None
        else:
            return self.item[0]

    def size(self):
        return len(self.item)

    def __str__(self):
        s = ""
        for i in self.item:

            s += i + " "
        return s
        pass


inp = input("Enter Input : ")
inp = inp.split(",")
# print(inp)
queue = Queue()

for i in inp:
    if i == "D":
        cmd = i
        if queue.is_Empty():
            print(queue.size() - 1)
        else:

            front_then = queue.peek()
            queue.dequeue()
            size_after = queue.size()
            print(f"Pop {front_then} size in queue is {size_after}")

    else:
        cmd, num = i.split(" ")
        index = queue.size()
        queue.enqueue(num)
        print(f"Add {num} index is {index}")
    # print(cmd)

if not queue.is_Empty():
    print(f"Number in Queue is :  {queue}")
else:
    print("Empty")
