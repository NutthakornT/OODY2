import time
import numpy as np


class Route:
    def __init__(self, route_no, amount):
        self.route_no = route_no
        self.amount = int(amount)

    def __str__(self):
        return f"ช่องทาง {self.route_no} : แขก {self.amount} คน"


class Room:
    def __init__(self, room, value):
        self.room = room
        self.value = value

    def __str__(self):
        return "(ห้องที่ {0},หมายเลขลำดับ {1})".format(self.room + 1, self.value)


class Hash:
    def __init__(self, size):
        self.table = np.full(size, None, dtype=object)
        self.MaxCollision = 3
        self.Threshold = 100
        self.size = 0

    def insert(self, data):
        if self.Threshold < (self.size + 1) / len(self.table) * 100:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash(data)
            return

        probe = 0
        while True:
            index = self.hashing_function(data.room, probe)
            if self.table[index] is None:
                self.table[index] = data
                self.size += 1
                return True
            elif "force add" in data.value:
                print("มีห้องนี้อยู่แล้ว")
                return False
            else:
                probe += 1
                print(f"collision number {probe} at {index}")

            if probe == self.MaxCollision:
                print("****** Max collision - Rehash !!! ******")
                self.rehash(data)
                return

    def hashing_function(self, key, probe):
        return (int(key) + probe**2) % len(self.table)

    # key คือ หมายเลขห้อง
    def search(self, key):
        for i in range(len(self.table)):
            index = self.hashing_function(key, i)
            if self.table[index] is None:
                return None
            if self.table[index].room == int(key):
                return self.table[index]

    def delete(self, key):
        for i in range(len(self.table)):
            index = self.hashing_function(key, i)
            if self.table[index] is None:
                return None
            if self.table[index].room == int(key):
                self.table[index] = None
                self.size -= 1
                print(f"ลบหมายเลขห้อง {key+1} สำเร็จ")
                return True
        print("ไม่พบหมายเลขห้องในระบบ")

    def rehash(self, data):
        old_order = self.table
        new_table = np.full((len(self.table) * 2), None, dtype=object)
        self.table = new_table
        self.size = 0

        for item in old_order:
            if item:
                self.insert(item)
        self.insert(data)

    def __str__(self):
        result = ""
        for i, data in enumerate(self.table):
            if data is None:
                continue
            result += f"room#{data.room+1}\t{data.value}\n"
        return result


# ฟังก์ชันบันทึกลงไฟล์
def print_file(hash_table):
    output = "\n".join(
        [
            " ***** Hotel *****",
            "----------------------------------------",
            str(hash_table),
            "----------------------------------------",
        ]
    )

    with open("hashtable_output.txt", "w", encoding="utf-8") as f:
        f.write(output)
    print("\n✅ ผลลัพธ์ถูกบันทึกลงไฟล์ชื่อ hashtable_output.txt แล้ว")


import sys
import psutil
import os


def show_memory_usage():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    print(
        f"[Memory] RSS: {mem_info.rss / (1024 ** 2):.2f} MB | VMS: {mem_info.vms / (1024 ** 2):.2f} MB"
    )


# def show_memory_usage(hash_table, routes_data, route_list):
#     total = 0

#     # ขนาดตาราง Hash
#     total += sys.getsizeof(hash_table.table)
#     # ขนาดของแต่ละ Room ที่อยู่ใน Hash Table
#     for item in hash_table.table:
#         if item is not None:
#             total += sys.getsizeof(item)
#             total += sys.getsizeof(item.room)
#             total += sys.getsizeof(item.value)

#     # ขนาดข้อมูล Route
#     for r in routes_data:
#         total += sys.getsizeof(r)
#         total += sys.getsizeof(r.route_no)
#         total += sys.getsizeof(r.amount)

#     # ขนาดรายการช่องทาง
#     total += sys.getsizeof(route_list)
#     for x in route_list:
#         total += sys.getsizeof(x)

#     print(f"\n📦 หน่วยความจำที่ใช้ทั้งหมด ≈ {total:,} bytes ({total/1024:.2f} KB)")


# ---------------------- เริ่มโปรแกรม ----------------------

route_list = []
routes_data = []
force_add = 1

routes = input("ใส่หมายเลขช่องทาง (เช่น 1 2 3): ").split()
amounts = list(
    map(int, input(f"ใส่จำนวนแขกที่มาในช่องทาง {routes} ตามลำดับ (เช่น 10 5 8): ").split())
)
if len(routes) != len(amounts):
    print("⚠️ จำนวนช่องทางและจำนวนแขกไม่ตรงกัน")
