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


def find_path_sum(root):
    path_all = []
    current_path = []

    def ods(node):
        # if node is None:
        #     return
        # current_path.append(node.data)
        # # print(current_path)
        # # path_all.append(
        # #     current_path.copy()
        # # )  # append every step ******************************
        # if not node.left and not node.right:
        #     path_all.append(current_path.copy())  # append  [100, 200, 300]

        # # else:
        # #     ods(node.left)
        # #     ############### pop
        # #     ods(node.right)
        # elif (node.left is None) != (node.right is None):
        #     if node.left:
        #         ods(node.left)
        #     else:
        #         ods(
        #             node.right
        #         )  # append  [100, 200, 300] first cause no left at node 200
        #     path_all.append(current_path.copy())

        # else:
        #     ods(node.left)
        #     ods(node.right)

        # current_path.pop()  # to seach for another right path (backtrack)
        # # print("Hi")
        if node is None:
            return
        current_path.append(node.data)

        # first go deeper
        ods(node.left)
        ods(node.right)

        # then append this path (after children)
        path_all.append(current_path.copy())

        current_path.pop()

    ods(root)  # call
    # print(path_all)
    return path_all


def remove_leaf(node, target, condition, current_sum=0):
    if node is None:
        return None

    current_sum += node.data
    node.left = remove_leaf(node.left, target, condition, current_sum)
    node.right = remove_leaf(node.right, target, condition, current_sum)
    if condition == "L":

        if not node.left and not node.right and current_sum < target:
            return None
    if condition == "EQ":

        if not node.left and not node.right and current_sum == target:
            return None
    if condition == "M":

        if not node.left and not node.right and current_sum > target:
            return None
    return node


T = BST()

inp, conditions = input(
    "Enter <Create City A (BST)>/<Create conditions and deploy the army>: "
).split("/")
conditions = conditions.split(",")
# print(conditions)


inp = list(map(int, inp.split(" ")))
# print(inp)
# print(l)
# print(eq)
# print(m)
# print(inp)
# print(target)
for i in inp:
    root = T.insert(i)

print("(City A) Before the war:")
T.printTree(root)
# print(find_path_sum(root))

count_print_stupid_line = 0
length = len(conditions) - 1
print("--------------------------------------------------")
for i in conditions:

    if count_print_stupid_line == length:
        c = 1
    else:
        c = 0

    i.strip()

    if i[0:1] == "L":
        condi = "L"
        l = int(i[2:])
        count = 0
        all_path = find_path_sum(root)
        print(all_path)
        print(f"Removing paths where the sum is less than {l}:")
        for i in all_path:
            if sum(i) < l and len(i) > 1:
                count += 1

                print(f"{count}) {'->'.join(map(str,i))} = {sum(i)}")

                root = remove_leaf(root, l, condi)

        print("--------------------------------------------------")
        print("(City A) After the war:")
        T.printTree(root)
        if c == 0:
            print("--------------------------------------------------")

    elif i[0:2] == "EQ":
        condi = "EQ"
        eq = int(i[3:])
        count = 0
        all_path = find_path_sum(root)
        print(all_path)
        print(f"Removing paths where the sum is equal to {eq}:")
        for i in all_path:
            if sum(i) == eq:
                count += 1

                print(f"{count}) {'->'.join(map(str,i))} = {sum(i)}")

                root = remove_leaf(root, eq, condi)
        print("--------------------------------------------------")
        print("(City A) After the war:")
        if not root:
            print("City A has fallen!")
            break
        T.printTree(root)
        if c == 0:
            print("--------------------------------------------------")

    elif i[0:1] == "M":

        condi = "M"
        m = int(i[2:])
        count = 0
        all_path = find_path_sum(root)
        print(all_path)
        print(f"Removing paths where the sum is greater than {m}:")
        for i in all_path:
            if sum(i) > m and len(i) > 1:

                count += 1

                print(f"{count}) {'->'.join(map(str,i))} = {sum(i)}")

                root = remove_leaf(root, m, condi)
        print("--------------------------------------------------")
        print("(City A) After the war:")
        T.printTree(root)
        if c == 0:
            print("--------------------------------------------------")

    count_print_stupid_line += 1
# print(find_path_sum(root, 250))
