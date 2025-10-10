class dog:

    animal = "Dog"

    def __init__(self, name, height):
        self.name = name
        self.height = height

german_shephard = dog('german shephard', '60-65cm')
greyhound = dog('Greyhound', "71cm")

print(german_shephard.animal)
print(german_shephard.name ,german_shephard.height)
print(greyhound.name, greyhound.height)




