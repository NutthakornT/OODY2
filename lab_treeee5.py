class BST:
    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.data = key

        def __repr__(self):
            return f"{self.data}"

    def __init__(self):
        self.root = None
        self.sum_till_leaf_list = []  #######

    def insert(self, data):
        self.root = BST._add(self.root, data)
        self.sum_till_leaf_list = []
        self.sum_till_leaf(None, [])
        return self.root

    def _add(root, data):
        if root is None:
            return BST.Node(data)
        elif data < root.data:
            root.left = BST._add(root.left, data)
        else:
            root.right = BST._add(root.right, data)
        return root

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
            self.printTree(node.left, level + 1)

    def sum_till_leaf(self, node=None, path=[]):
        if node is None:
            node = self.root  # start root
        if node is None:
            return

        path_copy = path.copy()
        path_copy.append(node.data)

        if node.left is None and node.right is None:
            self.sum_till_leaf_list.append(path_copy)  # append path

        if node.left:
            self.sum_till_leaf(node.left, path_copy)
        if node.right:
            self.sum_till_leaf(node.right, path_copy)

    def delete_leaf(self, value):
        self.root = self._delete_leaf(self.root, value)
        self.sum_till_leaf_list = []
        self.sum_till_leaf(None, [])  #
        return self.root

    def _delete_leaf(self, node, value):
        if node is None:
            return None
        # leaf
        if (
            node.data == value and node.left is None and node.right is None
        ):  # get to that leaf and delete
            return None  # delete leaf
        # visit
        node.left = self._delete_leaf(node.left, value)
        node.right = self._delete_leaf(node.right, value)
        return node


def find_sum_list(path):
    return sum(path)


def format_path(path):
    return "->".join(map(str, path)) + f" = {sum(path)}"


input_data = input(
    "Enter <Create City A (BST)>/<Create conditions and deploy the army>: "
)
numbers = list(map(int, input_data.split("/")[0].split()))
conditions = [c.strip() for c in input_data.split("/")[1].split(",")]

T = BST()
for num in numbers:
    T.insert(num)

print("(City A) Before the war:")
T.printTree(T.root)
###########################
for cond in conditions:
    paths_removed = []
    condition, value = cond.split()
    value = int(value)

    i = 0
    while i < len(T.sum_till_leaf_list):
        path = T.sum_till_leaf_list[i]
        total = find_sum_list(path)

        remove = False
        if condition == "L" and total < value:
            remove = True
        elif condition == "EQ" and total == value:
            remove = True
        elif condition == "M" and total > value:
            remove = True

        if remove:
            paths_removed.append(path)  # if true = that path will be remove
            T.delete_leaf(path[-1])  # leaf of that path
            i = 0  # restart
        else:
            i += 1  # no need remove = next path

    print("--------------------------------------------------")
    if condition == "L":
        print(f"Removing paths where the sum is less than {value}:")
    elif condition == "EQ":
        print(f"Removing paths where the sum is equal to {value}:")
    elif condition == "M":
        print(f"Removing paths where the sum is greater than {value}:")

    if paths_removed:
        for idx, path in enumerate(paths_removed, 1):
            print(f"{idx}) {format_path(path)}")
    else:
        print("No paths were removed.")

    print("--------------------------------------------------")
    print("(City A) After the war:")
    if T.root:
        T.printTree(T.root)
    else:  # not root
        print("City A has fallen!")
        break
