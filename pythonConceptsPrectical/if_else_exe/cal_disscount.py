#Calculate the discount based on the purchase amount.


amt = float(input("Enter Purchase Amount : "))

if amt <= 1000:
    discount = (10 * amt) / 100
    total = amt - discount
    print(f"Purchase amount is {amt} and Discount is 10% so total is {total}")
elif amt > 1000:
    discount = (20 * amt) / 100
    total = amt - discount
    print(f"Purchase amount is {amt} and Discount is 10% so total is {total}")  
else:
    print("Invalid Input")

