numberlargest = int(input("Enter largest number: "))
numberlowest = int(input("Enter lowest number: "))

while(numberlowest):
    numberstore = numberlowest
    numberlowest = numberlargest % numberlowest
    numberlargest = numberstore

print("HCF is: ", numberlargest)