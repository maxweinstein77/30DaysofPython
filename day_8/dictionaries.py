### Day 8

# 1
dog = {}

# 2
dog["name"] = "Caleb"
dog["color"] = "Yellow"
dog["breed"] = "Golden Retriever"
dog["legs"] = 4
dog["age"] = 8
print(dog)

# 3
student = {}
student["first_name"] = "James"
student["last_name"] = "Smith"
student["gender"] = "Male"
student["age"] = 20
student["marital_status"] = "Single"
student["skills"] = ["Python", "SQL", "JavaScript", "Springboot"]
student["country"] = "USA"
student["city"] = "Austin"
student["address"] = "1 Willow Creek Lane"
print(student)

# 4
print(len(student))

# 5
print(student["skills"])
print(type(student["skills"]))

# 6
student["skills"].append("C++")
student["skills"].append("CSS")
print(student)

# 7
print(student.keys())

# 8 
print(student.values())

# 9
print(student.items())

# 10
del student["skills"]

# 11
del dog