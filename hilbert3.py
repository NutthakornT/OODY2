import time
import numpy as np
from pympler import asizeof
import psutil
import os


# ==============================================
# 1️⃣ CLASS DEFINITIONS
# ==============================================
class Route:
    def __init__(self, route_no, amount):
        self.route_no = route_no
        self.amount = int(amount)

    def __str__(self):
        return f"ช่องทาง {self.route_no} : แขก {self.amount} คน"


class Room:
    def __init__(self, room, value, is_manual=False):
        self.room = int(room)
        self.value = value
        self.is_manual = bool(is_manual)  # ถ้าเพิ่มด้วย choice==2 ให้ True

    def __str__(self):
        return f"(ห้องที่ {self.room+1}, หมายเลขลำดับ {self.value}{' [manual]' if self.is_manual else ''})"


class Hash:
    def __init__(self, size):
        self.table = np.full(size, None, dtype=object)
        self.size = 0
        self.MaxCollision = 10
        self.Threshold = 70

    def hashing_function(self, key, probe):
        return (int(key) + probe**2) % len(self.table)

    def insert(self, data):
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
                return False
        self.rehash()
        return self.insert(data)

    def rehash(self):
        old_items = [x for x in self.table if x is not None]
        new_len = max(len(self.table) * 2, 2)
        self.table = np.full(new_len, None, dtype=object)
        self.size = 0
        for item in old_items:
            self.insert(item)

    def search(self, key):
        for i in range(self.MaxCollision):
            index = self.hashing_function(key, i)
            item = self.table[index]
            if item and item.room == key:
                return item
        return None

    def delete(self, key):
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
        lines = [f"room#{d.room+1}\t{d.value}" for d in self.table if d is not None]
        return "\n".join(lines)


# ------------------ ฟังก์ชันช่วยแปลง room -> (r,p) ------------------
def extract_r_p_from_room(n):
    """
    รับ n = guest.room (จำนวนเต็ม >= 0)
    คืนค่า (r, p) ตามนิยามที่ n = (2**r)*(2*p-1) - 1
    """
    val = n + 1
    r = 0
    # หา v2(val)
    while val % 2 == 0:
        val //= 2
        r += 1
    odd = val  # = 2*p - 1
    p = (odd + 1) // 2
    return r, p


# ------------------ ฟังก์ชันช่วย หาห้องว่างแบบ Hilbert (พยายามเพิ่ม p ก่อน) -------------
def find_free_hilbert_room_for(route_r, start_p, Hotel, max_tries=100000):
    """
    หา p >= start_p ที่ทำให้ hilbert_room_index(route_r, p) ว่างใน Hotel
    ถ้าไม่พบภายใน max_tries จะเพิ่ม route_r (fallback)
    คืน (room_no, p, r_used)
    """
    p = start_p
    tries = 0
    while tries < max_tries:
        candidate = hilbert_room_index(route_r, p)
        if Hotel.search(candidate) is None:
            return candidate, p, route_r
        p += 1
        tries += 1
    # ถ้าไม่พบ ให้ขยับ r ขึ้น 1 แล้วลองอีกครั้ง (fallback)
    route_r += 1
    p = start_p
    tries = 0
    while tries < max_tries:
        candidate = hilbert_room_index(route_r, p)
        if Hotel.search(candidate) is None:
            return candidate, p, route_r
        p += 1
        tries += 1
    raise RuntimeError(
        "Cannot find free hilbert room (increase max_tries or table size)"
    )


# ==============================================
# 2️⃣ HILBERT FUNCTION
# ==============================================
def hilbert_room_index(route_no, person_no):
    """สูตรคณิตศาสตร์ Hilbert Infinite Hotel"""
    return (2**route_no) * (2 * person_no - 1) - 1


# ==============================================
# 3️⃣ PRINT FUNCTION
# ==============================================
def print_file(hash_table):
    with open("hilbert_hotel.txt", "w", encoding="utf-8") as f:
        f.write(" ***** Hilbert's Infinite Hotel *****\n")
        f.write("----------------------------------------\n")
        f.write(f"{hash_table}\n")
        f.write("----------------------------------------\n")
        f.write(f"Total Guests: {hash_table.size}\n")
    print("\n✅ ผลลัพธ์ถูกบันทึกลงไฟล์ชื่อ hilbert_hotel.txt แล้ว")


def show_memory_usage():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    print(
        f"[Memory] RSS: {mem_info.rss / (1024 ** 2):.2f} MB | VMS: {mem_info.vms / (1024 ** 2):.2f} MB"
    )


