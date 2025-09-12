### Day 10 

## Level 1

# 1
count = 0

while count < 10:
    print(count)
    count = count + 1

print(count)

# 2
count = 10

while count > 0:
    print(count)
    count = count - 1

print(count)

# 3
count = 0

while count < 8:
    print(count * "#")
    count = count + 1

# 4
for row in range(4):
    for column in range(2):
        print("# " * 8)

# 5
count = 0

while count < 11:
    print(f"{count} x {count} = {count * count}")
    count = count + 1

# 6
languages = ["Python", "Numpy", "Pandas", "Django", "Flask"]

for language in languages:
    print(language)

# 7
for i in range(0, 101, 2):
    print(i)

# 8
for i in range(1, 101, 2):
    print(i)

## Level 2

# 1
sum = 0

for i in range(0, 101):
    sum = sum + i

print(f"The sum of all numbers is {sum}.")

# 2
even_sum = 0
odd_sum = 0

for i in range(0, 101, 2):
    even_sum = even_sum + i

for i in range(1, 101, 2):
    odd_sum = odd_sum + i

print(f"The sum of all evens is {even_sum}. The sum of all odds is {odd_sum}.")

## Level 3

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

land_countries = list(countries)

for country in countries:
    if "land" in country:
        land_countries.append(country)

print(land_countries)

# 2

fruits = ["banana", "orange", "mango", "lemon"]

reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)

# 3
from countries_data import countries

total_languages = []

for country in countries:
    for language in country["languages"]:
        total_languages.append(language)

unique_languages = set(total_languages)
print("Total number of languages:", len(unique_languages))

counts = {}

for country in countries:
    for language in country["languages"]:
        if language in counts:
            counts[language] += 1
        else:
            counts[language] = 1

items = []

for language, number in counts.items():
    items.append([number, language])

items.sort(reverse = True)

top_10_languages = items[:10]

print("Top 10 Languages:")

for count, language in top_10_languages:
    print(language, ":", count)

populations = []

for country in countries:
    name = country["name"]
    population = country["population"]
    populations.append([population, name])

populations.sort(reverse = True)

top_10_populations = populations[:10]
print("Top 10 Populations:")

for population, country in top_10_populations:
    print(country, ":", population)