start = time.perf_counter()
all_new_guest_amount = sum(amounts)
room_no = 0
Hotel = Hash(all_new_guest_amount)
for i in range(len(routes)):
    routes_data.append(Route(routes[i], amounts[i]))
    route_list.append(routes[i])
    for j in range(amounts[i]):
        Hotel.insert(Room(room_no, f"R{routes[i]}_P{j+1}"))
        room_no += 1
end = time.perf_counter()
print(f"runtime : {(end-start):.20f}")
print("\n✅ เพิ่มข้อมูลช่องทางที่แล้ว:")


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
        print("⚠️ กรุณาใส่เลข 0-6 เท่านั้น")
        continue

    choice = int(choice)

    if choice == 0:
        print("ออกจากโปรแกรมแล้ว")
        break

    elif choice == 1:
        routes = input("ใส่หมายเลขช่องทาง (เช่น 1 2 3): ").split()
        amounts = list(
            map(
                int,
                input(f"ใส่จำนวนแขกที่มาในช่องทาง {routes} ตามลำดับ (เช่น 10 5 8): ").split(),
            )
        )
        if len(routes) != len(amounts):
            print("⚠️ จำนวนช่องทางและจำนวนแขกไม่ตรงกัน")
            continue
        start = time.perf_counter()

        all_new_guest_amount = sum(amounts)
        old_amount = sum(r.amount for r in routes_data)
        room_no = 0
        temp = Hotel.table
        Hotel.table = np.full(
            len(temp) + all_new_guest_amount + old_amount + 10, None, dtype=object
        )
        # ย้ายห้องคนเก่าออกไป all_new_guest_amount
        for i, data in enumerate(reversed(temp)):
            if data:
                Hotel.table[data.room + all_new_guest_amount] = temp[data.room]
                data.room += all_new_guest_amount
        temp = None
        # เก็บประวัติหมายเลขที่มา+จำนวน
        # ทำการเช็คว่ามีเคยมายัง
        for i in range(len(routes)):
            # เคยมาแล้ว
            if routes[i] in route_list:
                # for loop เพื่อหา routes_data ที่เลขตรงกัน
                for j in routes_data:
                    if j.route_no == routes[i]:
                        for k in range(j.amount, j.amount + amounts[i]):
                            Hotel.insert(Room(room_no, f"R{routes[i]}_P{k+1}"))
                            room_no += 1
                        j.amount += amounts[i]
                        break

                # ยังไม่เคยมา
            else:
                routes_data.append(Route(routes[i], amounts[i]))
                route_list.append(routes[i])
                for j in range(amounts[i]):
                    Hotel.insert(Room(room_no, f"R{routes[i]}_P{j+1}"))
                    room_no += 1

        end = time.perf_counter()
        print(f"runtime : {(end-start):.20f}")
        print("\n✅ เพิ่มข้อมูลช่องทางที่แล้ว:")

    elif choice == 2:
        key = int(input("ใส่หมายเลขห้องที่ต้องการเพิ่ม: "))
        start = time.perf_counter()
        if Hotel.insert(Room(key - 1, f"force add room no : {force_add}")):
            print(f"เพิ่มห้อง {key} สำเร็จแล้ว")
            force_add += 1
        end = time.perf_counter()
        print(f"runtime : {(end-start):.20f}")

    elif choice == 3:
        key = int(input("ใส่หมายเลขห้องที่ต้องการลบ: "))
        start = time.perf_counter()
        Hotel.delete(key - 1)
        end = time.perf_counter()
        print(f"runtime : {(end-start):.20f}")

    elif choice == 4:
        print("\n=== จัดเรียงหมายเลขห้องที่มีในตาราง ===")
        print(Hotel)

    elif choice == 5:
        key = int(input("ใส่หมายเลขห้องที่ต้องการค้นหา: "))
        start = time.perf_counter()
        result = Hotel.search(key - 1)
        end = time.perf_counter()
        if result:
            print(f"✅ พบห้องหมายเลข {key} ในระบบ")
            print(result)
        else:
            print(f"❌ ไม่พบห้องหมายเลข {key}")
        print(f"runtime : {(end-start):.20f}")

    elif choice == 6:
        start = time.perf_counter()
        print_file(Hotel)
        end = time.perf_counter()
        print(f"runtime : {(end-start):.20f}")

    elif choice == 7:
        show_memory_usage()
