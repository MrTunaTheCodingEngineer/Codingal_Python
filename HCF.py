numberlargest = int(input("enter largest number: "))
numbersmallest = int(input("enter lowest number: "))

while(numbersmallest):
    numberstore = numbersmallest
    numbersmallest = numberlargest % numbersmallest
    numberlargest = numberstore

print("HCF is: ", numberlargest)