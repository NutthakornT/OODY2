class Queue:
    def __init__(self):
        self.main_queue = []
        self.sub_queue = {}
        pass

    def enqueue(self, number):
        id_front = number[0]  # 2 in 201
        # print(type(id_front))
        if id_front not in self.main_queue:  # in ["2","1"]?????
            self.sub_queue[id_front] = []  # {key:[201,202], key:[101,202]}
            self.main_queue.append(id_front)

        self.sub_queue[id_front].append(int(number))
        print(f"Enqueued: {number}")
        # print
        update_queue = []
        for member in self.main_queue:
            update_queue.append(self.sub_queue[member])
        pass

        print(f"Queue state: {update_queue}")

    def dequeue(self):
        if not self.main_queue:
            return print("Queue is empty")
        team_number = self.main_queue[0]  # ["2", "1"]
        member = self.sub_queue[team_number].pop(0)
        print(f"Dequeued: {member}")
        if not self.sub_queue[team_number]:
            self.main_queue.pop(0)
        # print
        update_queue = []
        for member in self.main_queue:
            update_queue.append(self.sub_queue[member])

        print(f"Queue state: {update_queue}")


print(" ***Queue of Queue of Queue of ...*** ")
inp = input("Enter Input : ")
q = Queue()
# print(inp)
for i in inp.split(","):

    if i[0] == "e" and i[1] == "n":
        com, num = i.split(" ")
        q.enqueue(num)
    else:
        q.dequeue()
