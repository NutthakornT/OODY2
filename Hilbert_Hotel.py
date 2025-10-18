import time
import numpy as np
from pympler import asizeof
import psutil
import os


class Route:
    def __init__(self, route_no, amount):
        self.route_no = route_no
        self.amount = int(amount)

    def __str__(self):
        return f"ช่องทาง {self.route_no} : แขก {self.amount} คน"


class Room:
    def __init__(self, room, value):
        self.room = int(room)
        self.value = value

    def __str__(self):
        return f"(ห้องที่ {self.room+1}, หมายเลขลำดับ {self.value})"


class Hash:
    def __init__(self, size, table=None):
        if table is not None:
            self.table = table
            self.size = len([x for x in table if x is not None])
        else:
            self.table = np.full(size, None, dtype=object)
            self.size = 0
        self.MaxCollision = 10
        self.Threshold = 70

    def hashing_function(self, key, probe):
        return (int(key) + probe**2) % len(self.table)

    def insert(self, data):
        """Insert safely with rehash if full"""
        if (self.size + 1) / len(self.table) * 100 > self.Threshold:
            self.rehash()

        key = int(data.room)
        for probe in range(self.MaxCollision):
            index = self.hashing_function(key, probe)
            if self.table[index] is None:
                self.table[index] = data
                self.size += 1
                return True
            elif self.table[index].room == key:
                # ทับห้องเดิมไม่ได้
                return False

        # ถ้าชนเกิน max
        self.rehash()
        return self.insert(data)

    def rehash(self):
        """ขยายตารางเป็น 2 เท่า"""
        old_items = [x for x in self.table if x is not None]
        new_len = max(len(self.table) * 2, 2)
        self.table = np.full(new_len, None, dtype=object)
        self.size = 0
        for item in sorted(old_items, key=lambda x: x.room):
            self.insert(item)

    def search(self, key):
        """ค้นหา key"""
        for i in range(self.MaxCollision):
            index = self.hashing_function(key, i)
            item = self.table[index]
            if item and item.room == key:
                return item
        return None

    def delete(self, key):
        """ลบแบบไม่พัง chain"""
        for i in range(self.MaxCollision):
            index = self.hashing_function(key, i)
            item = self.table[index]
            if item and item.room == key:
                self.table[index] = None
                self.size -= 1
                print(f"ลบหมายเลขห้อง {key+1} สำเร็จ")
                return True
        print("ไม่พบหมายเลขห้องในระบบ")
        return False

    def __str__(self):
        lines = []
        for data in sorted(
            [x for x in self.table if x is not None], key=lambda x: x.room
        ):
            lines.append(f"room#{data.room+1}\t{data.value}")
        return "\n".join(lines)


def print_file(hash_table):
    with open("hashtable_output.txt", "w", encoding="utf-8") as f:
        f.write(" ***** Hotel *****\n")
        f.write("----------------------------------------\n")
        for data in sorted(
            (x for x in hash_table.table if x is not None), key=lambda x: x.room
        ):
            f.write(f"room#{data.room+1}\t{data.value}\n")
        f.write("----------------------------------------\n")
        f.write(f"Total Rooms: {hash_table.size}\n")

    print("\n✅ ผลลัพธ์ถูกบันทึกลงไฟล์ชื่อ hashtable_output.txt แล้ว")


def show_memory_usage():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    print(
        f"[Memory] RSS: {mem_info.rss / (1024 ** 2):.2f} MB | VMS: {mem_info.vms / (1024 ** 2):.2f} MB"
    )


# ---------------------- เริ่มโปรแกรม ----------------------

route_list = []
manual_rooms = []
force_add = 1
flag = True

routes = input("ใส่หมายเลขช่องทาง (เช่น 1 2 3): ").split()
amounts = list(
    map(int, input(f"ใส่จำนวนแขกที่มาในช่องทาง {routes} ตามลำดับ (เช่น 10 5 8): ").split())
)

if len(routes) != len(amounts):
    print("⚠️ จำนวนช่องทางและจำนวนแขกไม่ตรงกัน")
    flag = False

for i in amounts:
    if i <= 0:
        print("Invalid input")
        flag = False
        break

if flag:
    start = time.perf_counter()
    all_new_guest_amount = sum(amounts)
    room_no = 0
    Hotel = Hash(all_new_guest_amount)
    for i in range(len(routes)):
        route_list.append(i)
        for j in range(amounts[i]):
            Hotel.insert(Room(room_no, f"R{i}_P{j+1}"))
            room_no += 1
    end = time.perf_counter()
    print(f"runtime : {(end-start):.20f}")
else:
    Hotel = Hash(0)

