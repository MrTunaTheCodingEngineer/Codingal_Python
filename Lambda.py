numbers = [2,4,6]
numbers2 = [1,3,5]
result = map(lambda x,y: x +y, numbers, numbers2)
print("Addition of two lists")
print(list(result))

num = [6,7,8,9]
def sq(n):
    return n*n
square = list(map(sq, num))
print("square of numbers in list")
print(square)