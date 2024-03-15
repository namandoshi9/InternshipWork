#  Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
# 1) add customer -> name,age,dob,mobile,opening_bal and generate randome account number
# 2) show balance, 3) money deposite, 4) money widthrwal, 5)show transcation, 
# 6) AadharNumber if aadhar number alreday exit print massge Customer alreday exist
# 7) Exit


import random

class Bank:
    def __init__(self):
        self.customers = []

    def generate_acc_no(self):
        return random.randint(10000, 99999)

    def add_customer(self, name, age, dob, mobile, opening_balance, aadhar_number):
        if not self._is_aadhar_unique(aadhar_number):
            print(f"Error: Customer with Aadhar number {aadhar_number} already exists.")
            return

        acc_no = self.generate_acc_no()
        customer = {
            'acc_no': acc_no,
            'name': name,
            'age': age,
            'dob': dob,
            'mobile': mobile,
            'opening_balance': opening_balance,
            'aadhar_number': aadhar_number,
            'balance': opening_balance,
            'transactions': []
        }
        self.customers.append(customer)
        print(f"Customer {name} with account number {acc_no} added successfully!")

    def show_balance(self, acc_no):
        customer = self._get_customer_by_acc_no(acc_no)
        if customer:
            print(f"Balance for account number {acc_no}: Rs.{customer['balance']}")
        else:
            print(f"Account number {acc_no} not found.")

    def deposit_money(self, acc_no, amount):
        customer = self._get_customer_by_acc_no(acc_no)
        if customer:
            customer['balance'] += amount
            customer['transactions'].append(f"Deposited Rs.{amount}")
            print(f"Rs.{amount} deposited successfully for account number {acc_no}.")
        else:
            print(f"Account number {acc_no} not found.")

    def withdraw_money(self, acc_no, amount):
        customer = self._get_customer_by_acc_no(acc_no)
        if customer:
            if amount <= customer['balance']:
                customer['balance'] -= amount
                customer['transactions'].append(f"Withdrew Rs.{amount}")
                print(f"Rs.{amount} withdrawn successfully for account number {acc_no}.")
            else:
                print(f"Insufficient funds for account number {acc_no}.")
        else:
            print(f"Account number {acc_no} not found.")

    def show_transactions(self, acc_no):
        customer = self._get_customer_by_acc_no(acc_no)
        if customer:
            print(f"Transactions for account number {acc_no}:")
            for transaction in customer['transactions']:
                print(transaction)
        else:
            print(f"Account number {acc_no} not found.")

    def _get_customer_by_acc_no(self, acc_no):
        for customer in self.customers:
            if customer['acc_no'] == acc_no:
                return customer
        return None

    def _is_aadhar_unique(self, aadhar_number):
        for customer in self.customers:
            if customer['aadhar_number'] == aadhar_number:
                return False
        return True


if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\nBank Menu:")
        print("1. Add Customer")
        print("2. Show Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Show Transactions")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter customer name: ")
            age = int(input("Enter customer age: "))
            dob = input("Enter customer date of birth (YYYY-MM-DD): ")
            mobile = input("Enter customer mobile number: ")
            opening_balance = float(input("Enter opening balance: "))
            aadhar_number = input("Enter customer Aadhar number: ")
            bank.add_customer(name, age, dob, mobile, opening_balance, aadhar_number)

        elif choice == '2':
            acc_no = int(input("Enter account number: "))
            bank.show_balance(acc_no)

        elif choice == '3':
            acc_no = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            bank.deposit_money(acc_no, amount)

        elif choice == '4':
            acc_no = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw_money(acc_no, amount)

        elif choice == '5':
            acc_no = int(input("Enter account number: "))
            bank.show_transactions(acc_no)

        elif choice == '6':
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

