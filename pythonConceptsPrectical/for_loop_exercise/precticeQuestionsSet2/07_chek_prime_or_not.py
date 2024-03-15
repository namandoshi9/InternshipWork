# 7. **Prime Number Checker:**
#    write a program that checks if a given number is prime.

n = int(input("Enter you want to check palindrome or not : "))

if n > 1:
    for i in range(2, int(n/2)+1):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(n, "is not a prime number")
    
    
