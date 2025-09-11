class Node:
    def __init__(self, data, next=None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next
        pass


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0
        pass

    def append(self, data):
        p = Node(data)
        if self.head == None:  # null list
            self.head = p
        else:
            t = self.head  # set t at the front of the list
            while t.next != None:  # if == None == you reach the end of the list
                t = t.next  # next if still not the end
            t.next = p #append at the back
            self.size += 1 #increase size
        pass

    def add_head(self, data):
        p = Node(data)
        p.next = self.head
        self.head = p
        self.size += 1
        pass

    def remove_head(self):
        if self.head == None:
            return
        if self.head.next == None:
            p = self.head  # have only 1 element
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
        pass

    def remove_tail(self):
        if self.head == None:
            return
        if self.head.next == None:
            self.head == None
            self.size -= 1
            return
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = p.next.next
            self.size -= 1
        pass

    def print_list(self):
        p = self.head
        while p != None:
            print(p.data, end="")
            if p.next is not None:
                print(" <- ", end="")

            p = p.next

        pass

    def insertAfter(self, i, data):
        p = Node(data)
        q = self.head
        count = 0
        while q != None:
            if count == i:  # insert in position i
                p.next = q.next
                q.next = p
                return
            q = q.next
            count += 1

    def deleteAfter(self, i):
        q = self.head
        count = 0
        while q != None and q.next != None:
            if count == i:
                p = q.next
                q.next = p.next
                q = None
                self.size -= 1
            q = q.next
            count += 1

        pass

    def find_tail(self):
        p = self.head
        while p.next != None:

            p = p.next
        return p.data
        pass

    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node.data))
            node = node.next
        return " -> ".join(ans)


inp = input("input : ")
inp = list(map(str, inp.split(" ")))
link_list = Linked_List()
for i in inp:
    link_list.append(i)
print("Original")
print(link_list)
print()
print("Process")

# tail = link_list.find_tail()
# print(tail)
# print(link_list.head.data)

# for i in range(link_list.size + 1, -1, -1):
#     print(i)

for x in range(link_list.size, -1, -1):#swap ลดครั้งในตัวถัดๆไป
    prev = None
    current = link_list.head
    for j in range(x):
        temp = current.next
        current.next = temp.next
        temp.next = current
        if prev is not None:
            prev.next = temp
        else:  # if it is the first character
            link_list.head = temp

        prev = temp
        print(link_list)
print()
print("Reverse")
print(link_list)
#         pass
