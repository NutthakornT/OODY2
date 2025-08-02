class Queue:
    def __init__(self, init_list=[]):
        self.item = init_list

    def enqueue(self, data):
        return self.item.append(data)
        pass

    def dequeue(self):
        return self.item.pop(0)
        pass

    def take_paper_out(self):
        return self.item.pop()

    def peek(self):
        if not self.item:
            return None
        return self.item[0]  # ใช้ดูตัวแรกของ Queue
        pass

    @property
    def isEmpty(self):
        return self.item == []

    @property
    def size(self):
        return len(self.item)

    def __str__(self):
        return str(self.item)


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


inp = input("Enter input: ")
inp = inp.split(", ")

status = ""
previous_line = ""
next_line = ""
pending = Queue()
paper_remain = 3
tray = Queue()
max_queue = 3


# print(inp)
# find max time
timelst = []
for i in inp:
    if i[0] == "P":
        cmd, rest = i.split(":")
        time, word = rest.split(" ", 1)
        # print(word)
        timelst.append(int(time))
    elif i[0] == "R":
        cmd, rest = i.split(":")
        time, refill_amount = rest.split(" ")
        timelst.append(int(time))
    else:
        cmd, time = i.split(":")
        timelst.append(int(time))
max_time = max(timelst)
# print(f"max_time = {max_time}")

# make dic {0, [('P',word)]}
event = {}
for i in inp:
    if i[0] == "P":
        cmd, rest = i.split(":")
        time, word = rest.split(" ", 1)
        time = int(time)
        if time not in event:
            event[time] = []
        event[time].append((cmd, word))

    elif i[0] == "R":
        cmd, rest = i.split(":")
        time, refill_amount = rest.split(" ")
        time = int(time)
        if time not in event:
            event[time] = []
        event[time].append((cmd, int(refill_amount)))

    else:
        cmd, time = i.split(":")
        time = int(time)
        if time not in event:
            event[time] = []
        event[time].append((cmd, time))


print(event)
# {0: [('P', 'Sawaddee'), ('P', 'Hello')], 3: [('P', 'Abcdfg')], 4: [('P', 'GGEZCU0'), ('T', 4)], 5: [('T', 5)], 6: [('T', 6)], 7: [('T', 7)]}
pass
################################################
for second in range(max_time):
    # previous_line += status
    # if next_line != "":
    #     status = next_line[0:5]
    #     if len(next_line) > 5:
    #         next_line = next_line[5:]
    #     else:
    #         next_line = ""
    # elif next_line == "" and previous_line != "":
    #     tray.enqueue(previous_line)
    #     paper_remain -= 1

    #     pass
    previous_line += status
    # have next line
    if next_line != "":
        status = next_line[0:5]
        if len(next_line) > 5:
            next_line = next_line[5:]
        else:
            next_line = ""
    # dont have next line check pending
    elif next_line == "" and previous_line != "":
        tray.enqueue(previous_line)
        paper_remain -= 1
        if pending.isEmpty():
            status = ""
        elif paper_remain > 0:
            status = pending.dequeue()
            if len(status) > 5:
                next_line = status[5:]
                status = status[0:5]
        elif paper_remain == 0:
            status = ""
        previous_line = ""

    elif (
        previous_line == ""
        and next_line == ""
        and status == ""
        and paper_remain != 0
        and not pending.isEmpty()
    ):
        status = pending.dequeue()
        if len(status) > 5:
            next_line = status[5:]
            status = status[0:5]

    if second in event:

        for cmd, data in event[second]:
            if cmd == "S":
                if paper_remain == 0:
                    print(
                        f"[Time {second}] Error: Printer is out of paper. Please refill."
                    )
                if status == "":
                    print(
                        f"[Time {second}] Status: Idle. Pending {pending.size} file(s) in queue."
                    )
                    pass
                else:
                    print(
                        # previous + status + nextline
                        f"[Time {second}] Status: Printing... {previous_line+status+next_line} and Pending {pending.size} file(s) in queue."
                    )
                    pass
            elif cmd == "R":
                paper_remain += data
                pass
            elif cmd == "T":
                if tray.isEmpty:
                    print(f"[Time {second}] You got: Nothing in tray.")
                else:
                    stack = Stack()
                    output = []
                    while not tray.isEmpty:
                        stack.push(tray.dequeue())
                    while not stack.isEmpty():
                        output.append(stack.pop())

                    pass

            elif cmd == "P":
                if status == "":
                    if len(data) > 5:
                        status = data[0:5]
                        next_line = data[5:]
                    else:
                        status = data

                else:
                    if pending.size < max_queue:
                        pending.enqueue(data)
                    else:
                        print(
                            f"[Time {second}] Error: Printer buffer is full. Please try again later."
                        )
                    pass

                pass
            # print(second)
            # print(f"Status ---> {status}")
            # print(f"previous_line ---> {previous_line}")
            # print(f"next_line ---> {next_line}")
            # print(pending.item)
            pass

    pass

# for i in inp:
#     if i[0] == "P":
#         _, d = i.split(":")
#         time, word = d.split(" ")
#         print(time)
#         print(word)
#         pass
#     elif i[0] == "T":

#         pass
#     elif i[0] == "S":

#         pass
#     elif i[0] == "R":

#         pass
#     pass
