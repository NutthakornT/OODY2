class BST:
    class Node:
        def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None

            pass
        def __str__(self):
            return str(self.data)
    def __init__(self,root=None):
        if root is None:
            self.root = None
        else:
            self.root = root
        pass

    def add(self,data):
        self.root = BST._add(self.root,data)
        return self.root

    def _add(root,data):
        if root is None:
            return BST.Node(data)
        elif data < root.data:
            root.left = BST._add(root.left,data)
        elif data > root.data:
            root.right = BST._add(root.right,data)
        return root
    def printTree(self,node,level=0):
        if node is not None:
            self.printTree(node.right,level+1)
            print("     "*level,node.data)
            self.printTree(node.left,level+1)

T = BST()
inp = input("Enter Input")
inp = inp.split(" ")
for i in inp:
    root = T.add(int(i))

T.printTree(root)
            


