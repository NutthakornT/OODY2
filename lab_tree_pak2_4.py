#normal insert not balsnce code
class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.h = self.update_height()

        def update_height(self): #get height
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.h = 1 + max(a,b)
            return self.h
            pass
        
        def getHeight(self, node):

            return -1 if node == None else node.h
        def balance_factor(self):
            return self.getHeight(self.right) - self.getHeight(self.left)
            pass
        
    def __init__(self):
        self.root = None
    
    def insert(self,key):
        if not self.root:
            self.root = BST.Node(key)
        else:
            BST._insert(self.root,key)

    def _insert(node,key):
        if key < node.data:
            if node.left:
                BST._insert(node.left,key)
            else:
                node.left = BST.Node(key)
        else:
            if node.right:
                BST._insert(node.right,key)
            else:
                node.right = BST.Node(key)
        node.update_height() #update height every time
   

    def _get_format(root,ans = ""):
        if root:
            temp = ""
            if root.right:
                temp += BST._get_format(root.right,ans + "     ")
            temp += f"{ans}{root.data}\n"
            if root.left:
                temp += BST._get_format(root.left,ans + "     ")
            return temp
        return ""
    
    def __str__(self):
        return BST._get_format(self.root)

################################
'''
⠀⠀⢘⣾⣾⣿⣾⣽⣯⣼⣿⣿⣴⣽⣿⣽⣭⣿⣿⣿⣿⣿⣧
⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣰⣯⣾⣿⣿⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
⠀⠀⠛⠛⠋⠁⣠⡼⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠤⣶⣾⣿⣿⣿⣦⡈⠉⠉⠉⠙⠻⣿⣿⣿⣿⣿⠿⠁⠀
⠀⠀⠀⠀⠈⠟⠻⢛⣿⣿⣿⣷⣶⣦⣄⠀⠸⣿⣿⣿⠗⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠀⠄⣿⡿⠋⣉⠈⠙⢿⣿⣦⣿⠏⡠⠂⠀⠀⠀
⠀⠀⠀⠀⢰⡌⠀⢠⠏⠇⢸⡇⠐⠀⡄⣿⣿⣃⠈⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣻⣿⢫⢻⡆⡀⠁⠀⢈⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣻⣷⣾⣿⣿⣷⢾⣽⢭⣍⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⣿⡿⠈⣹⣾⣿⡞⠐⠁⠀⠀⠀⠁⠀⠀⠀
⠀⠀⠀⠨⣟⣿⢟⣯⣶⣿⣆⣘⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡆⠀⠐⠶⠮⡹⣸⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

def isAVL(node : BST.Node):
    if node is None:
        return True 
    if node.balance_factor() < -1 or node.balance_factor() > 1:
        return False
    return isAVL(node.left) and isAVL(node.right)
    pass


################################


tree = BST()

print("**********IsAVL**********")
for i in list(map(int, input("Enter numbers to insert in the tree: ").split())):
    root = tree.insert(i)
print("Tree:")
print(tree)
print("Is AVL???:", isAVL(tree.root))
# print(tree.root.balance_factor())