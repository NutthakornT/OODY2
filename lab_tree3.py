class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self, root=None):
        self.root = None if root is None else root

    def insert(self, data):
        self.root = BST.add(self.root, data)
        return self.root

    def add(root, data):
        # print("Hi")
        # print(f"root-->{root}")
        # global lst
        # lst = []
        # lst.append(data)
        if root is None:
            return Node(data)
        else:
            if data < root.data:

                root.left = BST.add(root.left, data)
                # print(f"left->{data}")
            elif data > root.data:
                root.right = BST.add(root.right, data)

                # print(f"right->{data}")

        # Code Here

        # lst.append(data)
        # print(lst)
        return root  # return root to insert() function

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
            self.printTree(node.left, level + 1)


def find_sum(node):
    if node is None:
        return 0
    return node.data + find_sum(node.left) + find_sum(node.right)


def update_tree(node, num):
    if node:
        if node.data > num:
            node.data *= num
        update_tree(node.left, num)
        update_tree(node.right, num)


T = BST()
print("**Sum of tree**")
inp, num_khun = input("Enter input : ").split("/")
inp = list(map(int, inp.split(" ")))
# print(inp)
num_khun = int(num_khun)
# print(inp)
# print(target)
for i in inp:
    root = T.insert(i)  # return from insert()
print()
print("Tree before:")
T.printTree(root)

sum_sum = find_sum(root)
print(f"Sum of all nodes = {sum_sum}")
print()
update_tree(root, num_khun)
print("Tree after:")
T.printTree(root)
sum_sum_after = find_sum(root)
print(f"Sum of all nodes = {sum_sum_after}")
# print(lst)
