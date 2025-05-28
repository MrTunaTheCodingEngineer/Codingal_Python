word = input("Enter any name you want: ")
lett =input("Enter any letter in the alphabet: ")

i = 0
count = 0
while(i < len(word)):
    if (word[i] == lett):
        count = count + 1
    i = i+1
print(count)