class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # method to add a passenger to the flight
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name) # add the name to the list of passengers
        return True

    # method to return the number of open seats that are available
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3) #means that the flight has a capacity of 3 passengers

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    success = flight.add_passenger(person) # add the person to the flight
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")

# alternatively:
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")



# output will be:
# Added Harry to flight successfully.
# Added Ron to flight successfully.
# Added Hermione to flight successfully.
# No available seats for Ginny.
