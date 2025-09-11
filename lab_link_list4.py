class Node:
    def __init__(self, data, next=None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next
        pass


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0
        pass

    def append(self, data):
        p = Node(data)
        if self.head == None:  # null list
            self.head = p
        else:
            t = self.head  # set t at the front of the list
            while t.next != None:  # if == None == you reach the end of the list
                t = t.next  # next if still not the end
            t.next = p #append to the back
            self.size += 1 #increase size
        pass

    def add_head(self, data):
        p = Node(data)
        p.next = self.head
        self.head = p
        self.size += 1
        pass

    def isEmpty(self):
        return self.head is None

    def remove_head(self):
        if self.head == None:
            return
        if self.head.next == None:
            p = self.head  # have only 1 element
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
        pass

    def remove_tail(self):
        if self.head == None:
            return
        if self.head.next == None:
            self.head == None
            self.size -= 1
            return
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = p.next.next
            self.size -= 1
        pass

    def print_list(self):
        p = self.head
        while p != None:
            
            if p.next is None:
                print(p.data)
            else:
                print(p.data, end=" ")
            p = p.next
         
        pass

    def insertAfter(self, i, data):
        p = Node(data)
        q = self.head
        count = 0
        while q != None:
            if count == i:  # insert in position i
                p.next = q.next
                q.next = p
                return
            q = q.next
            count += 1

    def deleteAfter(self, i):
        q = self.head
        count = 0
        while q != None and q.next != None:
            if count == i:
                p = q.next
                q.next = p.next
                q = None
                self.size -= 1
            q = q.next
            count += 1

        pass

    def find_tail(self):
        p = self.head
        while p.next != None:

            p = p.next
        return p.data
        pass

    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node.data))
            node = node.next
        return " ".join(ans)

    # def add_working_ant(self):
    #     p = self.head
    #     target = "A1"
    #     while p.data != "A1" and p != None:
    #         if p.data == "W2":
    #             print("Hi")
    #         p = p.next
    #     pass
    
    def find_index_last_worker(self):
        p = self.head
        i = 0
        while p != None and p.data != "A1":
            if p.data[:1] == "W":
                i+=1
            p = p.next
        return i-1
    
    def find_index_last_army(self):
        p = self.head
        i = 0
        while p!= None:
            if p.data[:1] == "A":
                i+=1
                # print("Hi") 
            p = p.next
        return i-1
        pass
    
    def is_there_a_worker(self):
        w = Linked_List()
        p = self.head
        check = 0
        
        while p != None:
            if p.data[:1] == "W":   
                w.append(p.data)            
                check = 1    
            p = p.next
        
        if check == 0:
            return False
        elif check == 1:
            print(f"-> Remaining worker ants: {w}")
            return True
        pass
    
    def is_there_a_worker_not_print(self):
        p = self.head
        check = 0
        
        while p != None:
            if p.data[:1] == "W":   
                           
                check = 1    
            p = p.next
        
        if check == 0:
            return False
        elif check == 1:
            return True
        pass

    def is_there_a_soldier(self):
        x = Linked_List()
        p = self.head
        check = 0
        
        while p != None:
            if p.data[:1] == "A":
                x.append(p.data)
                check = 1
            p = p.next

        if check == 0:
            return False
        elif check == 1:
            print(f"-> Remaining soldier ants: {x}")
        pass

print("***This colony is our home***")
inp = input("Enter input : ")
pre_add,cmd = inp.split("/")
#cmd : C 5,F 10,S,W 1,A 1,S
w_ant,a_ant = pre_add.split(" ")
cmd = cmd.split(",")
# print(cmd) #['C 5', 'F 10', 'S', 'W 1', 'A 1', 'S']
w_ant = int(w_ant)
a_ant = int(a_ant)
link_lst = Linked_List()
if w_ant != 0:
    for i in range(1,w_ant+1):
        s = ""
        s = "W" + str(i)
        link_lst.append(s)

if a_ant != 0:
    for i in range(1,a_ant+1):
        s = ""
        s = "A" + str(i)
        link_lst.append(s)

