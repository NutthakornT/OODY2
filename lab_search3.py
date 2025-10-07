class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,size,maxcollision):
        self.size = size
        self.maxcollision = maxcollision
        self.table = [None] * size
        self.is_it_print_full = False   

        pass
    pass

    def is_full(self):
        for item in self.table:
            if item is None:
                return False
        return True

        pass
    def hash_this_n(self,key):
        return sum(ord(character) for character in key) % self.size
    def insert(self,data):
        # print(data.key)
        if self.is_full():
            if self.is_it_print_full is not True:

                print("This table is full !!!!!!")
                self.is_it_print_full = True
            return

        index = self.hash_this_n(data.key)
        collision = 0
        original_index  = index
        while self.table[index] is not None: # if same index, = collision, do quadratic 
            collision += 1
            
            if collision > self.maxcollision:
                print("Max of collisionChain")
                self.display_table()
                return
            print(f"collision number {collision} at {index}")
            index = (original_index + collision ** 2) % self.size # quadratic probe
        self.table[index] = data #(1+1, I) formatted
        self.display_table()
        pass
    
    def display_table(self):
        for i in range(self.size):

            print(f"#{i+1}      {self.table[i]}")
        print("---------------------------")
    # Code Here


print(" ***** Fun with hashing *****")
inp = input("Enter Input : ")
sizemax,data = inp.split("/")
tablesize, maxcollision = sizemax.split(" ")
tablesize = int(tablesize)
# print(tablesize)
maxcollision = int(maxcollision)
data = list(map(str,data.split(",")))
# print(tablesize,maxcollision)
# print(data)
h = hash(tablesize,maxcollision)

for data in data:
    key, value = data.split()
    h.insert(Data(key,value))