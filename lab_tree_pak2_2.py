class AVLTree:

    class AVLNode:

        def __init__(self, data, left=None, right=None):

            self.data = data

            self.left = None if left is None else left

            self.right = None if right is None else right

            self.height = self.setHeight()

        def __str__(self):

            return str(self.data)

        def setHeight(self):

            a = self.getHeight(self.left)

            b = self.getHeight(self.right)

            self.height = 1 + max(a, b)

            return self.height

        def getHeight(self, node):

            return -1 if node == None else node.height

        def balanceValue(self):

            return self.getHeight(self.right) - self.getHeight(self.left)

    def __init__(self, root=None):

        self.root = None if root is None else root

    def add(self, data):
        self.root = AVLTree._add(self.root, data)
        return self.root
        # code here

    def _add(root, data):
        if root is None:
            return AVLTree.AVLNode(data)

        if data < root.data:
            root.left = AVLTree._add(root.left, data)
        # elif data > root.data:
        #     root.right = AVLTree._add(root.right, data)
        # else:
        #     return root
        else:
            root.right = AVLTree._add(root.right, data)

        root.setHeight()
        balance_facto = root.balanceValue()

        # left heavy
        if balance_facto < -1:
            if data < root.left.data:
                return AVLTree.rotateRightChild(root)
            else:
                if root.left is not None:
                    root.left = AVLTree.rotateLeftChild(root.left)
                return AVLTree.rotateRightChild(root)
            pass
        # right heavy
        if balance_facto > 1:
            if data > root.right.data:
                return AVLTree.rotateLeftChild(root)
            else:
                if root.right is not None:
                    root.right = AVLTree.rotateRightChild(root.right)
                return AVLTree.rotateLeftChild(root)
            pass
        return root
        # code here

    def rotateLeftChild(root):
        if root is None or root.right is None:
            return root
        y = root.right
        T2 = y.left

        y.left = root
        root.right = T2

        root.setHeight()
        y.setHeight()
        # before:
        #  root
        #    \
        #     y
        #    / \
        #  T2   R
        # after:
        #     y
        #    / \
        # root   R
        #    \
        #     T2
        return y
        pass
        # code here

    def rotateRightChild(root):
        if root is None or root.left is None:
            return root
        y = root.left
        T3 = y.right

        y.right = root
        root.left = T3

        root.setHeight()
        y.setHeight()
        # before:
        #    root
        #    /
        #   y
        #  / \
        # L   T3
        # after:
        #     y
        #    / \
        #   L   root
        #        /
        #      T3
        return y
        pass
        # code here

    def postOrder(self):
        AVLTree._postOrder(self.root)
        pass
        # code here

    def _postOrder(root):
        if root:
            AVLTree._postOrder(root.left)
            AVLTree._postOrder(root.right)
            print(root.data, end=" ")

        pass
        # code here

    def printTree(self):

        AVLTree._printTree(self.root)

        print()

    def _printTree(node, level=0):

        if not node is None:

            AVLTree._printTree(node.right, level + 1)

            print("    " * level + str(node.data)) #for no space line in the front

            AVLTree._printTree(node.left, level + 1)


def check_same_tree(Tree1, Tree2):  # its a Node
    if Tree2 is None and Tree1 is None:
        return True
    if Tree1 is not None and Tree2 is not None:
        return (
            Tree1.data == Tree2.data
            and check_same_tree(Tree1.left, Tree2.left)
            and check_same_tree(Tree1.right, Tree2.right)
        )
    return False

    pass


Tree1 = AVLTree()

Tree2 = AVLTree()


Tree1_inp, Tree2_inp = (input("Enter Tree1/Tree2 : ")).split("/")

Tree1_inp = Tree1_inp.split()

Tree2_inp = Tree2_inp.split()


for data in Tree1_inp:

    Tree1.add(int(data))


for data in Tree2_inp:

    Tree2.add(int(data))


print("Tree 1")

Tree1.printTree()


# print()

print("Tree 2")

Tree2.printTree()


# print()

if check_same_tree(Tree1.root, Tree2.root):

    print("Same Tree")

else:

    print("Different Tree")
