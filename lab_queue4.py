# Define a Queue class with basic operations
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
        return self.item.pop(0)  # remove from front

    @property
    def peek(self):
        return self.item[0]  # view front without removing

    @property
    def size(self):
        return len(self.item)

    @property
    def isEmpty(self):
        return len(self.item) == 0

    def __str__(self):
        s = ""
        for i in self.item:
            s += str(i) + " "
        return s


# Define a Stack class with basic operations
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


# Main printer simulator function
def printing(message):
    paper = 3  
    paperStack = Stack()  # tray 
    printtingQ = Queue()  # main queue 
    pre_time = 0  # track last processed time
    printed = False  # whether a print job was just completed

    for item in message:
        command, value = item.split(":")
        
        # Extract current time from value (handle 1-digit or 2-digit time)
        if value[0:2].isdigit():
            cur_time = int(value[0:2])
        else:
            cur_time = int(value[0])
        
        command = command.strip()  

        # if time change = start
        if cur_time != pre_time:
            q = Queue()

            # loop check completion
            while printtingQ.size != 0:
                qinq = Queue()
                stoptime = "None"
                msgInQ = "None"
                printNotDone = False

                deQ = printtingQ.deQueue  # take out a print job (which is itself a queue)

                while deQ.size != 0:
                    # If previous fields exist, and job is due
                    if stoptime != "None" and msgInQ != "None":
                        if stoptime <= cur_time:
                            if paper <= 0:
                                printNotDone = True # still not complete
                            else: # if complete
                                printed = True
                                paper -= 1
                                paperStack.push(msgInQ)  # send to tray
                        else:
                            printNotDone = True

                    deQQ = deQ.deQueue  # process inner job queue
                    qinq.enQueue(deQQ)

                    if deQ.size == 2:
                        stoptime = deQ.peek
                    elif deQ.size == 1:
                        msgInQ = deQ.peek
                    
                    if cur_time < 10:
                        printed = False

                while qinq.size != 0:
                    deQ.enQueue(qinq.deQueue)  # restore job to original

                if printNotDone:
                    q.enQueue(deQ)

            while q.size != 0:
                printtingQ.enQueue(q.deQueue)

            # if time change and out of paper
            if cur_time - pre_time > 1 and paper <= 0 and printtingQ.size != 0:
                print(f"[Time {cur_time-1}] Error: Printer is out of paper. Please refill.")
            if paper <= 0 and printtingQ.size != 0:
                print(f"[Time {cur_time}] Error: Printer is out of paper. Please refill.")

        ########################################################################################

        if command == "P":  # Print
            msg = value[2::].strip() #there ,hi
            x = 3
            y = 4
            if printed:
                x = 2
                y = 3

            if paper <= 0:
                print(f"[Time {cur_time}] Error: Printer is out of paper. Please refill.")

            if printtingQ.isEmpty:
                # Add first print job
                q = Queue()
                q.enQueue(cur_time)
                #find when it will be done
                stoptime = cur_time + (len(msg) + 4) // 5  # 5 chars/second
                q.enQueue(stoptime)
                q.enQueue(msg)
                printtingQ.enQueue(q)
                pre_time = cur_time

            elif printtingQ.size <= x:
                # Add job at the end
                q = Queue()
                latestQ = None
                while printtingQ.size != 0:
                    deQ = printtingQ.deQueue
                    q.enQueue(deQ)
                    if printtingQ.size == 0:
                        latestQ = deQ
                while q.size != 0:
                    printtingQ.enQueue(q.deQueue)

                if latestQ == None:
                    print("error")
                    return

                # Extract start time
                while latestQ.size != 0:
                    if latestQ.size == 2: #the next one is the start time if == 2
                        starttime = latestQ.peek # save start time
                    q.enQueue(latestQ.deQueue)
                while q.size != 0:
                    latestQ.enQueue(q.deQueue)
                #find when it will be done
                stoptime = starttime + (len(msg) + 4) // 5
                q = Queue()
                q.enQueue(starttime) # when it startprint
                q.enQueue(stoptime) # when it finish
                q.enQueue(msg) # full message 
                #add to main print queue
                printtingQ.enQueue(q)
                pre_time = cur_time

            elif printtingQ.size >= y:
                # Too many jobs
                print(f"[Time {cur_time}] Error: Printer buffer is full. Please try again later.")
                pre_time = cur_time
        ###################################################################################
        elif command == "S":  # Status
            if paper <= 0:
                print(f"[Time {cur_time}] Status: Idle. Pending {printtingQ.size} file(s) in queue.")
                pre_time = cur_time
                continue

            if printtingQ.size == 0: # no queue
                print(f"[Time {cur_time}] Status: Idle. Pending 0 file(s) in queue.")
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
                print(f'[Time {cur_time}] Status: Printing... "{peekmsg}" and Pending {printtingQ.size-1} file(s) in queue.')
                # print
                if paper == 1 and stoptime - cur_time > 1:
                    print(f"[Time {stoptime}] Error: Printer is out of paper. Please refill.")
            pre_time = cur_time
        #####################################################################################
        elif command == "R":  # Refill
            time, num = value.split()
            num = int(num)
            paper += num
            pre_time = cur_time
        #####################################################################################
        elif command == "T":  # Tray
            if paperStack.size != 0:
                s = ""
                while paperStack.size != 0:
                    f = str(paperStack.pop)
                    s += '"' + f + '"'
                    if paperStack.size != 0:
                        s += ", "
                print(f"[Time {cur_time}] You got: {s}")
            else:
                print(f"[Time {cur_time}] You got: Nothing in tray.")
            pre_time = cur_time

# Run the simulation
inp = input("Enter input: ").split(",")
printing(inp)
