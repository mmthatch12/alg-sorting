animals = ['duck', 'jackal', 'hippo', 'aardvark', 'cat', 'flamingo', 'iguana', 'giraffe', 'elephant', 'lion']

# O(1)

# Return the name of all animals
def getAnimals():
    return animals

# O(n)

# Returns the number of animals
def countAnimals():
    num_animals = 0
    for animal in animals:
        num_animals += 1
    return num_animals
# if there was only on animal in animals then we would only need to run this one time, if there were 10,000, would need to run it that many times
# it is completely linear
# o(2n) is the same as O(n) because all we care about is the shape

# returns each animal with all letters lowercase
def getLowercaseAnimals():
    lowercase_animals = animals
    animal_index = 0
    for animal in animals:
        lowercase_animals[animal_index] = lowercase_animals[animal_index].lower()
        animal_index += 1
    return lowercase_animals

# given the name of an animal, return true if that animal is in the list, false otherwise
def hasAnimal(animal_name):
    for animal in animals:
        if animal == animal_name:
            return True
    return False

# O(n^2)

# right now you would do 10animals * 10animals = 100animals, if we added 1 animal it would be 11*11=121. O(n^2) increases super fast
def printAnimalPairs():
    for animal1 in animals:
        for animal2 in animals:
            print(f"{animal1} - {animal2}")

# O(n^3)

# right now you would do 10animals * 10animals = 100animals, if we added 1 animal it would be 11*11=121. O(n^2) increases super fast
def printAnimalPairs():
    for animal1 in animals:
        for animal2 in animals:
            for animal3 in animals:
                print(f"{animal1} - {animal2} {animal3}")
