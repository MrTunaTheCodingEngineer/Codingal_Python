import math

class Circle:

    def __init__(self,radius):
        
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        self.radius=radius

    def area(self):

        return math.pi * self.radius **2
    

    def perimeter(self):

        return 2 * math.pi * self.radius 
    

my_circle = Circle(5)

print(f"The radius of the circle is: {my_circle.radius}")
print(f"Area of the circle: {my_circle.area():.2f}")
print(f"Perimeter of the circle: {my_circle.perimeter():.2f}")

print("\n" + "="*30 + "\n")

circle2 = Circle(12.5)

print(f"The radius of the second circle is: {circle2.radius}")
print(f"Area of the second circle: {circle2.area():.2f}")
print(f"Perimeter of the second circle: {circle2.perimeter():.2f}")