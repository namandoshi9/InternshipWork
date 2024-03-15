'''
1. Display Available Items(Name,price,qty)
2. give order(ask to customer)
3. Order status (pending,ready,complete)
4. Exit

'''
class MenuItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Order:
    def __init__(self):
        self.items = []
        self.status = "Pending"

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price * item.quantity for item in self.items)

    def display_order(self):
        for item in self.items:
            print(f"{item.name} - Quantity: {item.quantity}, Price: Rs.{item.price}")
        print(f"Total Price: ${self.calculate_total()}")
        print(f"Order Status: {self.status}")

class RestaurantApp:
    def __init__(self):
        self.menu = [
            MenuItem("Burger", 5.99, 0),
            MenuItem("Pizza", 8.99, 0),
            MenuItem("Salad", 3.99, 0),
            # Add more menu items as needed
        ]
        self.order = None

    def display_menu(self):
        print("Available Items:")
        print("Name\tPrice\tQuantity")
        for item in self.menu:
            print(f"{item.name}\t${item.price}\t{item.quantity}")

    def take_order(self):
        self.order = Order()
        for item in self.menu:
            quantity = int(input(f"How many {item.name}s would you like to order? "))
            item.quantity = quantity
            if quantity > 0:
                self.order.add_item(item)

    def display_order_status(self):
        if self.order:
            self.order.display_order()
        else:
            print("No order placed yet.")

    def run(self):
        while True:
            print("\n1. Display Available Items\n2. Give Order\n3. Order Status\n4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.display_menu()
            elif choice == '2':
                self.take_order()
            elif choice == '3':
                self.display_order_status()
            elif choice == '4':
                print("Thank you for using the restaurant app. Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    restaurant_app = RestaurantApp()
    restaurant_app.run()
