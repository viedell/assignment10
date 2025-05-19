fruit1 = input("Fruit 1: ")
fruit2 = input("Fruit 2: ")
fruit3 = input("Fruit 3: ")
fruit4 = input("Fruit 4: ")
fruit5 = input("Fruit 5: ")

fruits = (fruit1, fruit2, fruit3, fruit4, fruit5)
print("Fruit you have entered: ", fruits)

search = input("Search your fruit: ")
if search in fruits:
    print(search, "is in the tuple")
else:
    print(search, "is not in the tuple")

print("Fruit counts: ")
for fruit in fruits:
    count = fruits.count(fruit)
    print(fruit, "appeared", count, "times.")