def quick_sort2(room_list):
    """เรียงลำดับหมายเลขห้องด้วย Quick Sort (DSA)"""
    if len(room_list) <= 1:
        return room_list
    else:
        pivot = room_list[len(room_list) // 2].room
        left = [x for x in room_list if x.room < pivot]
        middle = [x for x in room_list if x.room == pivot]
        right = [x for x in room_list if x.room > pivot]
        return quick_sort(left) + middle + quick_sort(right)


def quick_sort(room_list):
    """เรียงลำดับหมายเลขห้องด้วย Quick Sort (DSA) แบบไม่ใช้ recursion"""
    if len(room_list) <= 1:
        return room_list

    stack = [(0, len(room_list) - 1)]  # เก็บช่วงของ index ที่ต้องจัดการ

    while stack:
        low, high = stack.pop()
        if low >= high:
            continue

        # เลือก pivot เป็นค่ากลาง
        pivot = room_list[(low + high) // 2].room
        i, j = low, high

        while i <= j:
            while room_list[i].room < pivot:
                i += 1
            while room_list[j].room > pivot:
                j -= 1
            if i <= j:
                room_list[i], room_list[j] = room_list[j], room_list[i]
                i += 1
                j -= 1

        # push ขอบเขตซ้ายและขวาที่เหลือลง stack
        if low < j:
            stack.append((low, j))
        if i < high:
            stack.append((i, high))

    return room_list


# ==============================================
# 4️⃣ START PROGRAM
# ==============================================
route_list = []
manual_rooms = []
force_add = 1

routes = input("ใส่หมายเลขช่องทางเริ่มต้น (เช่น 0 1 2): ").split()
amounts = list(map(int, input(f"ใส่จำนวนแขกในช่องทาง {routes}: ").split()))

if len(routes) != len(amounts):
    print("⚠️ จำนวนช่องทางและจำนวนแขกไม่ตรงกัน")
    exit()

# ใช้ route_list เก็บจำนวนช่องทางทั้งหมดที่เคยสร้าง
for i in range(len(routes)):
    route_list.append(i)

max_possible_room = (2 ** (max(map(int, routes)) + 2)) * 3
Hotel = Hash(max_possible_room)

start = time.perf_counter()
for i, route in enumerate(routes):
    real_route_no = route_list[i]
    for j in range(1, amounts[i] + 1):
        room_no = hilbert_room_index(real_route_no, j)
        Hotel.insert(Room(room_no, f"R{real_route_no}_P{j}"))
end = time.perf_counter()

print(f"\n✅ จัดแขกเข้าห้องสำเร็จด้วยสูตร Infinite Hotel Paradox")
print(f"runtime : {(end-start):.10f}")


# ==============================================
# 5️⃣ MENU SYSTEM
# ==============================================
while True:
    print("\nพิมพ์เลขต่อไปนี้เพื่อใช้ฟังก์ชันนั้น")
    print("1. เพิ่มช่องทางและจำนวนแขกใหม่ (Hilbert mapping)")
    print("2. เพิ่มหมายเลขห้องแบบ manual")
    print("3. ลบหมายเลขห้องแบบ manual")
    print("4. แสดงหมายเลขห้องทั้งหมดที่เรียงแล้ว")
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
        routes = input("ใส่หมายเลขช่องทางใหม่ (เช่น 3 4 5): ").split()
        amounts = list(map(int, input(f"ใส่จำนวนแขกในช่องทาง {routes}: ").split()))

        if len(routes) != len(amounts) or any(a <= 0 for a in amounts):
            print("⚠️ ข้อมูลไม่ถูกต้อง")
            continue

        start = time.perf_counter()

        # เพิ่ม route_list ใหม่ (ต่อจากเดิม)
        start_route_index = len(route_list)
        for idx, route in enumerate(routes):
            route_no = start_route_index + idx
            route_list.append(route_no)

        # รวบรวมแขกเดิมทั้งหมด (จาก Hotel.table) และ manual_rooms
        old_guests = [x for x in Hotel.table if x is not None]
        # เพิ่มแขกใหม่ (จาก input) เข้า list old_guests เพื่อจะย้ายทั้งหมดพร้อมกัน
        for idx, route in enumerate(routes):
            route_no = start_route_index + idx
            for j in range(1, amounts[idx] + 1):
                # เพิ่มเป็น guest ชั่วคราว (ยังไม่ insert) -- treat as not manual
                old_guests.append(
                    Room(
                        hilbert_room_index(route_no, j),
                        f"R{route_no}_P{j}",
                        is_manual=False,
                    )
                )

        # สร้าง Hotel ใหม่ ขนาดคำนวณจาก route_list ปัจจุบัน
        max_possible_room = (2 ** (max(route_list) + 2)) * 3
        new_Hotel = Hash(max_possible_room)

        # ใส่ manual rooms ก่อน (ล็อกพื้นที่)
        for m in manual_rooms:
            if new_Hotel.search(m.room) is None:
                new_Hotel.insert(m)

        # ย้ายแขกทั้งหมดที่ไม่ใช่ manual
        for guest in old_guests:
            # ข้ามถ้าเป็น manual (เราไม่ต้องการย้าย manual)
            if getattr(guest, "is_manual", False):
                continue

            # แยก r,p จาก guest.room (รองรับทั้งแขกที่มาจาก Hilbert เดิม หรือ manual ที่ติดมาผิดพลาด)
            try:
                r, p = extract_r_p_from_room(guest.room)
            except Exception as e:
                # ถ้า decode ไม่ได้ (ค่ากรณีพิเศษ) ให้ fallback: treat as p=1,r=0
                r, p = 0, 1

            # ปรับ policy: ตัวอย่างนี้เพิ่ม r ทีละ 1 (ย้ายขึ้นชั้น)
            new_r = r + 1

            # หา room ว่างโดยพยายามเพิ่ม p ก่อน ถ้ายังชน จะขยับ r เป็น fallback
            candidate_room, candidate_p, used_r = find_free_hilbert_room_for(
                new_r, p, new_Hotel
            )

            # อัปเดต guest แล้ว insert
            guest.room = candidate_room
            guest.value = f"R{used_r}_P{candidate_p}"
            new_Hotel.insert(guest)

        # เปลี่ยน Hotel ไปใช้ตัวใหม่
        Hotel = new_Hotel

        end = time.perf_counter()
        print(f"✅ เพิ่มช่องทางใหม่และย้ายแขกเก่าเรียบร้อย runtime : {(end-start):.10f}")

    elif choice == 2:
        try:
            key = int(input("ใส่หมายเลขห้องที่ต้องการเพิ่ม (ตัวเลข): "))
        except ValueError:
            print("Invalid Input")
            continue

        if key <= 0:
            print("Invalid Input")
            continue

        # เปลี่ยนเป็น zero-based index
        desired_index = key - 1

        if Hotel.search(desired_index):
            print(f"⚠️ ห้อง {key} มีอยู่แล้ว — เพิ่มไม่สำเร็จ (avoid duplicate).")
            continue

        new_room = Room(
            desired_index, f"force add room no : {force_add}", is_manual=True
        )
        Hotel.insert(new_room)
        manual_rooms.append(new_room)
        force_add += 1
        print(f"✅ เพิ่มห้อง {key} (manual) สำเร็จแล้ว")

    elif choice == 3:
        key = int(input("ใส่หมายเลขห้องที่ต้องการลบ: "))
        start = time.perf_counter()
        Hotel.delete(key - 1)
        end = time.perf_counter()
        print(f"runtime : {(end-start):.10f}")

    elif choice == 4:
        print("\n=== รายชื่อห้องทั้งหมด (เรียงลำดับแล้ว - Quick Sort) ===")

        # 🔹 ดึงข้อมูลห้องทั้งหมดจาก Hash Table
        rooms = [x for x in Hotel.table if x is not None]

        if not rooms:
            print("⚠️ ยังไม่มีข้อมูลห้องในระบบ")
            continue

        # 🔹 เรียงลำดับด้วย Quick Sort
        start = time.perf_counter()
        sorted_rooms = quick_sort(rooms)
        end = time.perf_counter()

        # 🔹 แสดงผลเรียงแล้ว
        # for r in sorted_rooms:
        #     print(f"room#{r.room+1}\t{r.value}")

        # 🔹 สร้างไฟล์ผลลัพธ์
        with open("sorted_rooms.txt", "w", encoding="utf-8") as f:
            f.write("=== รายชื่อห้องทั้งหมด (เรียงลำดับแล้ว - Quick Sort) ===\n")
            for r in sorted_rooms:
                f.write(f"room#{r.room+1}\t{r.value}\n")
            f.write(f"\nรวมทั้งหมด {len(sorted_rooms)} ห้อง\n")
            f.write(f"runtime: {(end - start):.10f} วินาที\n")

        print("\n✅ บันทึกผลเรียงลำดับลงไฟล์ sorted_rooms.txt เรียบร้อยแล้ว")
        print(f"runtime : {(end-start):.10f} วินาที")

    elif choice == 5:
        key = int(input("ใส่หมายเลขห้องที่ต้องการค้นหา: "))
        start = time.perf_counter()
        result = Hotel.search(key - 1)
        end = time.perf_counter()
        if result:
            print(f"✅ พบห้องหมายเลข {key} -> {result}")
        else:
            print(f"❌ ไม่พบห้องหมายเลข {key}")
        print(f"runtime : {(end-start):.10f}")

    elif choice == 6:
        start = time.perf_counter()
        print_file(Hotel)
        end = time.perf_counter()
        print(f"runtime : {(end-start):.10f}")

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
