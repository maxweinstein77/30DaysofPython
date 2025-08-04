## Day 3: 30 Days of Python Programming

# Exercises

# 1
age = 18

# 2
height = 71 # Inches

# 3
complex = 2 - 2j

# 4
base = input("Enter base: ")
height = input("Enter height: ")
area = 0.5 * float(base) * float(height)
print("The area of the triangle is", area) 

# 5
side_a = input("Enter side a: ")
side_b = input("Enter side b: ")
side_c = input("Enter side c: ")
perimeter = int(side_a) + int(side_b) + int(side_c)
print("The perimeter of the triangle is", perimeter)

# 6
length = input("Length: ")
width = input("Width: ")
area = int(length) * int(width)
print("Area", area)
perimeter = 2 * (int(length) * int(width))
print("Perimeter:", perimeter)

# 7
radius = int(input("Radius: "))
area = 3.14 * radius * radius 
print("Area:", area)
circumference = 2 * 3.14 * radius 
print("Circumference", circumference)

# 8
# Equation: y = 2x - 2
m = 2
b = -2
x_int = -b / m 
print("Slope:", m)
print("Y-intercept:", b)
print("X-intercept:", x_int)

# 9
import math 

a, b = 2, 2
c, d = 6, 10

euclidean_distance = math.sqrt(((c - a) ** 2) + ((d - b) ** 2))
print(euclidean_distance)
slope = (d - b) / (c - a)
print(slope)

# 10
print(m == slope)

# 11
x = -3
y = (x ** 2) + (6 * x) + 9
print(y)

# 12
print(len("python"))
print(len("dragon"))
print(len("python") != len("dragon"))

# 13
print("on" in ("dragon" and "python"))

# 14
print("jargon" in "I hope this sentence is not full of jargon.")

# 15
print("on" not in ("dragon" and "python"))

# 16
print(str(float(len("python"))))

# 17
num_1 = int(input("Enter a number: "))
print(num_1 % 2 == 0)

# 18
print(7 // 3 == int(2.7))

# 19
print(type("10") == type(10))

# 20
print(int(float("9.8")) == 10)

# 21
hours = int(input("Enter hours: "))
hourly_rate = int(input("Enter rate per hor: "))
weekly_earning = hours * hourly_rate 
print("Your weekly earning is", weekly_earning)

# 22
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds")

# 23
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)