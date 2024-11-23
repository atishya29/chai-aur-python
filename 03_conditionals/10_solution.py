species = input("You have dog or cat:")
age = int(input("Enter Your Pet age:"))

if (species == "dog" and age < 2):
    food = "Puppy Food"
elif (species == "dog" and age >= 2):
    food = "Senior dog food"
elif (species == "cat" and age <= 5):
    food = "Kitten Food"
elif (species == "cat" and age > 5):
    food = "Senior cat food"
else:
    print("Enter a valid species or age")
    exit()

print("Recommended food type is:", food)