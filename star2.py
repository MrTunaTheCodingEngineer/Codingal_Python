print("The half pyramud of stars(*)")
n = int(input("Enter how mant rows you want to have: "))

for i in range(n):

    for j in range(i + 1):

        print("* ", end="")
    print()