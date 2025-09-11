class AVLTree:
    def __init__(self):
        self.root = None

    def insertMovie(self, movie):  
        self.root = self._insert(self.root, movie)

    def _insert(self, node, movie):
        if not node:
            return Node(Movie(movie[0], movie[1]))
        if movie[1] < node.data.rating:
            node.left = self._insert(node.left, movie)
        elif movie[1] >= node.data.rating:
            node.right = self._insert(node.right, movie)
        node.setHeight()
        return self.balance(node)

    def removeMovie(self, movieName):
        self.root = self._remove(self.root, movieName)

    def _remove(self, node, movieName):
        if not node:
            return node
        
        if node.data.title == movieName:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self.getMin(node.right)
            node.data = temp.data #เอาค่าน้อยสุดฝั่งขวาขึ้นมาเป็น root แทน
            node.right = self._remove(node.right, temp.data.title)#ลบค่าที่ดึงมาออก
        node.left = self._remove(node.left, movieName)
        node.right = self._remove(node.right, movieName)
        node.setHeight()
        return self.balance(node)
        

    def top(self, number):
        # self.printTree(self.root)
        return  self._top(self.root, number)
    def _top(self, node, number, li=None):
        if li is None:
            li = []
        if node is None or len(li) >= number:
            return li
        self._top(node.right, number, li)
        if len(li) < number:
            li.append(node.data)
            # Then traverse left subtree
            self._top(node.left, number, li)
        return li
        
        pass
    def _reverseInOrder(self, node, result, number):
        if node is None or len(result) >= number:
            return
        self._reverseInOrder(node.right, result, number)
        if len(result) < number:
            result.append(node.data)
            self._reverseInOrder(node.left, result, number)

    def getRatingRange(self, start, end):
        result = []
        self._getRatingRange(self.root, start, end, result)
        return result

    def _getRatingRange(self, node, start, end, result):
        if node is None:
            return
        if start <= node.data.rating:
            self._getRatingRange(node.left, start, end, result)
        if start <= node.data.rating <= end:
            result.append(node.data)
        if node.data.rating <= end:
            self._getRatingRange(node.right, start, end, result)

    def balance(self, node):    #balance current node which return new root node
        BF = node.balanceFactor()
        if BF < -1:
            # Left heavy
            if node.left and node.left.balanceFactor() > 0:
                node.left = node.left.rotateLeft()
            return node.rotateRight()
        if BF > 1:
            # Right heavy
            if node.right and node.right.balanceFactor() < 0:
                node.right = node.right.rotateRight()
            return node.rotateLeft()
        return node

    def getMin(self, node): #Get minimum rating node
        current = node
        while current.left:
            current = current.left
        return current

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def isAVL(self):
        return self._isAVL(self.root)

    def _isAVL(self, node):
        if not node:
            return True
        if abs(node.balanceFactor()) > 1:
            return False
        expected_height = 1 + max(node.left.height if node.left else -1, node.right.height if node.right else -1)
        if node.height != expected_height:
            return False
        return self._isAVL(node.left) and self._isAVL(node.right)

    def isBST(self):
        return self._isBST(self.root)

    def _isBST(self, node, min=float('-inf'), max=float('inf')):
        if not node:
            return True
        if not (min <= node.data.rating <= max):
            return False
        return (self._isBST(node.left, min, node.data.rating) and
                self._isBST(node.right, node.data.rating, max))

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return f'{self.data}'

    def balanceFactor(self):    #Get balance factor
        if not self:
            return -1
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        return right_height - left_height

    def setHeight(self):        #Set height base on child node
        a = self.left.height if self.left else -1
        b = self.right.height if self.right else -1
        self.height = 1 + max(a, b)

    def rotateRight(self):      #Rotate right (clockwise)
        new_root = self.left
        self.left = new_root.right
        new_root.right = self
        self.setHeight()
        new_root.setHeight()
        return new_root

    def rotateLeft(self):       #Rotate left (counter-clockwise)
        new_root = self.right
        self.right = new_root.left
        new_root.left = self
        self.setHeight()
        new_root.setHeight()
        return new_root

class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = float(rating)

    def __str__(self):
        return f'{self.title}({self.rating})'

rottenPotato = AVLTree()
movies = [
    ("Megalodon", 5.0),
    ("Inception", 9.1),
    ("The_Dark_Knight", 8.9),
    ("Interstellar", 9.4),
    ("Tenet", 7.2),
    ("Memento", 7.9),
    ("Dunkirk", 7.7),
    ("The_Prestige", 8.3),
    ("Avatar", 7.8),
    ("Titanic", 8.1),
    ("Gladiator", 8.6),
    ("The_Matrix", 9.3),
    ("John_Wick", 7.5),
    ("Parasite", 9.0),
    ("Whiplash", 8.5),
    ("La_La_Land", 8.0),
    ("The_Godfather", 9.2),
    ("Pulp_Fiction", 8.4),
    ("Fight_Club", 8.7),
    ("Forrest_Gump", 8.8)
]

for movie in movies:
    rottenPotato.insertMovie(movie)

inp = input("The Requests From User: ").split(", ")
for request in inp:
    req = request.split(" ")
    if req[0] == "I":
        rottenPotato.insertMovie([req[1], float(req[2])])
    elif req[0] == "D":
        rottenPotato.removeMovie(req[1])
    elif req[0] == "T":
        print(f"Top {req[1]}")
        print([str(movie) for movie in rottenPotato.top(int(req[1]))])
        print()
    elif req[0] == "R":
        print(f'Rating range from {req[1]} to {req[2]}')
        print([str(movie) for movie in rottenPotato.getRatingRange(float(req[1]), float(req[2]))])
        print()
print(f'Is this AVL Tree? {rottenPotato.isAVL() and rottenPotato.isBST()}')