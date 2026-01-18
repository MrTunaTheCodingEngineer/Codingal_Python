from abc import ABC, abstractmethod

class Abclass(ABC):


    def print(self,x):
        print("Passed Value: ",x)

    def task(self):
        print("We are inside Abstract class")

class test_class(Abclass):
    def task(self):
        print("We are in test_class class")

test_object = test_class()
test_object.task()
test_object.print("100")