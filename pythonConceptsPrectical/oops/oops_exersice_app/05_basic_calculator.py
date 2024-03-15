class BasicCalculator:
    def __init__(self):
        pass
    
    def add(self,a,b):
        return a + b
    
    def sub(self,a,b):
        return a - b
    
    def mul(self,a,b):
        return a * b
    
    def divi(self,a,b):
        return a / b
    
while True:
    calc = BasicCalculator()
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Division")
    
    print("\nChoose an option by typing the number in front of it:\n")
    operation_choice = input("Option: ")
    
    if operation_choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = calc.add(num1,num2)
        print("\nThe sum is: {}".format(result))
    
    elif operation_choice == "2":
        try:
            num1 = int(input("Enter the number you want to subtract from :"))
            num2 = float(input("Enter the number you want to subtract: "))
            result = calc.sub(num1,num2)
            print("\nThe result is: {}".format(result))
        except:
            print("\nInvalid Input! Please enter integer for 'num1' and decimal/integer for'num2'.\n")
            
    elif operation_choice == "3":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = calc.mul(num1,num2)
        print("\nThe product is: {}".format(result))
        
    elif operation_choice == "4":
        num1 = float(input("Enter the dividend: "))
        num2 = float(input("Enter the divisor: "))
        if num2==0:
            print("\nError! Division by zero is not allowed.\n")
        else:
            result = calc.divi(num1,num2)
            print("\nThe quotient is: {}".format(result))
            
    else:
        print("\nWrong choice!\n")
    
    
        