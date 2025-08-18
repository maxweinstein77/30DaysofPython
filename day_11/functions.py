## Day 11: 30 Days of Python

# 1
def add_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum

# 2
def area_of_circle(r):
    pi = 3.14
    area = pi * r ** 2
    return area 

# 3
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if type(num) == int or type(num) == float:
            total += num
        else:
            return f"Error: does not accept{type(num)}. Enter a number."
    return total

# 4
def celsius_to_farenheit(celsius):
    farenheit = celsius * (9/5) + 32
    return farenheit 

# 5
def check_season(month):
    month = month.capitalize()

    if month in ["December", "January", "February"]:
        return f"It's currently winter."
    elif month in ["March", "April", "May"]:
        return f"It's currently spring."
    elif month in ["June", "July", "August"]:
        return f"It's currently summer."
    elif month in ["September", "October", "November"]:
        return f"It's currently autumn."
    else:
        return "That month does not exist."
    
# 6
def calculate_slope(x_1, y_1, x_2, y_2):
    slope = ((y_2 - y_1) / (x_2 - x_1))
    return slope 

# 7
import math

def solve_quadratic_eqn(a, b, c):
    if (b ** 2 - 4 * a * c) > 0:
        x_1 = (-b + math.sqrt((b ** 2 - 4 * a * c) / (2*a)))
        x_2 = (b + math.sqrt((b ** 2 - 4 * a * c) / (2*a)))
        return {x_1, x_2}
    elif (b ** 2 - 4 * a * c) == 0:
        x = -b / (2 * a)
        return {x}
    else:
        return set()

# 8
def print_list(items):
    for item in items:
        print(item)

# 9 
def reverse_list(items):
    reversed_list = []
    for i in range(len(items) - 1, -1, -1):
        reversed_list.append(items[i])
    return reversed_list

# 10
def capitalize_list_items(items):
    capitalized_list = []
    for item in items:
        capitalized_list.append(item.capitalize())
    return capitalized_list 

# 11
def add_item(items, item):
    items.append(item)
    return items

# 12
def remove_item(items, item):
    if item in items:
        items.remove(item)
    return items

# 13
def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

# 14
def sum_of_odds(n):
    odd_total = 0
    for i in range(n + 1):
        if i % 2 != 0:
            odd_total += i
    return odd_total

# 15
def sum_of_even(n):
    even_total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            even_total += i
    return even_total

# Exercises: Level 2

# 1
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f"The number of odds are {odds}.")
    print(f"The number of evens are {evens}.")

# 2
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 3 
def is_empty(item):
    return len(item) == 0

# 4
def calculate_mean(items):
    total = 0
    for item in items:
        total += item
    mean = total / len(items)
    return mean

def calculate_median(items):
    items = sorted(items)
    n = len(items)

    if n % 2 != 0:
        return items[n // 2]
    else:
        return (items[n // 2 - 1] + items[n // 2]) / 2

def calculate_mode(items):
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    mode = max(counts, key=lambda x: counts[x])
    return mode

def calculate_range(items):
    result = max(items) - min(items)
    return result 

def calculate_variance(items):
    mean = calculate_mean(items)
    total = 0
    for item in items:
        total += (item - mean) ** 2
    variance = total / len(items)
    return variance

import math

def calculate_std(items):
    mean = calculate_mean(items)
    total = 0
    for item in items:
        total += (item - mean) ** 2
    std = math.sqrt(total / (len(items) - 1))
    return std

# Exercises: Level 3

# 1
def is_prime(n):
    if n <= 1:
        return False 
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 

# 2
def is_unique(items):
    seen = []
    for item in items:
        if item in seen:
            return False 
        elif item not in seen:
            seen.append(item)

# 3
def same_data_type(items):
    for item in items:
        if type(item) != type(items[0]):
            return False
    return True

# 4
def is_valid_variable(variables):
    for variable in variables:
        if variable[0].isdigit() or " " in variable:
            return False
        return True
    
# 5
import json

def most_populated_countries(n=10):
    with open("countries_data.py", "r") as f:
        countries = json.load(f)

    populations = []
    for country in countries:
        populations.append((country["name"], country["population"]))

    sorted_populations = sorted(populations, key=lambda x: x[1], reverse=True)
    return sorted_populations[:n]


def most_spoken_languages(n=10):
    with open("countries_data.py", "r") as f:
        countries = json.load(f)

    language_frequency = {}

    for country in countries:
        for lang in country["languages"]:
            if lang in language_frequency:
                language_frequency[lang] += 1
            else:
                language_frequency[lang] = 1

    sorted_langs = sorted(language_frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_langs[:n]