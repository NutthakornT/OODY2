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
        # print(f"root-->{root}")
        lst = []
        if root is None:
            return Node(data)
        else:
            if data < root.data:

                root.left = BST.add(root.left, data)
                # print(f"left->{data}")
            else:
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


def in_order(node, lst):
    if node:
        in_order(node.left, lst)
        lst.append(node.data)
        in_order(node.right, lst)


def find_path_sum(root, target):
    path_all = []
    current_path = []

    def ods(node):
        if node is None:
            return
        current_path.append(node.data)
        # print(current_path)

        if not node.left and not node.right:
            path_all.append(current_path.copy())  # then pop for the righty path

        else:
            ods(node.left)
            ############### pop
            ods(node.right)

        current_path.pop()  # to seach for another right path (backtrack)
        # print("Hi")

    ods(root)  # call
    # print(path_all)
    return path_all


T = BST()

inp, target = input("Enter the values to insert into BST and target sum : ").split(
    " / "
)
inp = list(map(int, inp.split(" ")))
# print(inp)
target = int(target)

for i in inp:
    root = T.insert(i)  # return from insert()
# T.printTree(root)
# print(f"--->{find_path_sum(root, target)}")

inorder = []
in_order(root, inorder)
print(f"Inorder Traversal of BST :", *inorder)
path_allah = find_path_sum(root, target)
check = 0
for i in path_allah:
    if check == 1:
        break
    else:
        if sum(i) == target:
            print(f"Path with sum {target} exists : True")
            check = 1
        else:
            check = 0

if check == 0:
    print(f"Path with sum {target} exists : False")

#         10
#         /  \
#        9    23
#       /    /
#      1    13
#     / \
#    0   4
