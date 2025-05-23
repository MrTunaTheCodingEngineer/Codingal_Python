medical_cause = bool(input("did you have a medical cause: "))
atten = int(input("Enter the attendance of the student: "))

if medical_cause == True:
    print("The student is allowed")
else:
    if atten >= 75:
        print("Allowed")
    else:
        print("Not Allowed")