# ---------------------- เมนูหลัก ----------------------
while True:
    print("\nพิมพ์เลขต่อไปนี้เพื่อใช้ฟังก์ชันนั้น")
    print("1. เพิ่มช่องทางที่แขกเดินทางมาและจำนวนแขกในแต่ละช่องทาง")
    print("2. เพิ่มหมายเลขห้องแบบ manual")
    print("3. ลบหมายเลขห้องแบบ manual")
    print("4. จัดเรียงลำดับหมายเลขห้อง")
    print("5. ค้นหาหมายเลขห้อง")
    print("6. สร้างไฟล์แสดงผลลัพธ์")
    print("7. แสดงจำนวนหน่วยความจำที่ใช้")
    print("0. ออกจากโปรแกรม")
    choice = input("กรุณาใส่หมายเลขข้างต้น 0-7 : ")

    if not choice.isdigit() or not (0 <= int(choice) <= 7):
        print("⚠️ กรุณาใส่เลข 0-7 เท่านั้น")
        continue

    choice = int(choice)

    if choice == 0:
        print("ออกจากโปรแกรมแล้ว")
        break

    elif choice == 1:
        routes = input("ใส่หมายเลขช่องทางใหม่ (เช่น 4 5): ").split()
        amounts = list(map(int, input(f"ใส่จำนวนแขกในช่องทาง {routes}: ").split()))

        if len(routes) != len(amounts) or any(a <= 0 for a in amounts):
            print("⚠️ ข้อมูลไม่ถูกต้อง")
            continue

        start = time.perf_counter()

        # เก็บห้องเดิมทั้งหมด
        all_items = sorted(
            [x for x in Hotel.table if x is not None], key=lambda x: x.room
        )
        new_rooms = []

        # สร้างห้องใหม่สำหรับแต่ละ route
        print(len(route_list))
        for i in range(len(route_list) + 1, len(routes) + len(route_list) + 1):
            amount = amounts[i - len(route_list)]

            for j in range(amount):
                new_rooms.append(Room(j, f"R{i}_P{j + 1}"))

            route_list.append(i)

        # รวมข้อมูลใหม่ไว้หน้าสุด แล้วลดขนาด Hash Table ให้พอดี
        combined = new_rooms + all_items
        new_size = len(combined) * 2
        Hotel.table = np.full(new_size, None, dtype=object)
        Hotel.size = 0

        for i, room in enumerate(combined):
            room.room = i
            Hotel.insert(room)

        end = time.perf_counter()
        print(f"✅ เพิ่มช่องทางใหม่เรียบร้อย runtime : {(end-start):.20f}")

    elif choice == 2:
        try:
            key = int(input("ใส่หมายเลขห้องที่ต้องการเพิ่ม: "))
        except ValueError:
            print("Invalid Input")
            continue

        if key <= 0:
            print("Invalid Input")
            continue

        start = time.perf_counter()

        # ตรวจว่าห้องมีอยู่แล้วหรือไม่
        if Hotel.search(key - 1):
            print(f"⚠️ ห้อง {key} มีอยู่แล้ว")
            # all_items = sorted([x for x in Hotel.table if x is not None], key=lambda x: x.room)
            # for item in reversed(all_items):
            #     if item.room >= key - 1:
            #         item.room += 1
            # Hotel.rehash()
            continue

        # เพิ่มห้องใหม่
        new_room = Room(key - 1, f"force add room no : {force_add}")
        Hotel.insert(new_room)
        if not any(m.room == new_room.room for m in manual_rooms):
            manual_rooms.append(new_room)
        force_add += 1

        end = time.perf_counter()
        print(f"✅ เพิ่มห้อง {key} สำเร็จแล้ว")
        print(f"runtime : {(end-start):.10f}")

    elif choice == 3:
        key = int(input("ใส่หมายเลขห้องที่ต้องการลบ: "))
        start = time.perf_counter()
        Hotel.delete(key - 1)
        end = time.perf_counter()
        print(f"runtime : {(end-start):.20f}")

    elif choice == 4:
        print("\n=== จัดเรียงหมายเลขห้อง ===")
        print(Hotel)

    elif choice == 5:
        key = int(input("ใส่หมายเลขห้องที่ต้องการค้นหา: "))
        start = time.perf_counter()
        result = Hotel.search(key - 1)
        end = time.perf_counter()
        if result:
            print(f"✅ พบห้องหมายเลข {key} ในระบบ -> {result}")
        else:
            print(f"❌ ไม่พบห้องหมายเลข {key}")
        print(f"runtime : {(end-start):.20f}")

    elif choice == 6:
        start = time.perf_counter()
        print_file(Hotel)
        end = time.perf_counter()
        print(f"runtime : {(end-start):.20f}")

    elif choice == 7:
        datasize_bytes = asizeof.asizeof(Hotel)
        process = psutil.Process(os.getpid())
        mem_info = process.memory_info()

        def human_readable(num_bytes):
            for unit in ("Bytes", "KB", "MB", "GB", "TB"):
                if num_bytes < 1024.0 or unit == "TB":
                    return f"{num_bytes:,.2f} {unit}"
                num_bytes /= 1024.0

        print("\n📦 ขนาดข้อมูล Hotel:")
        print(f"  - raw bytes : {datasize_bytes:,} Bytes")
        print(f"  - readable  : {human_readable(datasize_bytes)}")
        print("\n🧠 หน่วยความจำ:")
        print(f"  - RSS : {human_readable(mem_info.rss)}")
        print(f"  - VMS : {human_readable(mem_info.vms)}")
