import array as arr

array_num = arr.array('i',[4 ,6 ,3 ,7 ,4 ,8 ,2 ,4 ,5 ,4])
print("Original array:"+str(array_num))

print("Amout of thimes the number 4 has been included in the array "+str(array_num.count(4)))


array_num.reverse()
print("The rreversed order of the array:")
print(str(array_num))
