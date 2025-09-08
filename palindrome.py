number = int(input("Enter your number: "))

originalnumber = number
reversed_number = 0


while number > 0:
    digit = number % 10
    reversed_number = 10 * reversed_number + digit
    number //= 10

if originalnumber ==  reversed_number:
    print(f"{originalnumber} is a palindrome")
else:
    print(f"{originalnumber} is not a palindrome")
