test_dict = {'Python': 6, 'is': 6, 'a': 6, 'coding': 6, 'app': 6}

print("The Original dictonary: " + str(test_dict))

K = 6

res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1


print("Frequency of K is: " +str(res))

  

