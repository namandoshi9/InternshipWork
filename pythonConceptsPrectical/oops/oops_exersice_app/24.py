'''
1.get destination n show flight details
2.book a ticket to that place
3.cancel the booking
4.exit
passanger capacity 10 in one plane and show all passanger name using flight number
'''

class Flight:
    def __init__(self,destnation,flight_no):
        self.destination=destnation
        self.flight_number = flight_no
        self.status='available'
    
    def display_details(self):
        print("Destination : ",self.destination)
        print("Flight Number : ",self.flight_number)
        print("Status : ",self.status)
        
    def book_ticket(self):
        if self.status=='available':
            print("Ticket Booked Successfully")
            self.status='booked'
        else:
            print("Sorry! The flight is not available.")
            
    def cancel_booking(self):
        if self.status=='booked':
            self.status='available'
            print("Booking Cancelled Successfully")
        else:
            print("No Ticket to be canceled.")

# Create objects for different flights
f1=Flight('Delhi','FGH789')
f2=Flight('Mumbai','XYZ654')

choice=input("\nEnter your choice:\n1.Get Destination and Show Flight Details\n2.Book a Ticket \n3.Cancel Booking\n4. EXit")

if choice == "1":
    destnation = input("Enter Destination : ")
    f1.display_details()
elif choice == "2":
    num = int(input("Enter Flight number :"))
    if num == 1:
        f1.book_ticket()
    elif num == 2:
        f2.book_ticket()
else:
    num = int(input("Enter Flight number :"))
    if num == 1:
        f1.cancel_booking()
    elif num == 2:
        f2.cancel_booking()
