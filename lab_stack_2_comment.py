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

    def peek(self):  # ใช้ดู top of stack
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


def find_plate_all(target_item, list_plates_available, max_plate):
    each_side_stack = Stack()
    sorted_plates = sorted(list_plates_available, reverse=True)
    remaining = target_item  # we gonna decrease this one (target weight)

    for plate in sorted_plates:

        while (
            remaining >= plate and each_side_stack.size() < max_plate
        ):  # skio heavier plate than remaining item
            each_side_stack.push(plate)
            remaining -= plate
        if remaining == 0:
            break

    if remaining != 0:
        return None
    pass
    return each_side_stack


def format_weight(w: float):
    if w == 85:
        return "85.0"
    return str(int(w) if w.is_integer() else f"{w:.1f}")


#########################################################################

weights = input("Enter needed weight(s): ")
weights = list(map(float, weights.split()))
max_plate = 5
Bar_item = 20
plates = [1.25, 2.5, 5, 10, 15, 20, 25]

plates_s = Stack(plates)
item_s = Stack(weights)

current_stack = Stack()  ######

for weight in weights:
    if weight < Bar_item or (weight - Bar_item / 2) % 1.25 != 0:
        print(f"It's impossible to achieve the item you want({weight}).")

    each_side_item = (weight - Bar_item) / 2

    new_stack = find_plate_all(each_side_item, plates, max_plate)

    if new_stack is None:
        print("new_stack is None, Check find_plate_all func.")
        break

    # pu = []
    # po = []
    pu = Stack()
    po = Stack()

    old_stack_t = current_stack.copy()
    new_stack_t = new_stack.copy()
    print(f"old = {old_stack_t.item}")
    print(f"new = {new_stack_t.item}")

    for plate in current_stack.item:
        if plate in new_stack.item:
            new_stack_t.pop(plate)
            old_stack_t.pop(plate)
    print(f"old_stack_t = {old_stack_t.item}")
    print(f"new_stack_t = {new_stack_t.item}")
    ### PU
    for i in new_stack_t.item:  # big --> small
        pu.push(i)
    ### PO
    # print(f" ------->{pu.item}")
    for i in reversed(old_stack_t.item):  # small --> big
        po.push(i)

    po_print = [f"PO:{p} " for p in po.item]
    pu_print = [f"PU:{p} " for p in pu.item]

    left_side = "".join(
        f"[{int(p) if p.is_integer() else p}]" for p in reversed(new_stack.item)
    )
    right_side = "".join(f"[{int(q) if q.is_integer() else q}]" for q in new_stack.item)

    # dash line
    dash_count = 5 - new_stack.size()
    dash_line = "-" * dash_count
    # print(f"dash_count ------------------------> {dash_count}")
    bench_press_bar = f"{dash_line}{left_side}|======|{right_side}{dash_line}"

    # format weight ;)
    formatted_weight = format_weight(weight)
    ##################
    if not po_print and not pu_print:
        print(f"{bench_press_bar} => {formatted_weight} KG.")
    else:
        print(
            f"{''.join(po_print)}{''.join(pu_print)}=> {bench_press_bar} => {formatted_weight} KG."
        )

    ##################
    current_stack = new_stack.copy()
    # print(new_stack.item)
