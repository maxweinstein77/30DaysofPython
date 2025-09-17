### Day 11

## Level 1

# 1
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum

print(add_two_numbers(2, 3))

# 2
def area_of_circle(radius):
    pi = 3.14
    area = 3.14 * radius ** 2
    return area

print(area_of_circle(2))

# 3
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, (int, float)):
            total += num
        else:
            print("Only numbers allowed.")
            return
    return total

add_all_nums("Max", 2, 3)

# 4
def celsius_to_farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

print(celsius_to_farenheit(0))

# 5
def check_season(month):
    autumn = ["September", "October", "November"]
    winter = ["December", "January", "February"]
    spring = ["March", "April", "May"]
    summer = ["June", "July", "August"]

    month = month.capitalize()

    if month in autumn:
        print("Season: Autumn")
    elif month in winter:
        print("Season: Winter")
    elif month in spring:
        print("Season: Spring")
    elif month in summer:
        print("Season: Summer")
    else:
        print("Invalid month.")

check_season("february")

# 6
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

print(calculate_slope(5, 5, 10, 10))

# 7
import cmath

def solve_quadratic_eqn(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    return root1, root2

# 8
def print_list(list):
    for i in range(len(list)):
        print(list[i])

# 9
def reverse_list(list):
    for i in range(len(list) - 1, -1, -1):
        print(list[i])

# 10
def capitalize_list_items(list):

    capitalized_list = []

    for i in range(len(list)):
        capitalized_word = list[i].capitalize()
        capitalized_list.append(capitalized_word)

    return capitalized_list 

fruits = ["apple", "banana", "orange"]
print(capitalize_list_items(fruits))

# 11
def add_item(list, item):
    list.append(item)
    return list 

food_staff = ["Potato", "Tomato", "Mango", "Milk"]
print(add_item(food_staff, "Meat"))

# 12
def remove_item(list, item):
    list.pop(item)
    return list

numbers = [2, 3, 7, 9]

print(remove_item(numbers, 3))

# 13
def sum_of_numbers(number):
    total = 0
    for i in range(0, number + 1):
        total += i
    
    return total

print(sum_of_numbers(5))

# 14
def sum_of_odds(number):
    odd_total = 0
    for i in range(1, number + 1, 2):
        odd_total += i
    
    return odd_total

print(sum_of_odds(5))

# 15
def sum_of_even(number):
    even_total = 0
    for i in range(0, number + 1, 2):
        even_total += i
    
    return even_total

print(sum_of_even(6))

## Exercises: Level 2

# 1
def evens_and_odds(pos_int):
    odds = 0
    evens = 0

    for i in range(0, pos_int + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1

    print("The number of odds are {odds}.")
    print("The number of evens are {evens}.")

# 2
import math

def factorial(whole_num):
    return math.prod(range(1, whole_num + 1))

print(factorial(4))

# 3
def is_empty(array):
    if len(array) == 0:
        return "List is empty."
    else:
        return "List is not empty."

# 4
def calculate_mean(array):
    mean = sum(array) / len(array)

    return mean

nums = [1, 2, 3, 4]
print(calculate_mean(nums))

def calculate_median(array):

    array.sort()

    n = len(array)

    if n % 2 == 0:
        mid1 = n // 2
        mid2 = n // 2 - 1
        median = (array[mid1] + array[mid2]) / 2
    else:
        median = array[n // 2]
    return median

def calculate_mode(array):
    max_count = 0
    mode = None

    for num in array:
        count = array.count(num)
        if count > max_count:
            max_count = count
            mode = num
        
    return mode 

def calculate_range(array):
    array.sort()

    range = max(array) - min(array)

    return range

def calculate_variance(array):
    mean = sum(array) / len(array)
    total = 0

    for x in array:
        total += (x - mean) ** 2
    return total / (len(nums) - 1)

def calculate_std(array):

    import math

    mean = sum(array) / len(array)
    total = 0

    for x in array:
        total += (x - mean) ** 2
    return math.sqrt(total / (len(array) - 1))

## Level 3

# 1
def is_prime(num):
    import math

    if num <= 1:
        return False
    for i in range(2, math.sqrt(num) + 1):
        if num % i == 0:
            return False
    return True

# 2
def is_unique(items):
    return len(items) == len(set(items))

# 3
def is_same_data_type(items):
    if len(items) == 0:
        return True
    
    first_type = type(items[0])

    for item in items:
        if not isinstance(item, first_type):
            return False
    return True

# 4
def is_valid_variable(name):

    import keyword

    return name.isidentifier() and not keyword.iskeyword(name)

# 5

from countries_data import countries

def most_spoken_languages():
    language_count = {}

    for country in countries:
        for lang in country["languages"]:
            if lang in language_count:
                language_count[lang] += 1
            else:
                language_count[lang] = 1
    
    sorted_languages = sorted(language_count.items(), key = lambda x : x[1], reverse = True)

    result = []

    for lang, count in sorted_languages[:10]:
        result.append((lang, count))
    return result

def most_populated_countries():
    sorted_countries = sorted(countries, key = lambda x : x["population"], reverse = True)

    result = []

    for country in sorted_countries[:10]:
        result.append((country["name"], country["population"]))
    return result