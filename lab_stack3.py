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


inp = input("Enter Input : ")
start_items, add_items = inp.split("/")
if not start_items:  # add item if no start item
    start_items_stack = Stack()
    add_items = list(add_items.split(","))
    add_items_stack = Stack()
    for i in add_items:
        add_items_stack.push(i)
else:
    start_items = list(map(int, (start_items.split(" "))))
    add_items = list(add_items.split(","))
    start_items_stack = Stack()
    add_items_stack = Stack()

    for i in start_items:
        if i != 0:
            start_items_stack.push(i)

    for i in add_items:
        add_items_stack.push(i)


# print(f" add_item_stack ---->{add_items_stack.item}")
damage = add_items_stack.pop().split(" ")  # damage is at the top of the add_item_stack
damage = int(damage[1])

spawn_items_stack = add_items_stack.copy()
spawn_items_stack_to_add = Stack()
for item in spawn_items_stack.item:
    item_lst = item.split(" ")
    item_lst[1] = int(item_lst[1])
    for i in item_lst:
        if type(i) == int:
            spawn_items_stack_to_add.push(i)  # [10,10,10] spwan

    # print(type(item_lst[0]))
    # print(type(item_lst[1]))


# print(f"new -------->{spawn_items_stack_new.item}")

# print(f" damage ----->{damage}")
# print(f" start item stack ---->{start_items_stack.item}")
# print(f" add_item_stack_after ---->{add_items_stack.item}")
# print(f" spawn_item_stack ---->{spawn_items_stack.item}")
print()
print("start")
print(start_items_stack.item)

for i in spawn_items_stack_to_add.item:
    print()
    print(f"spawn an enemy of {i} HP")
    start_items_stack.push(i)
    print(start_items_stack.item)
# [10, 40, 30, 20, 60, 30, 10, 10]
damage_left = damage
kill = 0
if damage_left <= 0:
    print()
    print("Invalid number")
else:
    while damage_left > 0 and not start_items_stack.isEmpty():
        top_enemy = start_items_stack.pop()
        if damage_left >= top_enemy:
            damage_left -= top_enemy
            kill += 1
        else:
            ememy_still_alive = top_enemy - damage_left
            start_items_stack.push(ememy_still_alive)
            damage_left = 0
    # print(damage)
    # print(kill)
    # print(start_items_stack.item)
    print()
    print(f"deal {damage} damage, killed {kill} enemy")
    print(start_items_stack.item)

    if not start_items_stack.item:
        print()
        print(">>>> Player Wins <<<<")
