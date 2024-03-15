# Create a program that prints all prime numbers between 10 and 50 using a for loop.

# num = int(input("Enter Number you want to check prime or not : "))

#Simple chek prime or not
# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            break
#    else:
#        print(num,"is a prime number")
    
# else:
#    print(num,"is not a prime number")



#check between 10 to 50 method 1

# for number in range(10, 51):
#     if number > 1:
#         is_prime = True
#         for i in range(2, int(number**0.5) + 1):
#             if number % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(number)

    
#check prime or not between 10 to 50
for number in range(10, 51):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            break
    else:
        print(number)
