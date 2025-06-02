import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(400,500)
polygon = turtle.Turtle()

num_sides = 23
side_length = 50
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()
