s1 = {6,2,4}
s2 = {'t', 's', 'r'}
s3 = list(zip(s1, s2))
print(s3,"\n")

listx = [50,60,70,80]
listy = [500,600,700,800]

for x,y in zip(listx,listy[::-1]):
    print(x,y)

    cars = ('BMW', 'Audi', 'Mercedes')
    prices = [2300, 4500, 3400]

new_dict = {cars: prices for cars,
                                 prices in zip(cars,prices)}

print('\n{}'.format(new_dict))