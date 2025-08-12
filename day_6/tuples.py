## Day 6 30 Days of Python Programming

# Exercises: Level 1

# 1
empty_tuple = ()

# 2 
sisters = ("Sara", "Lynne", "Lauren")
brothers = ("Max", "Sam", "David")

# 3
siblings = sisters + brothers
print(siblings)

# 4
print(len(siblings))

# 5
parents = ("John", "Sally")
family_members = siblings + parents 
print(family_members)

# Exercises: Level 2

# 1
siblings = family_members[0:6]
print(siblings)
parents = family_members[6:]
print(parents)

# 2
fruits = ("Apple", "Banana")
vegetables = ("Onion", "Cucumber")
animal_products = ("Eggs", "Meat")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3
food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp)

# 4
middle_items = food_stuff_tp[2:4]
print(middle_items)

# 5
first_items = food_stuff_tp[0:3]
print(first_items)
last_items = food_stuff_tp[-3:]
print(last_items)

# 6 
del food_stuff_tp

# 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)xx