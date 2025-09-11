class Queue:
    def __init__(self, init_list=[]):
        self.item = init_list

    def enqueue(self, data):
        return self.item.append(data)
        pass

    def dequeue(self):
        return self.item.pop(0)
        pass

    def peek(self):
        if not self.item:
            return None
        return self.item[0]  # ใช้ดูตัวแรกของ Queue
        pass

    @property
    def size(self):
        return len(self.item)

    def __str__(self):
        return str(self.item)


print("*****Hot Potato Game*****")
inp = input("Enter Input: ")
names, num_kill = inp.split("/")
names = names.split(",")

# print(type(num_kill))
player = Queue()
for name in names:
    player.enqueue(name)

# print(player.item)
while player.size > 1:
    print(f"{player.peek()} is the first player holding the potato")
    for _ in range(int(num_kill)): #loop till the num_kill
        player.enqueue(player.peek())
        player.dequeue()
        print(f"  Potato passed to: {player.peek()}")
    print(f"Eliminated: {player.peek()}", end="")
    player.dequeue()
    print(f". Remaining players: {player.item}")
print()
print(f"The winner is: {player.item[0]}!")
