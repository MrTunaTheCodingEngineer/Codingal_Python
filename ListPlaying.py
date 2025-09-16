L = [2, 4, 5, 18, 248, 17 , 36, 67, 21]
print("Original list: ", L)

count = 0

for i in L:
    count += i

avg = count/len(L)

print("sum: ", count)
print("average: ", avg)

L.sort

print("Largest number is: ",L[-1])

print("smallest number is: ", L[0])