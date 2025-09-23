class BST:
    class Node:
        def __init__(self,data):
            self.data = data
            self.right = None
            self.left = None
            pass
        def __str__(self):
            return str(self.data)
            pass
        pass
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
        else:
            root.right = BST._add(root.right,data)
        return root
    
    def printTreee(self,node,level=0):
        if node is not None:
            self.printTreee(node.right,level+1)
            print('     '*level,node)
            self.printTreee(node.left,level+1)

T = BST()
inp = input("Enter Input")
inp = inp.split(" ")
for i in inp:
    root = T.add(int(i))

T.printTreee(root)