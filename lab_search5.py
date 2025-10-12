# ฟังก์ชัน ถ้าให้กล่องแต่ละใบรับน้ำหนักได้ไม่เกิน max_weight

def can_divide(weights, k, max_weight):
    count = 1           
    current = 0         
    for w in weights:   
        # ถ้าใส่ของชิ้นนี้แล้วเกินน้ำหนักที่กำหนดไว้
        if current + w > max_weight:
            count += 1      # เปิดกล่องใหม่
            current = w     # ของชิ้นนี้ใส่ในกล่องใหม่
            if count > k:   # ถ้าเกินจำนวนกล่องที่มีอยู่
                return False
        else:
            # ยังไม่เกินน้ำหนักสูงสุด → ใส่ต่อไปได้
            current += w
    return True             #ถ้าใส่ได้ครบทุกชิ้น


# (min possible max weight)
def min_box_weight(weights, k):
    low, high = max(weights), sum(weights)
    # low = ของที่หนักที่สุด (ต้องใส่ได้แน่นอน)
    # high = น้ำหนักรวมของทั้งหมด (ถ้าใส่ทุกชิ้นในกล่องเดียว)

    while low < high:
        mid = (low + high) // 2   # เดาน้ำหนักสูงสุดของกล่องแต่ละใบ
        # ถ้าแบ่งได้ไม่เกิน k กล่อง หมายความว่า mid ยังใหญ่เกินไป
        if can_divide(weights, k, mid):
            high = mid            # ลดลงเพื่อหาค่าที่น้อยกว่า
        else:
            low = mid + 1         # ไม่ได้ mid เล็กไป ต้องเพิ่มขึ้น
    return low                    # เมื่อจบ loop ค่า low คือคำตอบที่เหมาะสมที่สุด



s = input("Enter Input : ")
    

    
left, right = s.split('/')
    
weights = list(map(int, left.split()))
    
k = int(right)

    
result = min_box_weight(weights, k)

   
print(f"Minimum weigth for {k} box(es) = {result}")
