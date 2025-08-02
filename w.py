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


def is_valid_group(group):
    # เงื่อนไข 1: Green + Pink ห้ามอยู่ด้วยกัน ถ้าไม่มี Blue
    if "Green" in group and "Pink" in group and "Blue" not in group:
        return False
    # เงื่อนไข 2: Blue + Yellow ห้ามอยู่ด้วยกัน ถ้าไม่มี Red
    if "Blue" in group and "Yellow" in group and "Red" not in group:
        return False
    return True


def make_groups(group_size, names):
    q = Queue(names)
    group_count = 0
    rejected = []

    while q.size() >= group_size:
        # ดึงคนมาตามจำนวนกลุ่ม
        current_group = []
        for _ in range(group_size):
            current_group.append(q.dequeue())

        # ตรวจสอบว่าผ่านเงื่อนไขไหม
        if is_valid_group(current_group):
            group_count += 1
            print(f"Group {group_count} : {', '.join(current_group)}")
        else:
            rejected.extend(current_group)

    # เหลือคนไม่ครบกลุ่ม → reject ด้วย
    while not q.isEmpty():
        rejected.append(q.dequeue())

    if rejected:
        print("Rejected : " + ", ".join(rejected))


# ================================
# ทดสอบตามตัวอย่าง
raw_input = "4, Green Pink Blue Red Yellow Green Pink Yellow Blue Red Green Pink"
size_str, names_str = raw_input.split(",", 1)
group_size = int(size_str.strip())
names = names_str.strip().split()

make_groups(group_size, names)
