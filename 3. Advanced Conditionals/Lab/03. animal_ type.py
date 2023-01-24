animal_name = input()

is_reptile = animal_name == "crocodile" or animal_name == "tortoise" or animal_name == "snake"
if animal_name == "dog":
    print ('mammal')
elif is_reptile:
    print("reptile")
else:
    print("unknown")
