
def is_prime(num):
    if num < 2:
        return False
    elif num ==2:
        return True
    else:
        for i in range(2,num):
            if num%i == 0:
                return False
            
        return True


def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n



class Hash:
    def __init__(self, size, max_collision, threshold):
        self.size = size                     
        self.max_collision = max_collision   
        self.threshold = threshold           
        self.table = [None] * size
        self.order = []           
        print("Initial Table :")
        self.display_table()
        

    
    def display_table(self):
        for i in range(self.size):
            print(f"#{i+1}\t{self.table[i]}")
        print("----------------------------------------")

    
    def hash_func(self, key):
        return key % self.size

    
    def is_full(self):
        filled = sum(x is not None for x in self.table)  
        percent = (filled / self.size) * 100             
        return percent >= self.threshold                 

   
    def insert(self, key):
        print(f"Add : {key}")            

        # Check threshold BEFORE attempting to insert the new key.
        filled_count = sum(x is not None for x in self.table)
        if ((filled_count + 1) / self.size) * 100 >= self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()
               
        index = self.hash_func(key)          
        collision = 0                        
        original_index = index               

       
        while self.table[index] is not None:
            collision += 1
            print(f"collision number {collision} at {index}")
            if collision >= self.max_collision:
                print("****** Max collision - Rehash !!! ******")
                self.rehash()               
                index = self.hash_func(key)          
                collision = 0                        
                original_index = index
                # self.display_table()           
                continue
            
            
            
            index = (original_index + collision ** 2) % self.size # quadratic probe

        
        self.table[index] = key
        self.order.append(key)
        # #rehash
        # if self.is_full():
        #     print("****** Data over threshold - Rehash !!! ******")
        #     self.rehash()
        
        self.display_table()             

    # Rehashing process
    def rehash(self):
        old_data = self.order.copy()
        # old_data = [x for x in self.table if x is not None]  
        old_size = self.size                                 

       
        self.size = next_prime(old_size * 2 ) #new size *****
        
        self.table = [None] * self.size
        # print(self.size)
        
        for item in old_data: #hash agian
            index = self.hash_func(item)
            collision = 0
            original_index = index
            
            while self.table[index] is not None:

                collision += 1
                print(f"collision number {collision} at {index}")
                index = (original_index + collision ** 2) % self.size
            self.table[index] = item
        self.order = old_data.copy()
        # self.display_table() 
        # print("Hi")
        #   



print(" ***** Rehashing *****")
inp = input("Enter Input : ").split("/")

size, max_col, threshold = map(int, inp[0].split())
data = list(map(int, inp[1].split()))


h = Hash(size, max_col, threshold)


for key in data:
    h.insert(key)
