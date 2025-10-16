class Vehicle:

    def __init__(self, name, max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 160, 15)
print("Vehicle name:", School_bus.name, "max speed: ", School_bus.max_speed, "mileage: ", School_bus.mileage)
