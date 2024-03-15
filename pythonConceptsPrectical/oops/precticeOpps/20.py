import random

class Bank:
    def __init__(self):
        self.coustomers = []
        
    def generate_acc_no(self):
        return random.randint(10000,9999)
    
    def add_customer(self,name,age,dob,mobile,o_b,a_n):
        if not self._is_aadhar_unique(a_n):
            print(f"Error: customer with aadhar number {a_n} already exits.")
            return
        
        acc_no = self.generate_acc_no()
        customer = {
            'acc_no' : acc_no,
            'name' : name,
            'age' : age,
            'dob' : dob,
            'mobile' : mobile,
            'o_b' : o_b,
            'a_n' : a_n,
            'balance': o_b,
            'transactions' : []
        }
        self.coustomers.append(customer)
        print(f"customer{name}with account number{acc_no}added successfully")
        
        
    def show_balance(self,acc_no):
        customer = self._get_customer_by_acc_no(acc_no)
        if customer:
            print(f"Balance of the account is Rs.{customer['balance']}")
        else:
            print(f"Account number {acc_no} not found.")
            
    def deposite_money(self,acc_no,amt):
        customer = self._get_customer_by_acc_no(acc_no)
        if customer:
            customer['balance'] += amt
            customer['transction'].append(f"Deposited Rs.{amt}")
            print(f"{amt} deposited sucessfully")
        else:
            print(f"Account number {acc_no} not found ")
            
    def withdraw_money(self,acc_no,amt):
        customer = self._get_customer_by_acc_no(acc_no)
        if customer:
            if amt <= customer['balance']:
                pass