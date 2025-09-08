class BST:
    count_last_node = 0
    node_count = 0

    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.data = key

        def __repr__(self):
            return f"{self.data}"

    def __init__(self):
        self.root = None
        self.sum_till_leaf_list = []

    def insert(self, data):
        self.root = BST._add(self.root, data)
        self.sum_till_leaf_list = []
        self.sum_till_leaf(None, [])
        # print(f"After inserting {data}, sum_till_leaf_list: {self.sum_till_leaf_list}")  # Debug
        return self.root

    def _add(root, data):
        if root == None:
            return BST.Node(data)
        elif data < root.data:
            root.left = BST._add(root.left, data)
        elif data >= root.data:
            root.right = BST._add(root.right, data)
        BST.node_count += 1
        return root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
            self.printTree(node.left, level + 1)

    def postOrderRight(self):
        order_list = []
        return BST._postOrderRight(self.root, order_list)

    def _postOrderRight(root, order_list):
        if root is not None:
            order_list.append(root.data)
            BST._postOrderRight(root.right, order_list)
            BST._postOrderRight(root.left, order_list)
            return order_list

    def get_sum(self, root):
        if root is None:
            return 0
        return root.data + self.get_sum(root.left) + self.get_sum(root.right)

    def compare_and_replace(self, root, k):
        if root is not None and root.data > k:
            root.data *= k
        if root.left:
            self.compare_and_replace(root.left, k)
        if root.right:
            self.compare_and_replace(root.right, k)

    def sum_till_leaf(self, node=None, node_list=[]):
        if node == None:
            node = self.root
        if node == None:
            return

        node_copy = node_list.copy()
        node_copy.append(node.data)

        if node.left is None and node.right is None:
            self.sum_till_leaf_list.append(node_copy)
            # print(f"Appending path: {node_copy}")  # Debug

        if node.left:
            self.sum_till_leaf(node.left, node_copy)
        if node.right:
            self.sum_till_leaf(node.right, node_copy)

    def delete(self, data: int):
        self.root = self._delete(self.root, data)
        self.sum_till_leaf_list = []
        self.sum_till_leaf(None, [])
        # print(f"After deleting {data}, sum_till_leaf_list: {self.sum_till_leaf_list}")  # Debug
        return self.root

    def _delete(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            # ลบเฉพาะโหนดที่เป็นใบ (leaf node) เท่านั้น
            if node.left is None and node.right is None:
                return None
            if node.left and node.left.data < data:
                node.left = self._delete(node.left, data)
            if node.right and node.right.data > data:
                node.right = self._delete(node.right, data)
            if node.left and node.left.data == data:
                node.left = self._delete(node.left, data)
            if node.right and node.right.data == data:
                node.right = self._delete(node.right, data)
            # ถ้าไม่ใช่ใบ ไม่ลบโหนด คืนโหนดเดิม
            return node

        return node


def find_sum_list(list: list):
    output = 0
    for i in list:
        output += i
    return output


def format_list(list: list):
    output = ""
    sum = find_sum_list(list)
    for i, data in enumerate(list):
        output += str(data)
        if i < len(list) - 1:
            output += "->"
        else:
            output += " = %s" % sum
    return output


input_data = input(
    "Enter <Create City A (BST)>/<Create conditions and deploy the army>: "
)
inp1 = [int(i) for i in input_data.split("/")[0].split()]
inp2 = [i for i in input_data.split("/")[1].split(",")]
for i, attacker in enumerate(inp2):
    inp2[i] = [attacker.split(" ")[0], int(attacker.split(" ")[1])]

T = BST()
for i in inp1:
    T.insert(i)

print("(City A) Before the war:")
T.printTree(T.root)

less_than = -1
equal = -1
morethan = -1

for index, a in enumerate(inp2):
    if a[0] == "L":
        less_than = a[1]
        equal = -1
        morethan = -1
    elif a[0] == "EQ":
        less_than = -1
        equal = a[1]
        morethan = -1
    elif a[0] == "M":
        less_than = -1
        equal = -1
        morethan = a[1]

    paths_to_print = []
    i = 0
    while i < len(T.sum_till_leaf_list):
        list_of_node_path = T.sum_till_leaf_list
        if (
            less_than != -1
            and find_sum_list(list_of_node_path[i]) < less_than
            and T.root
        ):
            paths_to_print.append(list_of_node_path[i])
            T.delete(list_of_node_path[i][-1])
            i = 0
            continue
        elif (
            morethan != -1 and find_sum_list(list_of_node_path[i]) > morethan and T.root
        ):
            paths_to_print.append(list_of_node_path[i])
            T.delete(list_of_node_path[i][-1])
            i = 0
            continue
        elif equal != -1 and find_sum_list(list_of_node_path[i]) == equal and T.root:
            paths_to_print.append(list_of_node_path[i])
            T.delete(list_of_node_path[i][-1])
            i = 0
            continue
        i += 1

    if paths_to_print:
        print("--------------------------------------------------")
        if a[0] == "L":
            print(f"Removing paths where the sum is less than {less_than}:")
        elif a[0] == "M":
            print(f"Removing paths where the sum is greater than {morethan}:")
        elif a[0] == "EQ":
            print(f"Removing paths where the sum is equal to {equal}:")
        for idx, path in enumerate(paths_to_print, 1):
            print(f"{idx}) {format_list(path)}")
        print("--------------------------------------------------")
        print("(City A) After the war:")
        T.printTree(T.root)
        if T.root == None:
            print("City A has fallen!")
            exit()

    else:
        print("--------------------------------------------------")
        if a[0] == "L":
            print(f"Removing paths where the sum is less than {less_than}:")
            print("No paths were removed.")
        elif a[0] == "M":
            print(f"Removing paths where the sum is greater than {morethan}:")
            print("No paths were removed.")
        elif a[0] == "EQ":
            print(f"Removing paths where the sum is equal to {equal}:")
            print("No paths were removed.")
        print("--------------------------------------------------")
        print("(City A) After the war:")
        T.printTree(T.root)
        print("City A has fallen!") if T.root == None else None
