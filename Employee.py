class Employee():

    def __init__(self):
        print("Created Employee")

    def __del__(self):
        print("Emplyee Destructed")

def Create_obj():
    print("Making object...")
    obj = Employee()
    print("Function end..")
    return obj

print("Calling Create_obj Function...")
obj = Create_obj
print("Program end.")

      