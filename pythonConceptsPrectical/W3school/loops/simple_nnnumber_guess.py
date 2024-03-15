#Implement a simple number guessing game using a `while` loop.


num_guesses = int(input("Enter the maximum number of guesses: "))
secret_number = input("Enter your secret number (0 to quit): ")
print("\nWelcome to the Number Guessing Game!")

if secret_number == '0':
    print('Goodbye!')
else:
    i = 1
    while i <= num_guesses:
        guess = input("Take a guess: ")
        if guess == secret_number:
            print('\nCongratulations, you got it right!')
            break
        elif int(guess) > int(secret_number):
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
        i += 1
        if i > num_guesses:
            print("\nSorry, you've used all your guesses. The correct answer was{}.".format(secret_number))

                       