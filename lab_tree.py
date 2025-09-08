# Binary Search Tree (BST) class
class BST:
    # Node class represents each node in the BST
    class Node:
        def __init__(self, key):
            self.left = None  # Left child
            self.right = None  # Right child
            self.data = key  # Node value

        def __repr__(self):
            return f"{self.data}"  # When printing the node, show its value

    def __init__(self):
        self.root = None
        self.sum_till_leaf_list = []  # List of all root-to-leaf paths

    # Public method to insert a new value into the BST
    def insert(self, data):
        self.root = BST._add(self.root, data)  # Insert using recursive helper
        self.sum_till_leaf_list = []  # Recalculate all paths after insertion
        self.sum_till_leaf(None, [])  # Populate sum_till_leaf_list
        return self.root

    # Recursive helper function to insert node into BST
    def _add(root, data):
        if root is None:
            return BST.Node(data)  # Create a new node if empty
        elif data < root.data:
            root.left = BST._add(root.left, data)  # Go left if smaller
        else:
            root.right = BST._add(root.right, data)  # Go right if greater or equal
        return root

    # Print the BST in a readable tree format (rotated sideways)
    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)  # Print right child first
            print("     " * level, node)  # Indent according to level
            self.printTree(node.left, level + 1)  # Print left child

    # Recursive function to find all root-to-leaf paths
    def sum_till_leaf(self, node=None, path=[]):
        if node is None:
            node = self.root
        if node is None:  # BST is empty
            return

        path_copy = path.copy()  # Make a copy of current path
        path_copy.append(node.data)  # Add current node to path

        # If leaf node, append the path to sum_till_leaf_list
        if node.left is None and node.right is None:
            self.sum_till_leaf_list.append(path_copy)

        # Recursively visit left and right children
        if node.left:
            self.sum_till_leaf(node.left, path_copy)
        if node.right:
            self.sum_till_leaf(node.right, path_copy)

    # Delete a leaf node by value
    def delete_leaf(self, value):
        self.root = self._delete_leaf(self.root, value)
        self.sum_till_leaf_list = []  # Update paths after deletion
        self.sum_till_leaf(None, [])
        return self.root

    # Recursive helper to delete a leaf node
    def _delete_leaf(self, node, value):
        if node is None:
            return None
        # Delete only if node is a leaf and matches value
        if node.data == value and node.left is None and node.right is None:
            return None
        # Recursively check left and right subtrees
        node.left = self._delete_leaf(node.left, value)
        node.right = self._delete_leaf(node.right, value)
        return node


# Utility function to calculate sum of a path
def find_sum_list(path):
    return sum(path)


# Utility function to format path for printing
def format_path(path):
    return "->".join(map(str, path)) + f" = {sum(path)}"


# ---------------- MAIN PROGRAM ----------------
# Input format: "<numbers>/<conditions>"
# Example: "50 30 70 20 40 60 80/L 100,EQ 150,M 200"
input_data = input(
    "Enter <Create City A (BST)>/<Create conditions and deploy the army>: "
)

# Split numbers and conditions
numbers = list(map(int, input_data.split("/")[0].split()))
conditions = [c.strip() for c in input_data.split("/")[1].split(",")]

# Create BST and insert numbers
T = BST()
for num in numbers:
    T.insert(num)

# Print initial BST
print("(City A) Before the war:")
T.printTree(T.root)

# Loop over each condition
for cond in conditions:
    paths_removed = []  # Keep track of removed paths

    # Split condition type and target value
    condition, value = cond.split()
    value = int(value)

    i = 0
    # Loop over all root-to-leaf paths
    while i < len(T.sum_till_leaf_list):
        path = T.sum_till_leaf_list[i]
        total = find_sum_list(path)  # Sum of this path

        remove = False
        # Determine if path meets the removal condition
        if condition == "L" and total < value:
            remove = True
        elif condition == "EQ" and total == value:
            remove = True
        elif condition == "M" and total > value:
            remove = True

        if remove:
            paths_removed.append(path)  # Remember path to print later
            T.delete_leaf(path[-1])  # Delete leaf node
            i = 0  # Restart, because paths list changed
        else:
            i += 1

    # Print removed paths
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
    else:
        print("City A has fallen!")
        break
