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


def find_plate_all(target_item, list_plates_available, max_plate):
    each_side_stack = Stack()
    sorted_plates = sorted(list_plates_available, reverse=True)
    remaining = target_item

    for plate in sorted_plates:

        while remaining >= plate and each_side_stack.size() < max_plate:
            each_side_stack.push(plate)
            remaining -= plate
        if remaining == 0:
            break

    if remaining != 0:
        return None
    pass
    return each_side_stack


def format_weight(w: float):
    return str(int(w) if is_that_damn_number_is_integer(w) else f"{w:.1f}")


def is_that_damn_number_is_integer(number):
    # if type(number) == float:
    #     return False
    # else:
    #     return True

    return number == int(number)


weight = input("Enter needed weight(s): ")
weight_1 = list(map(float, weight.split()))
max_plate = 5
Bar_item = 20
plates = [1.25, 2.5, 5, 10, 15, 20, 25]

plates_s = Stack(plates)
item_s = Stack(weight_1)

current_stack = Stack()

for weight in weight_1:
    if weight < Bar_item or (weight - Bar_item / 2) % 1.25 != 0:
        print(
            f"It's impossible to achieve the weight you want({int(weight) if is_that_damn_number_is_integer(weight) else weight})."
        )
        break
    # print(f"------------------------------------------------>{type(weight)}")
    each_side_item = (weight - Bar_item) / 2

    new_stack = find_plate_all(each_side_item, plates, max_plate)

    if new_stack is None:
        print(
            f"It's impossible to achieve the weight you want({int(weight) if is_that_damn_number_is_integer(weight) else weight})."
        )
        break

    po = Stack()
    pu = Stack()

    # Make mutable copies
    old = current_stack.item.copy()
    new = new_stack.item.copy()

    # Work from OUTERMOST → INWARD
    while old and new and old[0] == new[0]:
        # Both stacks match at top → skip
        old.pop(0)
        new.pop(0)

    # Now we reached mismatch point → must remove ALL remaining old plates
    while old:
        po.push(old.pop(0))  # remove in order (outermost first)

    # After clearing, we now need to add remaining new plates
    while new:
        pu.push(new.pop(0))  # add in order (outermost first)
    # pu = Stack()
    # po = Stack()

    # make mutable copies of the lists
    # old_list = current_stack.item.copy()
    # new_list = new_stack.item.copy()

    # print(f"old_list_before ----------------> {old_list}")
    # print(f"new_list_before ----------------> {new_list}")
    # # remove common plates (one by one to handle duplicates)
    # for plate in sorted(current_stack.item, reverse=True):
    #     if plate in new_list:
    #         new_list.remove(plate)
    #         old_list.remove(plate)

    # # what’s left in old_list → must remove (PO)
    # for plate in sorted(old_list, reverse=True):  # heavier first
    #     po.push(plate)

    # # what’s left in new_list → must add (PU)
    # for plate in sorted(new_list, reverse=True):  # heavier first
    #     pu.push(plate)
    # print(f"old_list ----------------> {old_list}")
    # print(f"new_list ----------------> {new_list}")
    # print(f"PO: ---------------------> {po.item}")
    # print(f"PU: ---------------------> {pu.item}")
    po_print = [f"PO:{p} " for p in reversed(po.item)]
    pu_print = [f"PU:{p} " for p in pu.item]

    left_side = "".join(
        f"[{int(p) if is_that_damn_number_is_integer(p) else p}]"
        for p in reversed(new_stack.item)
    )
    right_side = "".join(
        f"[{int(q) if is_that_damn_number_is_integer(q) else q}]"
        for q in new_stack.item
    )
    # dash line
    dash_count = 5 - new_stack.size()
    dash_line = "-" * dash_count

    bench_press_bar = f"{dash_line}{left_side}|======|{right_side}{dash_line}"

    formatted_weight = format_weight(weight)

    weight = (sum(new_stack.item) * 2) + Bar_item

    if not po_print and not pu_print:
        print(f"{bench_press_bar} => {formatted_weight} KG.")
    else:
        print(
            f"{''.join(po_print)}{''.join(pu_print)}=> {bench_press_bar} => {weight} KG."
        )

    current_stack = new_stack.copy()
    # current_stack = new_stack.copy()
