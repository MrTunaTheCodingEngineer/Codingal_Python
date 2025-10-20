class MyClass:

    __privVar = 27

    def __privMeth(self):
        print("im inside class myClass")

    def hello(self):
        print("Private Variable Value: ",MyClass.__privVar)

foo = MyClass()
foo.hello()
foo.__privMeth