height = float(input("Enter you height in cm: "))
weight = float(input("Enter you weight in kg: "))

BMI = weight / (height/100)**2

print("Your BMI is: ", BMI)

if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are Healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are obese")
else:
    print("You are extremly obese")