## Day 7: 30 Days of Python

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# 1
len(it_companies)

# 2
it_companies.add("Twitter")

# 3
new_companies = ("Apple", "Samsung")
it_companies.update(new_companies)

# 4
it_companies.remove("Twitter")

# 5 
"""
If you try to remove something from a list but that item
is not in the list to begin with, then it will raise errors. 
On the contrary, using the discard method will not raise about any errors,
even if the item you're trying to discard is not in the list.
"""

# Exercises: Level 2

# 1
joined = A.union(B)
print(joined)

# 2
print(A.intersection(B))

# 3
print(A.issubset(B)) 

# 4
print(A.isdisjoint(B))

# 5
A.update(B)
print(A)
B.update(A)
print(B)

# 6
A.symmetric_difference(B)

# 7
del A, B

# Exercises: Level 3

# 1
set = set(age)
list = list(age)
print(len(list) > len(set))

# 2
"""
string - series of characters
list - ordered/modifiable collection that allows duplicates
tuple - ordered/unmodifiable collection that allows duplicates
set - unordered/un-indexed/unmodifiable collection that disables duplicates
"""

# 3
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split(" ")
unique_words = set(words)
print(len(unique_words))