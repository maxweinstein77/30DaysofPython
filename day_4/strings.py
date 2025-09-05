### Day 4

# 1
first = "Thirty"
second = "Days"
third = "Of"
fourth = "Python"
space = " "
full = first + space + second + space + third + space + fourth
print(full_course)

# 2
first = "Coding"
second = "For"
third = "All"
space = " "
full = first + space + second + space + third 
print(full)

# 3
company = "Coding For All"

# 4
print(company)

# 5
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9
print(company[0:7])

# 10
print(company.find("Coding"))

# 11
print(company.replace("Coding", "Python"))

# 12
company = "Python For All"
print(company.replace("Everyone", "All"))

# 13
company = "Coding For All"
print(company.split())

# 14
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))

# 15
print(company[0]) # C

# 16
print(company[-1]) # l

# 17
print(company[10]) # Nothing (space)

# 18
python_for_everyone = "PFE"

# 19
coding_for_all = "CFA"

# 20
print(company.index("C"))

# 21
print(company.index("F"))

# 22
print(company.rfind("l"))

# 23
sentence = "You cannot end a sentence with because because because is a conjunction."
print(sentence.index("because"))

# 24
print(sentence.rindex("because"))

# 25
print(sentence[31:54])

# 26
print(sentence.index("because"))

# 27
print(sentence[31:54])

# 28
print(company.startswith("Coding"))

# 29
print(company.endswith("coding"))

# 30
title = " Coding For All  "
print(title.strip())

# 31
name1 = "30DaysofPython"
name2 = "thirty_days_of_python"
print(name1.isidentifier())
print(name2.isidentifier()) # True

# 32
libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("# ".join(libraries))

# 33
print("I am enjoyingi this challenge.\nI just wonder what is next.")

# 34
challenge1 = "Name\tAge\tCountry\tCity"
challenge2 = "Asabeneh\t250\tFinland\tHelsinki"
print(challenge1.expandtabs(10))
print(challenge2.expandtabs(10))

# 35
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

# 36
num_one = 8
num_two = 6
print("{} + {} = {}".format(num_one, num_two, num_one + num_two))
print("{} - {} = {}".format(num_one, num_two, num_one - num_two))
print("{} * {} = {}".format(num_one, num_two, num_one * num_two))
print("{} / {} = {}".format(num_one, num_two, num_one / num_two))
print("{} % {} = {}".format(num_one, num_two, num_one % num_two))
print("{} // {} = {}".format(num_one, num_two, num_one // num_two))
print("{} ** {} = {}".format(num_one, num_two, num_one ** num_two))