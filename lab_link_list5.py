class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node
        self.size += 1

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" → " if current.next else "\n")
            current = current.next

    def find_current(self, i):
        current = self.head
        count = 1
        while current.next and count < i:
            current = current.next
            count += 1

        return current

    def peek(self, index):
        check = 0
        current = self.head
        for i in range(self.size):

            if i == index:
                return current  # return Node
            if current is None:
                return None
            current = current.next
        return None


print(" *** Ant Army ***")
inp = input("Input : ")
lst, k = inp.split(",")
lst = list(map(str, lst.split(" ")))
# print(lst)
k = int(k)

# print(type(k))
link_lst = LinkedList()
for i in lst:
    link_lst.append(i)
# print(link_lst.size) # 1-26 size == 25
print("Before : ", end="")
link_lst.print_list()
# link_lst.print_list()
# print(link_lst.size)
if k > link_lst.size:
    k = link_lst.size + 1  # force k to be the size of link_lst
if k != 0:
    for i in range(0, link_lst.size, k * 2): #skip เป็นช่วงๆ
        # print(f"i ---> {i}")
        # print(f"k ---> {k}")
        if k > link_lst.size - i + 1: #limit k size
            k = link_lst.size - i + 1
            # print(k)

        for j in range(k - 1, -1, -1): #swap
            prev = None
            head = link_lst.peek(i)
            # print(f"head = {head}")
            # print(head)
            current = head
            if current is None:
                break

            for _ in range(j):

                temp = current.next
                if temp is None:
                    break
                current.next = temp.next
                temp.next = current
                if prev is not None:
                    prev.next = temp
                elif i == 0:  # if it is the first character
                    link_lst.head = temp  # head still at the front
                else:
                    a = link_lst.peek(i - 1)  # q = index 5 if i == 6
                    a.next = temp
                    # print(a.next)
                # for i in range(k - 1):
                #     temp = temp.next

                prev = temp
                # link_lst.print_list()
            # print(j)
            pass

        pass


print("After : ", end="")
link_lst.print_list()
# print(f"After : {link_lst.print_list()}")
# current = link_lst.head
# count = 0
# while current:
#     if count == k:
#         print(count)
#     current = current.next
