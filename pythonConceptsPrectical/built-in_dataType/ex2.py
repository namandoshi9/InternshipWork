import random

def generate_random_number():
    random_number = random.randint(1,100)
    return random_number

if __name__ == "__main__":
    random_number = generate_random_number()

    print("Randome Number : ",random_number)