try:   
    number = int(input("Enter the number of your age: "))

    if number%2 ==0:
        print("Your Age is an Even number")

    else:
        print("Your Age is an odd Number")

except ValueError:
    print("Please Enter your Age in Numbers instead of your Age in Words ")


