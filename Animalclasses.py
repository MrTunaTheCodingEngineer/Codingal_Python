from abc import ABC, abstractmethod

class Animal(ABC):

    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("I can run and walk")

class Fish(Animal):

    def move(self):
        print("I can swim")

class Bird(Animal):

    def move(self):
        print("I can fly")

class Snake(Animal):

    def move(self):
        print("I can Slither")


R = Human()
R.move()

K = Fish()
K.move()

R = Bird()
R.move()

K = Snake()
K.move()








