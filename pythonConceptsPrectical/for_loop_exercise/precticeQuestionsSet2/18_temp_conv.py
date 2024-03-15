# 18. **Temperature Converter:**
#     Create a program that converts temperatures between Celsius and Fahrenheit.

num_conversions = int(input("Enter the number of temperature conversions: "))

ask = input("What do you want to check c (Celsius) or f (Fahrenheit) : ")

for i in range(num_conversions):
    if ask.lower() == "c": 
        celsius_temperature = float(input("Enter temperature in Celsius: "))
        fahrenheit_temperature = (celsius_temperature * 9/5) + 32
        print(f"{celsius_temperature:.2f} Celsius is equal to {fahrenheit_temperature:.2f} Fahrenheit\n")
    elif ask.lower() == "f":   
        fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))
        celsius_temperature = (fahrenheit_temperature - 32) * 5/9
        print(f"{fahrenheit_temperature:.2f} Fahrenheit is equal to {celsius_temperature:.2f} Celsius\n")
print("Temperature conversion program complete.")
