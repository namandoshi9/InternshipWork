#FILO - First In Last Out
class Stack:
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
            print(f"Stack is full {self.li}")

    def rem_ele(self):
        if not self.is_empty():
            return self.li.pop()
        else:
            print(f"Stack is empty {self.li}")
            
    def show_ele(self):
        print("Stack:", self.li)
            
my_Stack = Stack(max_length=5)

while True:
    print("------Choice One------")
    print("1). Add Stack")
    print("2). Remove Stack")
    print("3). Show Stack")
    print("4). Exit")
    print("-"*10)
    
    ch = input("Enter your choice : ")
    
    if ch == "1":
        ele = input("Enter The element : ")
        my_Stack.add_ele(ele)
        
    elif ch == "2":
        my_Stack.rem_ele()
    
    elif ch == "3":
        my_Stack.show_ele()
        
    elif ch == "4":
        print("Exit The Stack")
        break
    
    else:
        print("Invailed choice Enter (1-4) only..")
             