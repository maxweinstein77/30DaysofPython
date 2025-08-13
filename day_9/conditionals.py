## Day 9: 30 Days of Python

# Exercises: Level 1

# 1
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive. ")

# 2
my_age = 18
your_age = int(input("Enter your age: "))

if my_age != your_age:
    if my_age < your_age:
        print("You are", your_age - my_age, "years older than me.")
    else:
        print("You are", my_age - your_age, "years younger than me.")
else:
    print("We are the same age.")

# 3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is smaller than", b)
else:
    print(a, "is equal to", b)

# Exercises: Level 2

# 1
grade = int(input("Enter score: "))

if 80 <= grade <= 100:
    print("Your grade is an A.")
elif 70 <= grade <= 89:
    print("Your grade is a B.")
elif 60 <= grade <= 69:
    print("Your grade is a C.")
elif 50 <= grade <= 59:
    print("Your grade is a D.")
else:
    print("Your grade is an F.")

# 2
month = input("Enter the month: ").lower()
autumn = ["september", "october", "november"]
winter = ["december", "january", "february"]
spring = ["march", "april", "may"]
summer = ["june", "july", "august"]

if month in autumn:
    print("It's autumn.")
elif month in winter:
    print("It's winter.")
elif month in spring:
    print("It's spring.")
elif month in summer:
    print("It's summer.")

# 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter fruit: ").lower()

if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print("That fruit already exists in the list.")

# Exercises: Level 3

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
    mid = len(skills) // 2
    if len(skills) % 2 == 0:
        print(skills[mid - 1: mid + 1])
    else:
        print(skills[mid])

if "skills" in person:
    if "Python" in person["skills"]:
        print("This person knows Python.")

front_end = ["JavaScript", "React"]
back_end = ["Node", "Python", "MongoDB"]

front_end = ["JavaScript", "React"]
back_end = ["Node", "Python", "MongoDB"]

if "skills" in person:
    if "JavaScript" in person["skills"] and "React" in person["skills"] \
       and not ("Node" in person["skills"] or "Python" in person["skills"] or "MongoDB" in person["skills"]):
        print("He is a front-end developer.")
    elif "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"] \
         and not ("JavaScript" in person["skills"] or "React" in person["skills"]):
        print("He is a back-end developer.")
    elif "JavaScript" in person["skills"] and "React" in person["skills"] \
         and "Node" in person["skills"] and "MongoDB" in person["skills"]:
        print("He is a full-stack developer.")
    else:
        print("Unknown title")

if person["is_married"] == True and person["country"] == "Finland":
    print(person["first_name"] + " " + person["last_name"] + " lives in " + person["country"] + ". He is married.")