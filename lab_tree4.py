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


def find_path(root, treasure, escape):
    path_all = []
    current_path = []

    def ods(node, check=0):
        if node is None:
            return
        check
        current_path.append(node.data)
        if node.data == treasure:
            print("Found Treasure !!!")
            check = 1  # find treasure first then exit
        if node.data == escape and check == 1:
            print("Found Escape !!!")
            print("✅ ", end="")
            print(" -> ".join(map(str, current_path)))
            print(">>> Mission Complete <<<")
            return 0
        else:
            print("❌ ", end="")
            print(" -> ".join(map(str, current_path)))
        # if current_path[-1] == treasure:
        #     print("Found Treasure !!!")
        # if current_path[-1] == escape:
        #     print("Found Escape !!!")
        #     print("✅ ", end="")
        #     print(" -> ".join(map(str, current_path)))
        #     check = 1
        #     return
        # else:
        #     print("❌ ", end="")
        #     print(" -> ".join(map(str, current_path)))

        # print(current_path)

        if not node.left and not node.right:
            path_all.append(current_path.copy())  # then pop for the righty path

        else:

            result = ods(node.left, check)
            ############### pop
            if result == 0:
                return 0

            result = ods(node.right, check)
            if result == 0:
                return 0

        current_path.pop()  # to seach for another right path (backtrack)
        return

    result = ods(root)  # call
    # print(path_all)
    return result


T = BST()

inp, treasure, escape = input("Enter Input : ").split("/")
inp = list(map(int, inp.split(" ")))
# print(inp)
treasure = int(treasure)
escape = int(escape)
# print(inp)
# print(target)
for i in inp:
    root = T.insert(i)

T.printTree(root)
print("-------------------------------------------------")
s = find_path(root, treasure, escape)
# print(s)
# print(s) #None
if s == None:
    print(">>> Mission Failed <<<")
