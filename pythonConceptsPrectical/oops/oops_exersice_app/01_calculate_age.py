from datetime import datetime

class Person:
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = birthdate

    def calculate_age(self):
        today = datetime.now()
        birthdate = datetime.strptime(self.birthdate, "%Y-%m-%d")
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

# Example usage:
if __name__ == "__main__":
    # Create a Person instance
    person_name = input("Enter the person's name: ")
    person_country = input("Enter the person's country: ")
    person_birthdate = input("Enter the person's birthdate (YYYY-MM-DD): ")

    person = Person(person_name, person_country, person_birthdate)

    # Calculate and print the person's age
    age = person.calculate_age()
    print(f"{person.name} from {person.country} is {age} years old.")
