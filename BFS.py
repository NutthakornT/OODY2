class BST:
    def __init__(self,root=None):
        if root is None:
            self.root = None
        else:
            self.root = root
        pass
    class Node:
        def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None

            pass
        def __str__(self):
            return str(self.data)
        
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
    
    def printTree(self,node,level = 0):
        if node is not None:
            self.printTree(node.right,level+1)
            print("     "*level,node.data)
            self.printTree(node.left,level+1)
    def bfs(self):
        if self.root is None:
            return []
        queue = [self.root]
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current.data)
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)
        return result
    def post_order(self,node,arr=None):
        if arr is None: arr = []
        if node:
            self.post_order(node.left,arr)
            self.post_order(node.right,arr)
            arr.append(node.data)
        return arr
    def in_order(self,node,arr=None):
        if arr is None: arr = []
        if node:
            self.in_order(node.left,arr)
            arr.append(node.data)
            self.in_order(node.right,arr)
        return arr
    def pre_order(self,node,arr=None):
        if arr is None: arr = []
        if node:
            arr.append(node.data)
            self.pre_order(node.left,arr)
            self.pre_order(node.right,arr)
        return arr
    def deleteNode(self,root,key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.deleteNode(root.left,key)
        elif key > root.data:
            root.right = self.deleteNode(root.right,key)
        else:
            #found
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:  
                temp = self.find_min(root.right)
                root.data = temp.data   
                root.right = self.deleteNode(root.right,temp.data)
        return root
    def find_min(self,node):
        
        while node.left:
            node = node.left
        return node
    def findpath(self,root):
        path_all = []
        current_path = []
        def dfs(node):
            if node is None:
                return None
            current_path.append(node.data)
            if node.left is None and node.right is None:
                path_all.append(current_path.copy())
            else:
                dfs(node.left)
                dfs(node.right)
            
            current_path.pop()
                
                
            
        dfs(root)
        return path_all

T = BST()
inp = input("Enter Input: ")
inp = inp.split(" ")
for i in inp:
    root = T.add(int(i))

T.printTree(root)


print("Level Order :",*T.bfs())
print("In Order :",*T.in_order(root))
print("Pre Order :",*T.pre_order(root))
print("Post_order" ,*T.post_order(root))


path = T.findpath(root)
print(path)

T.root = T.deleteNode(T.root,9)
T.printTree(T.root)

 