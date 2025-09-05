### Day 6

## Level 1

# 1
tpl = ()

# 2
brothers = ("Jacob", "Josh")
sisters = ("Rachel", "Sarah")

# 3
siblings = brothers + sisters

# 4
print(len(siblings))

# 5
lst = list(siblings)
lst.append("Mike")
lst.append("Lynne")
family_members = tuple(lst)
print(family_members)

## Level 2

# 1
*siblings, father, mother = family_members
parents = (father, mother)

print("Siblings:", tuple(siblings))
print("Parents:", parents)

# 2
fruits = ("apple", "banana", "orange")
vegetables = ("cucumber", "tomato", "beets ")
animal_products = ("chicken", "beef", "eggs")
food_stuff_tp = fruits + vegetables + animal_products 

# 3
food_lst = list(food_stuff_tp)

# 4
n = len(food_lst)

if n % 2 == 0:
    mid1, mid2 = n // 2 - 1, n // 2
    mid = food_lst[mid1:mid2+1]
else:
    mid = food_lst[n // 2]

print(mid)

# 5
print(food_lst[:3])
print(food_lst[-3:])

# 6
del food_lst

# 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)