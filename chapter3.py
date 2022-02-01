#4-1 Pizzas
pizzas = ["Pepperoni", "Meatball", "Meat Feast"]
for pizza in pizzas:
    print(f"I like {pizza.lower()} pizza")

print("I really like pizza!")

#4-2 Animals
animals = ["Dog", "Cat", "Lion"]
messages = ["is very loyal", "is independent", "is brave"]
x = 0
for animal in animals:
    print(f"A {animal} is {messages[x]}")
    x = x + 1

print("They all have tails")

#4-3 Counting to twenty
for value in range (1, 21):
    print(value)

#4-4 One Million (Commented Out)
#for value in range (1, 1_000_001):
#    print(value)

#4-5 Summing a Million
digits = list(range(1,1_000_001))
print(min(digits))
print(max(digits))
print(sum(digits))

#4-6 Odd Numbers
odd_numbers = list(range(1,20,2))
for odd_number in odd_numbers:
    print(odd_number)

#4-7 Threes
threes = [value*3 for value in range(3,11)]
for a_three in threes:
    print (a_three)


#4-8 Cubes
cubes = []
for value in range (1, 11):
    cube = value ** 3
    cubes.append(cube)
    print(cube)

#4-9 Cube Comprehension
myCubes = [cubeValue**3 for cubeValue in range(1,11)]
for myCube in myCubes:
    print(myCube)

#4-10 Slices
odd_numbers = list(range(1,20,2))
for odd_number in odd_numbers:
    print(odd_number)

print("The first three numbers are:")
for odd_number in odd_numbers[:3]:
    print(odd_number)

#4-11 My Pizzas, Your Pizzas
friend_pizzas = ["Pepperoni", "Meatball", "Meat Feast", "Cheese"]
for pizza in pizzas:
    print(f"I like {pizza.lower()} pizza")

for pizza in friend_pizzas:
    print(f"My friend likes {pizza.lower()} pizza")

print("I really like pizza!")

#4-12 More Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
for food in my_foods:
    print(food)

print("My friends favourite foods are:")
for food in friend_foods:
    print(food)


#4-13 Buffet
simpleFoods = ("Chicken", "Bacon", "Cheese", "Egg", "Bread")
#simpleFoods[0] = "Beef"
simpleFoods = ("Rice", "Ham", "Chicken", "Bacon", "Cheese")
for food in simpleFoods:
    print(food)

#4-14 PEP 8
#I have read this

#4-15 Code Review
#I have looked through some of my code and ensured it matches the specification in instructions
