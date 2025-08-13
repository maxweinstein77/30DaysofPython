## Day 8: 30 Days of Python

# 1
dog = {}

# 2
dog = {
    "name":"Lilah",
    "color":"Black",
    "breed":"Chihuahua",
    "legs":"four",
    "age" : "6"
}

# 3
student = {
    "first_name":"John",
    "last_name":"Doe",
    "gender":"Male",
    "age":"16",
    "marital_status":"Single",
    "skills":["Python", "JS", "SQL"],
    "country":"USA",
    "city":"Miami",
    "address":{
        "street":"1130 Ocean Dr",
        "zipcode":"33139"
    }
}

# 4
len(student)

# 5
student["skills"]
type(student["skills"])

# 6
student["skills"].append("HTML")

# 7
keys = student.keys()
print(keys)

# 8
values = student.values()
print(values)

# 9
print(student.items())

# 10
del student["first_name"]
print(student)

# 11
del student 