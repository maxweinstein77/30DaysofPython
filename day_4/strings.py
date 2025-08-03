## Day 4: 30 Days of Python Programming

# Exercises

first = "Thirty"
second = "Days"
third = "Of"
fourth = "Python"
space = " "
result = first + space + second + space + third + space + fourth 

a = "Coding"
b = "For"
c = "All"
space = " "
result = a + space + b + space + c

company = result 
print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

no_first_word = company[7:]
print(no_first_word)

sub_string = "Coding"
print(company.index(sub_string))
print(company.find("Coding"))

new_company = company.replace("Coding", "Python")
print(new_company)

latest_company = new_company.replace("All", "Everyone")
print(latest_company)

print(company.split(" "))

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))

print(company[0]) # C

sub_string = "l"
print(company.rindex(sub_string)) # 12

print(company[10]) # space (nothing)

company = "Python For Everyone"
words = latest_company.split()
first_letter = words[0][0]
second_letter = words[1][0]
third_letter = words[2][0]
acronym = first_letter + second_letter + third_letter
print(acronym)

company = "Coding For All"
words = company.split()
first_letter = words[0][0]
second_letter = words[1][0]
third_letter = words[2][0]
acronym = first_letter + second_letter + third_letter
print(acronym)

company = "Coding For All"
print(company.index("C"))

company = "Coding For All"
print(company.index("F"))


company = "Coding For All People"
print(company.rfind("l"))

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.rindex("because"))

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence[31:54])

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))

sentence = "You cannot end a sentence with because because because is a conjunction"
new_sentence = sentence[:31] + sentence[55:]
print(new_sentence)

phrase = "Coding For All"
sub_string = "Coding"
print(phrase.startswith(sub_string))

phrase = "Coding For All"
sub_string = "Coding"
print(phrase.endswith(sub_string))

phrase = " Coding For All "
print(phrase[1:15])

variable_one = "30DaysOfPython"
print(variable_one.isidentifier()) # False
variable_two = "thirty_days_of_python"
print(variable_two.isidentifier()) # True 

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(libraries)
print(result)

print("I am enjoying this challenge. \nI just wonder what is next.")

print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print("radius = {}".format(radius))
print("area = 3.14 * radius ** 2")
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

a, b = 8, 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))