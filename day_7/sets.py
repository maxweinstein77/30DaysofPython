### Day 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

## Level 1

# 1
print(len(it_companies))

# 2
it_companies.add("Twitter")

# 3
it_companies.update(["Aviato", "Meta", "Instagram"])

# 4
it_companies.remove("Aviato")

# 5
"""
If you are trying to remove an item that does not 
exist in the list, you will receive an error. On the
other hand, discard will not present an error, even
if you attempt to discard something that does not exist
in the list."""

## Level 2

# 1
A.update(B)
print(A)

# 2
A.intersection(B)

# 3
A.issubset(B)

# 4
A.isdisjoint(B)

# 5
A.update(B)
B.update(A)

# 6
A.symmetric_difference(B)

# 7
del A 
del B

## Level 3

# 1
print(len(age)) # List bigger - permits duplicates
print(len(set(age))) 

# 2
# String - any data type written as text (data types in text form)
# List - collection which is ordered, changeable, and permits duplicates
# Tuple - ordered, immutable, and permits duplicates
# Set - unordered, immutable, and doesn't permit duplicates

# 3
sentence = "I am teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print(unique_words)
