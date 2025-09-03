### Day 3

# 1
age = 18

# 2
height = 70.5

# 3
comp_number = 3 - 3j

# 4
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area_of_triangle = 0.5 * base * height 
print("The area of the triangle is", area_of_triangle)

# 5
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter_of_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is", perimeter_of_triangle)

# 6
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print("The area of the rectangle is", area_of_rectangle)
print("The perimeter of the rectangle is", perimeter_of_rectangle)

# 7
radius = float(input("Enter radius: "))
area_of_circle = 3.14 * radius * radius
circumference_of_circle = 2 * 3.14 * radius
print("The area of the circle is", area_of_circle)
print("The circumference of the circle is", circumference_of_circle)

# 8
# Equation: y = 2x - 2
slope = 2
x_intercept = 1
y_intercept = -2

print("Slope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept", y_intercept)

# 9
import math

x_1 = 2
x_2 = 6
y_1 = 2
y_2 = 10

slope = (y_2 - y_1) / (x_2 - x_1)
euclidean_distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
print("Slope", slope)
print("Euclidean Distance:", euclidean_distance)

# 10
slope_8 = 2
slope_9 = 2
print(slope_8 == slope_9)

# 11
x = -3
y = x ** 2 + 6 * x + 9
print(y)

# 12
print(len("python"))
print(len("dragon"))
print(len("python") > len("dragon"))

# 13
print("on" in "python" and "on" in "dragon")

# 14
print("jargon" in "I hope this course is not full of jargon.")

# 15
print("on" not in "dragon" and "on" not in "python")

# 16
print(str(float(len("python"))))

# 17
# You can use the modulus operator to determine the remainder and thus whether it's an even number.
number = float(input("Number: "))
even_checker = number % 2

if even_checker % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")

# 18
print((7 // 3) == int(2.7))

# 19
print(type("10") == type(10))

# 20
print(int((float("9.8"))) == 10)

# 21
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print("Your weekly earning is", pay)

# 22
years_lived = int(input("Enter number of years you have lived: "))
seconds_lived = years_lived * 31536000
print("You have lived for", seconds_lived, "seconds.")

# 23
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)