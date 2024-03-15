# Flight Booking System:

# Design a class hierarchy for a flight booking system. 
# Consider classes for flights, passengers, and bookings. 
# Include methods for booking flights, managing reservations, and checking flight availability.

class Flight:
    def __init__(self, number, source, destination):
        self.number = number
        self.source = source
        self.destination = destination
        self.capacity = 100
        self.booked = []
    
    def book_flight(self, passenger):
        if len(self.booked) < self.capacity:
            self.booked.append(passenger)
            return True
        else:
            return False
            
    def check_availability(self):
        return len(self.booked)
        

class Passenger:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Booking:
    def make_reservation(flight, passenger):
        if flight.book_flight(passenger):
            return f"Booking successful! {passenger.name} is now booked on flight {flight.number}"
        else:
            return "Flight is fully booked!"
            # Test the code with sample data

f1 = Flight("123", "London", "Paris")
p1 = Passenger("John Doe", "JD007")
print(Booking.make_reservation(f1, p1))   # Should print "Booking successful! John Doe is now booked on flight 123"