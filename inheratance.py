class dad:

    def __init__(self, eyes, aggresive, color):
        self.eyes = eyes
        self.aggresive = aggresive
        self.color = color

    def display(self):
        print("Your eye color is: ", self.eyes)
        print("You are aggresive ", self.aggresive)
        print("Your color is: ", self.color)

    
class son(dad):

    def __init__(self, name, age, eyes, aggresive, color):
        self.name = name
        self.age = age

        super().__init__(eyes, aggresive, color)

animal1 = son("Lion" ,9, "Red", True, "brown")
animal2 = son("Cheetah", 11, "Green", False, "white")
animal3 = son("Eagle", 13, "Brown", False, "Black")


animal1.display()
    