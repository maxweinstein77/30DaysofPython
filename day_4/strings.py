## Day 4: 30 Days of Python Programming

# Exercises

# 1
first = "Thirty"
second = "Days"
third = "Of"
fourth = "Python"
space = " "
result = first + space + second + space + third + space + fourth 

# 2
a = "Coding"
b = "For"
c = "All"
space = " "
result = a + space + b + space + c

# 3
company = result 

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
no_first_word = company[7:]
print(no_first_word)

# 10
sub_string = "Coding"
print(company.index(sub_string))
print(company.find("Coding"))

# 11
new_company = company.replace("Coding", "Python")
print(new_company)

# 12
latest_company = new_company.replace("All", "Everyone")
print(latest_company)

# 13
print(company.split(" "))

# 14
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))

# 15
print(company[0]) # C

# 16
sub_string = "l"
print(company.rindex(sub_string)) # 12

# 17
print(company[10]) # space (nothing)

# 18
company = "Python For Everyone"
words = latest_company.split()
first_letter = words[0][0]
second_letter = words[1][0]
third_letter = words[2][0]
acronym = first_letter + second_letter + third_letter
print(acronym)

# 19
company = "Coding For All"
words = company.split()
first_letter = words[0][0]
second_letter = words[1][0]
third_letter = words[2][0]
acronym = first_letter + second_letter + third_letter
print(acronym)

# 20
company = "Coding For All"
print(company.index("C"))

# 21
company = "Coding For All"
print(company.index("F"))

# 22
company = "Coding For All People"
print(company.rfind("l"))

# 23
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))

# 24
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.rindex("because"))

# 25
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence[31:54])

# 26
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))

# 27
sentence = "You cannot end a sentence with because because because is a conjunction"
new_sentence = sentence[:31] + sentence[55:]
print(new_sentence)

# 28
phrase = "Coding For All"
sub_string = "Coding"
print(phrase.startswith(sub_string))

# 29
phrase = "Coding For All"
sub_string = "Coding"
print(phrase.endswith(sub_string))

# 30
phrase = " Coding For All "
print(phrase[1:15])

# 31
variable_one = "30DaysOfPython"
print(variable_one.isidentifier()) # False
variable_two = "thirty_days_of_python"
print(variable_two.isidentifier()) # True 

# 32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(libraries)
print(result)

# 33
print("I am enjoying this challenge. \nI just wonder what is next.")

# 34
print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")

# 35
radius = 10
area = 3.14 * radius ** 2
print("radius = {}".format(radius))
print("area = 3.14 * radius ** 2")
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

# 36
a, b = 8, 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))