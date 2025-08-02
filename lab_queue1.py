class Queue:
    def __init__(self, list=None):
        if list == None:
            self.item = []
        else:
            self.item = list
        pass

    def enqueue(self, data):
        return self.item.append(data)

    def dequeue(self):
        return self.item.pop(0)

    def copy(self):
        return Queue(self.item.copy())

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.item == []


inp = input("Enter Input : ")
inp = inp.split(",")
number_queue = Queue()
# print(inp)  # ['E 10', 'E 20', 'E 30', 'E 40', 'D', 'D']
count = 0
for i in inp:
    sep = i.split()

    if len(sep) > 1 and sep[-1].isdigit():
        number_queue.enqueue(int(sep[-1]))
        print(f"Add {sep[-1]} index is {(number_queue.size())-1}")

    if i == "D":
        if number_queue.size() > 0:
            number_to_pop = number_queue.item[0]
            number_queue.dequeue()
            print(f"Pop {number_to_pop} size in queue is {number_queue.size()}")
        else:
            print(number_queue.size() - 1)


if number_queue.size() > 0:
    print(f"Number in Queue is :  {list(map(str,number_queue.item))}")
else:
    print("Empty")
