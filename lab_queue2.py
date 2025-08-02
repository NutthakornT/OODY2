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

    def peek(self):
        if not self.item:
            return None
        return self.item[0]  # ใช้ดูตัวแรกของ Queue
        pass


def check_color(group, next_color):
    temp_group = group + [next_color]
    # จำลอง group ขึ้นมาก่อน [pink,green(ลองเอามา)] = hell no
    if "Pink" in temp_group and "Green" in temp_group and "Blue" not in temp_group:
        return False

    if "Blue" in temp_group and "Yellow" in temp_group and "Red" not in temp_group:
        return False

    return True


print("***Make a group***")
inp = input("Enter input : ")
group_size, name_str = inp.split(", ", 1)
names = name_str.strip().split()
group_size = int(group_size)
q = Queue()
for name in names:
    q.enqueue(name)
# print(f"group_size = {group_size}")
# print(f"name_str = {name_str}")
# print(f"name = {names}")
# print(q.item)
rejected = []
group_num = 1
while not q.isEmpty():

    group = []
    while len(group) < group_size and not q.isEmpty():
        next_person = q.peek()
        if len(group) == 0:
            if q.isEmpty():
                break
            group.append(q.dequeue())

        else:

            if check_color(group, next_person):  # check if next เข้ากับที่มีอยู่
                group.append(q.dequeue())
            else:
                if not q.isEmpty():
                    rejected.append(q.dequeue())

        pass
    if len(group) < group_size:
        rejected.extend(group)
        break

    print(f"Group {group_num} : ", end="")  # print label without newline
    print(*group, sep=", ")
    group_num += 1

    pass


if rejected:
    # print(f"Rejected : {", ".join(rejected)}")
    print(f"Rejected : ", end="")
    print(*rejected, sep=", ")
else:
    print("Rejected : None")
