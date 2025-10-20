class Vehicle:

    def __init__(self, name, seats, price):
        self.name = name
        self.seats = seats
        self.price = price

class Bus(Vehicle):
    pass

City_bus = Bus("Audi Bus", 50, 20 )
print("Vehicle name: ",City_bus.name,"Vehicle seats: ", City_bus.seats,"Vehicle price per seats: ",City_bus.price)