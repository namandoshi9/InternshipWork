#  Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price. 

class ShoppingCart:
    def __init__(self):
        self.stock = {'apple': {'price': 2.5, 'qty': 10},
                      'banana': {'price': 1.0, 'qty': 15},
                      'orange': {'price': 3.0, 'qty': 12},
                      'grapes': {'price': 5.0, 'qty': 8}}
        self.cart = {}

    def display_stock(self):
        print("Available Stock:")
        print("Fruit\tPrice\tQuantity")
        for fruit, details in self.stock.items():
            print(f"{fruit}\t${details['price']}\t{details['qty']}")
        print()

    def add_to_cart(self, fruit, quantity):
        if fruit in self.stock and quantity <= self.stock[fruit]['qty']:
            if fruit in self.cart:
                self.cart[fruit]['qty'] += quantity
            else:
                self.cart[fruit] = {'price': self.stock[fruit]['price'], 'qty': quantity}
            self.stock[fruit]['qty'] -= quantity
            print(f"{quantity} {fruit}(s) added to the cart.")
        else:
            print("Invalid selection or insufficient quantity.")

    def place_order(self):
        if not self.cart:
            print("Your cart is empty. Add items before placing an order.")
            return

        total_price = sum(item['price'] * item['qty'] for item in self.cart.values())
        print("\nOrder Summary:")
        for fruit, details in self.cart.items():
            print(f"{fruit}\t{details['qty']} x ${details['price']} = ${details['qty'] * details['price']:.2f}")
        print(f"Total Price: ${total_price:.2f}")

        confirm = input("\nDo you want to place the order? (y/n): ").lower()
        if confirm == 'y':
            for fruit, details in self.cart.items():
                self.stock[fruit]['qty'] -= details['qty']
            self.cart.clear()
            print("Order placed successfully!")
        else:
            print("Order canceled.")

    def run(self):
        while True:
            print("\n-------------Menu:------------")
            print("1. Display Available Stock")
            print("2. Add to Cart")
            print("3. Place Order")
            print("4. Exit")

            choice = input("\nEnter your choice (1-4): ")

            if choice == '1':
                self.display_stock()
                want_to_purchase = input("Do you want to purchase anything? (y/n): ").lower()
                if want_to_purchase == 'y':
                    fruit = input("Enter the fruit name: ").lower()
                    quantity = int(input("Enter the quantity: "))
                    self.add_to_cart(fruit, quantity)
                    print("\nYour item add to cart successfully..")
                    print("----Now Available Stock is----")
                    self.display_stock()
            elif choice == '2':
                fruit = input("Enter the fruit name: ")
                quantity = int(input("Enter the quantity: "))
                self.add_to_cart(fruit, quantity)
            elif choice == '3':
                self.place_order()
            elif choice == '4':
                print("Exiting the program. Thank you!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    shopping_cart = ShoppingCart()
    shopping_cart.run()