print("Current Ant List: ",end="")
if link_lst.isEmpty():
    print("Empty")
else:
    link_lst.print_list()
print()
queen_angry  = 0
nest_fall = 0
for i in cmd:
    

    if nest_fall == 1:
        print("Ant nest has fallen!")
        break

    if i[:1] == "W": # add Worker 
        amount = int(i[2])
        
        for i in range(amount): 
            if link_lst.isEmpty(): #or link_lst.head.data[:1] == 'A':
                s = ""
                s = "W" + str(i+1)
                link_lst.append(s)
            elif link_lst.head.data[:1]== "A": # add Worker behind Army ant
                if link_lst.is_there_a_worker_not_print() == False:
                    s = ""
                    s = "W" + str(i+1)
                    link_lst.append(s)
                else:
                    current = link_lst.head
                    while current.data[:1] != "W" and current.next != None:
                        current = current.next
                    last_number = current.data[1:]
                    last_number = int(last_number)
                    s = ""
                    s = "W" + str(last_number+1)
                    link_lst.append(s)
                pass
            else:
                ind = link_lst.find_index_last_worker() #1
                s = ""
                s += "W" + str(ind+2) # W1 W2 return index = 1, want W3 so +2 
                link_lst.insertAfter(ind,s)

        # print("Insert W :")
        # link_lst.print_list()   
        pass
    elif i[:1] == "A": # add army ant
        amount_a = int(i[2])
        
        for i in range(amount_a):
            if link_lst.isEmpty():
                s = ""
                s = "A" + str(i+1)
                link_lst.append(s) #at the back
            else:
                ind_a = link_lst.find_index_last_army()
                s_a = ""
                s_a += "A" + str(ind_a+2)
                link_lst.append(s_a)


        # print("Insert A :")
        # link_lst.print_list()
        # for i in range(amount):
        #     ind = link_lst
        pass
    elif i[:1] == "C": #carry
        carry_mission = Linked_List() # keep how many go to work
        item_left = int(i[2:])
        # print(item_left) #5
        p = link_lst.head
        while p!= None :
            if p.data[:1] == "W":
                item_left -= 2
                carry_mission.append(p.data)
                link_lst.remove_head()
                if item_left < 0:
                    item_left = 0
            elif p.data[:1] == "A":
                item_left -= 5
                carry_mission.append(p.data)
                if item_left < 0:
                    item_left = 0
                link_lst.remove_head()
            # link_lst.print_list()
            if item_left == 0:
                break
            
            p = p.next
            pass
        # print(item_left)
        if carry_mission.isEmpty():
            print("Food carrying mission : Empty")
        else:
            print(f"Food carrying mission : {carry_mission}")
        
        # print(item_left)
        if item_left > 0 and link_lst.isEmpty():
            print("The food load is incomplete!")
            print("Queen is angry! ! !")
            queen_angry += 1

        if queen_angry == 3:
            print("**The queen is furious! The ant colony has been destroyed**")
            break
        pass
    elif i[:1] == "F":
        attack_mission = Linked_List() # keep how many go to work
        hp_left = int(i[2:])
        # print(hp_left)          
        q = link_lst.head
        while not link_lst.isEmpty() and  q != None:
            if q.data[:1] == "W":
                hp_left -= 5 #worker
                attack_mission.append(q.data)
                link_lst.remove_head()
                if hp_left < 0:
                    hp_left = 0
            elif q.data[:1] == "A":
                hp_left -= 10 #army
                attack_mission.append(q.data)
                link_lst.remove_head()
                if hp_left < 0:
                    hp_left = 0
            
            if hp_left == 0:
                break
            
            q = q.next
        print(f"Attack mission : {attack_mission}")

        if hp_left > 0 and link_lst.isEmpty():
            nest_fall = 1
        pass
    elif i[:1] == "S":
        if link_lst.is_there_a_worker() == False:
            print("-> Remaining worker ants: Empty")
            pass
        if link_lst.is_there_a_soldier() == False:
            print("-> Remaining soldier ants: Empty")
            pass
        pass
# print(w_ant)
# print(a_ant)
# print(pre_add)
# link_lst.add_working_ant()
