def print_factor(number):
    print("Factors of", number ,"are: ")
    for i in range(1, number +1):
        if number % i == 0:
            print(i)

number  = int(input("Enter yout number to find out its factors: "))

print_factor(number)

