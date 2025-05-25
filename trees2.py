text =str(input("enter your name: "))

revText = text[::-1]
text = revText

print("reverse of given string is: ")
print(text)

tree1 = float(input("Enter the sum of tree1: "))

tree2 = float(input("Enter the sum of tree2: "))

tree3 = float(input("Enter the sum of tree3: "))

tree4 = float(input("Enter the sum of tree4: "))

tree5 = float(input("Enter the sum of tree5: "))

sum = tree1+tree2+tree3+tree4+tree5
print("the sum of all the trees are: ", sum)

average = sum/5
print("the average of all tree is: ", average)