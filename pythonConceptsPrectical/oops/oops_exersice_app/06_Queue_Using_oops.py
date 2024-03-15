#FIFO - First In First Out
class queue:
    def __init__(self,max_length):
        self.li=[]
        self.max_length = max_length
        
    def is_empty(self):
        return len(self.li) == 0
    
    def is_full(self):
        return len(self.li) == self.max_length
    
    def add_ele(self,ele):
        if not self.is_full():
            self.li.append(ele)
        else:
            print(f"Queue is full {self.li}")

    def rem_ele(self):
        if not self.is_empty():
            return self.li.pop(0)
        else:
            print(f"Queue is empty {self.li}")
            
    def show_ele(self):
        print("Queue:", self.li)
            
my_queue = queue(max_length=5)

while True:
    print("------Choice One------")
    print("1). Add queue")
    print("2). Remove queue")
    print("3). Show queue")
    print("4). Exit")
    print("-"*10)
    
    ch = input("Enter your choice : ")
    
    if ch == "1":
        ele = input("Enter The element : ")
        my_queue.add_ele(ele)
        
    elif ch == "2":
        my_queue.rem_ele()
    
    elif ch == "3":
        my_queue.show_ele()
        
    elif ch == "4":
        print("Exit The Queue")
        break
    
    else:
        print("Invailed choice Enter (1-4) only..")
             