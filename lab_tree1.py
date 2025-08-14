class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self,root = None):
        self.root = None if root is None else root

    def insert(self, data):
        self.root = BST.add(self.root,data)
        return self.root
        
        
        
    def add(root,data):
        lst = []
        if root is None:
            return Node(data)
        else:
            if data < root.data:
      
                root.left = BST.add(root.left,data)
            else:
                root.right = BST.add(root.right,data)
            
        # Code Here
        
        lst.append(data)
        print(lst)
        return root # return root to insert() function
         
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i) #return from insert()
T.printTree(root)