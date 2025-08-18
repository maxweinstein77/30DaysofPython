## Day 10: 30 Days of Python

# Exercises: Level 1

# 1
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

count = 0
while count < 11:
    print(count)
    count = count + 1

# 2 
for number in range(10, -1, -1):
    print(number)

count = 10
while count > -1:
    print(count)
    count = count - 1

# 3
count = 0
while count < 8:
    print(count * "#")
    count = count + 1

# 4
for row in range(0, 8):
    string = ""
    for col in range(0, 8):
        string = string + "#"
    print(string)

# 5
for i in range(0, 11):
    print(f"{i} * {i} = {i * i}")

# 6
languages = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for language in languages:
    print(language)

# 7
for i in range(0, 101, 2):
    print(number)

# 8 
for i in range(1, 100, 2):
    print(number)

# Exercises: Level 2

# 1
sum = 0

for i in range(0, 101):
    print(i)
    sum = sum + i
print("The sum of all the numbers is", sum)

# 2
even_sum = 0
odd_sum = 0

for i in range(0, 101, 2):
    even_sum = even_sum + i

for i in range(1, 101, 2):
    odd_sum = odd_sum + i

print("The sum of all the even numbers is", even_sum)
print("The sum of all the odd numbers is", odd_sum)

# Exercises: Level 3

# 1
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

for country in countries:
    if "land" in country:
        print(country)

# 2
fruits = ["banana", "orange", "mango", "lemon"]

for i in range(len(fruits) - 1, -1, -1):
    print(fruits[i])

# 3

import json

with open("countries_data.py", "r") as f:   
    countries = json.load(f)

for country in countries:
    for lang in country["languages"]:
        languages.add(lang)
    
print("Total number of languages", len(languages))



import json

with open("countries_data.py", "r") as f:   
    countries = json.load(f)

language_frequency = {}

for country in countries:
    for lang in country["languages"]:
        if lang in language_frequency:
            language_frequency[lang] = language_frequency[lang] + 1
        else:
            language_frequency[lang] = 1

sorted_langs = sorted(language_frequency.items(), key=lambda x: x[1], reverse=True)
top_10 = sorted_langs[:10]

for lang, count in top_10:
    print(lang, count)



import json

with open("countries_data.py", "r") as f:   
    countries = json.load(f)

populations = []

for country in countries:
    populations.append((country["name"], country["population"]))

sorted_populations = sorted(populations, key = lambda x: x[1], reverse=True)
top_10 = sorted_populations[:10]

for country, pop in top_10:
    print(country, pop)is