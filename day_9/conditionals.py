### Day 9

## Level 1

# 1
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive.")
else:
    wait = 18 - age
    print(f"You need {wait} more years to learn to drive.")

# 2
my_age = 18
your_age = int(input("Enter your age: "))


if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:   
        print(f"You are {difference} year older than me.")
    else:
        print(f"You are {difference} years older than me.")
elif your_age < my_age:
    difference = my_age - your_age 
    if difference == 1:
        print(f"You are {difference} year younger than me.")
    else:
        print(f"You are {difference} years younger than me.")
elif your_age == my_age:
    print(f"We are the same age.")

# 3
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is less than {b}.")
elif a == b:
    print(f"{a} is equal to {b}.")

## Level 2

# 1
score = float(input("Enter score: "))

if 80 <= score <= 100:
    print("You earned an A.")
elif 70 <= score <= 89:
    print("You earned a B.")
elif 60 <= score <= 69:
    print("You earned a C.")
elif 50 <= score <= 59:
    print("You earned a D.")
elif 0 <= score <= 49:
    print("You earned an F.")

# 2
month = input("Enter month: ")
month = month.capitalize()

autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]

if month in autumn:
    print("It's autumn.")
elif month in winter:
    print("It's winter.")
elif month in spring:
    print("It's spring.")
elif month in summer:
    print("It's summer.")

# 3
fruits = ["banana", "orange", "mango", "lemon"]

fruit = input("Enter fruit: ")
fruit = fruit.lower()

if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print("That fruit already exists in the list.") 

## Level 3

# 1
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if "skills" in person:
    skills = person["skills"]
    n = len(skills)

    if n % 2 == 0:
        mid1, mid2 = n // 2 - 1, n // 2
        print("Middle skills:", [skills[mid1], skills[mid2]])
    else:
        print("Middle skill:", skills[n // 2])

    print("Person knows Python.") if "Python" in skills else print("Person doesn't know Python.")

    skills = set(skills)
    frontend = {"JavaScript", "React"}
    backend = {"Node", "Python", "MongoDB"}
    full_stack = {"React", "Node", "MongoDB"}

    if skills == frontend:
        print("Person is a frontend developer.")
    elif backend.issubset(skills):
        print("Person is a backend developer.")
    elif full_stack.issubset(skills):
        print("Person is a full stack developer.")
    else:
        print("Unknown title.")
else:
    print("Skills key not found.")

if person["is_married"] and person["country"] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")














if "skills" in person:
    skills = person["skills"]
    n = len(skills)

    if n % 2 == 0:
        mid1 = n // 2 - 1
        mid2 = n // 2
        middle = [skills[mid1], skills[mid2]]
        print("Middle skills:", middle)
    else:
        middle = skills[n // 2]
        print("Middle skill:", middle)
    
    print("Person knows Python.") if "Python" in skills else print("Person doesn't know Python.")

    skills = set(skills)
    frontend = {"JavaScript", "React"}
    backend = {"Node", "Python", "MongoDB"}
    full_stack = {"React", "Node", "MongoDB"}

    if skills == frontend:
        print("Person is a frontend developer.")
    elif backend.issubset(skills):
        print("Person is a backend developer.")
    elif full_stack.issubset(skills):
        print("Person is a full stack developer.")
    else:
        print("Unknown title.")
else:
    print("Skills key not found.")

print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.") if person['married'] == True and person['country'] == "Finland" else None