class Queue:
    def __init__(self, list=None):
        if list == None:
            self.item = []
        else:
            self.item = list

    def enQueue(self, i):
        self.item.append(i)

    @property
    def deQueue(self):
        return self.item.pop(0)

    @property
    def peek(self):
        return self.item[0]

    @property
    def size(self):
        return len(self.item)

    @property
    def isEmpty(self):
        return len(self.item) == 0

    def __str__(self):
        s = ""
        for i in self.item:
            s += str(i)
            s += " "
        return s


class Stack:
    def __init__(self, list=None):
        if list == None:
            self.item = []
        else:
            self.item = list

    def push(self, i):
        self.item.append(i)

    @property
    def pop(self):
        return self.item.pop()

    @property
    def peek(self):
        return self.item[-1]

    @property
    def size(self):
        return len(self.item)

    def __str__(self):
        return str(self.item)


def printting(message):
    # print(message)
    paper = 3
    paperStack = Stack()
    printtingQ = Queue()
    pre_time = 0
    printed = False
    for item in message:
        # print(f'item: {item}')
        command, value = item.split(":")
        if value[0:2].isdigit():
            cur_time = int(value[0:2])
        else:
            cur_time = int(value[0])
        command = command.strip()
        if cur_time != pre_time:  # time switch
            q = Queue()
            # print("-------------------")
            # print(printtingQ)
            while printtingQ.size != 0:
                qinq = Queue()
                stoptime = "None"
                msgInQ = "None"
                printNotDone = False
                deQ = printtingQ.deQueue
                while deQ.size != 0:
                    # print(deQ)
                    if stoptime != "None" and msgInQ != "None":
                        if stoptime <= cur_time:  # print done
                            if paper <= 0:
                                printNotDone = True
                                # print(f"[Time {cur_time}] Error: Printer is out of paper. Please refill.")
                            else:
                                # print(f"use 1 paper on {msgInQ}")
                                printed = True
                                paper -= 1
                                paperStack.push(msgInQ)
                        else:
                            printNotDone = True
                    deQQ = deQ.deQueue
                    qinq.enQueue(deQQ)
                    if deQ.size == 2:
                        stoptime = deQ.peek
                    elif deQ.size == 1:
                        msgInQ = deQ.peek
                    if cur_time < 10:
                        printed = False
                while qinq.size != 0:
                    deQ.enQueue(qinq.deQueue)
                if printNotDone:
                    q.enQueue(deQ)
            while q.size != 0:
                printtingQ.enQueue(q.deQueue)
            if cur_time - pre_time > 1 and paper <= 0 and printtingQ.size != 0:
                print(
                    f"[Time {cur_time-1}] Error: Printer is out of paper. Please refill."
                )
            if paper <= 0 and printtingQ.size != 0:
                print(
                    f"[Time {cur_time}] Error: Printer is out of paper. Please refill."
                )
            # print(printtingQ)
            # print("-----------------------")

        if command == "P":
            msg = value[2::].strip()
            # print(msg)
            x = 3
            y = 4
            if printed:
                x = 2
                y = 3

            if paper <= 0:
                print(
                    f"[Time {cur_time}] Error: Printer is out of paper. Please refill."
                )
            if printtingQ.isEmpty:
                # print("emptyQ")
                q = Queue()
                q.enQueue(cur_time)
                stoptime = cur_time + (len(msg) + 5 - 1) // 5
                q.enQueue(stoptime)
                q.enQueue(msg)
                printtingQ.enQueue(q)
                pre_time = cur_time

            elif printtingQ.size <= x:
                # print("Qing")
                q = Queue()
                latestQ = None
                while printtingQ.size != 0:
                    deQ = printtingQ.deQueue
                    # print(deQ)
                    q.enQueue(deQ)
                    if printtingQ.size == 0:
                        latestQ = deQ
                while q.size != 0:
                    printtingQ.enQueue(q.deQueue)
                if latestQ == None:
                    print("error")
                    return
                while latestQ.size != 0:
                    if latestQ.size == 2:
                        starttime = latestQ.peek
                    q.enQueue(latestQ.deQueue)
                while q.size != 0:
                    latestQ.enQueue(q.deQueue)
                stoptime = starttime + (len(msg) + 5 - 1) // 5
                q.enQueue(starttime)
                q.enQueue(stoptime)
                q.enQueue(msg)
                printtingQ.enQueue(q)
                pre_time = cur_time

            elif printtingQ.size >= y:
                print(
                    f"[Time {cur_time}] Error: Printer buffer is full. Please try again later."
                )
                pre_time = cur_time

        elif command == "S":
            if paper <= 0:
                print(
                    f"[Time {cur_time}] Status: Idle. Pending {printtingQ.size} file(s) in queue."
                )
                pre_time = cur_time
                continue
            if printtingQ.size == 0:
                print(
                    f"[Time {cur_time}] Status: Idle. Pending {printtingQ.size} file(s) in queue."
                )
            else:
                peekmsg = None
                stoptime = "None"
                peek = printtingQ.peek
                qu = Queue()
                while peek.size != 0:
                    if peek.size == 1:
                        peekmsg = peek.peek
                    elif peek.size == 2:
                        stoptime = peek.peek
                    qu.enQueue(peek.deQueue)
                while qu.size != 0:
                    peek.enQueue(qu.deQueue)
                print(
                    f'[Time {cur_time}] Status: Printing... "{peekmsg}" and Pending {printtingQ.size-1} file(s) in queue.'
                )
                if paper == 1 and stoptime - cur_time > 1:
                    print(
                        f"[Time {stoptime}] Error: Printer is out of paper. Please refill."
                    )
            pre_time = cur_time
        elif command == "R":
            time, num = value.split()
            num = int(num)
            paper += num
            pre_time = cur_time
        elif command == "T":
            if paperStack.size != 0:
                s = ""
                while paperStack.size != 0:
                    f = str(paperStack.pop)
                    s += '"'
                    s += f
                    s += '"'
                    if paperStack.size != 0:
                        s += ", "
                print(f"[Time {cur_time}] You got: {s}")
            else:
                print(f"[Time {cur_time}] You got: Nothing in tray.")
            pre_time = cur_time
        # print(command)
        # print(printtingQ)


inp = input("Enter input: ").split(",")
printting(inp)
