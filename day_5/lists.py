### Day 5

## Level 1

# 1
list = []

# 2
names = ["Max", "John", "James", "Cameron", "Nathan", "Noah", "Ben"]

# 3
print(len(names))

# 4
print(names[::3])

# 5
mixed_data_types = ["James", 20, 70, "Single", "USA"]

# 6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7
print(it_companies)

# 8
print(len(it_companies))

# 9
print(it_companies[::3])

# 10
it_companies[0] = "IBM"
print(it_companies)

# 11
it_companies.append("NVIDIA")
print(it_companies)

# 12
it_companies.insert(4, "Meta")
print(it_companies)

# 13
it_companies[1] = it_companies[1].upper()
print(it_companies)

# 14
joined = "#; ".join(it_companies)
print(joined)

# 15
print("IBM" in it_companies)

# 16
it_companies.sort()
print(it_companies)

# 17
it_companies.reverse()
print(it_companies)

# 18
print(it_companies[0:3])

# 19
print(it_companies[-3:])

# 20
if len(it_companies) % 2 == 0:
    mid1 = len(it_companies) // 2 - 1
    mid2 = len(it_companies) // 2 + 1
    middle = it_companies[mid1:mid2]
    print(middle)
elif len(it_companies) % 2 != 0:
    middle = it_companies[len(it_companies) // 2]
    print(middle)

# 21
it_companies.pop(0)
print(it_companies)

# 22
if len(it_companies) % 2 == 0:
    mid1 = len(it_companies) // 2 - 1
    mid2 = len(it_companies) // 2 + 1
    middle = it_companies[mid1:mid2]
    print(middle)
elif len(it_companies) % 2 != 0:
    middle = it_companies[len(it_companies) // 2]
    print(middle)

# 23
it_companies.pop(-1)
print(it_companies)

# 24
it_companies.clear()
print(it_companies)

# 25
del it_companies

# 26
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]

front_end.extend(back_end)

# 27
full_stack = front_end 
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)

## Level 2

# 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages[0])
print(ages[-1])
ages.append(19)
ages.append(26)

if len(ages) % 2 == 0:
    mid1 = len(ages) // 2 - 1
    mid2 = len(ages) // 2
    median = (ages[mid1] + ages[mid2]) / 2
    print(median)
elif len(ages) % 2 != 0:
    median = ages[len(ages) // 2]
    print(median)

average = sum(ages) / len(ages)
print(average)

range = ages[-1] - ages[0]

min_minus_average = abs(ages[0] - average)
max_minus_average = abs(ages[-1] - average)
print(min_minus_average, max_minus_average)

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

# 1
if len(countries) % 2 == 0:
    mid1 = len(countries) // 2 - 1
    mid2 = len(countries) // 2
    middle = countries[mid1:mid2 + 1]
    print(middle)
elif len(countries) % 2 != 0:
    middle = countries[len(countries) // 2]
    print(middle)

# 2
if len(countries) % 2 == 0:
    mid = len(countries) // 2
    list_one = countries[:mid]
    list_two = countries[mid:]
    
elif len(countries) % 2 != 0:
    mid = countries[len(countries) // 2 + 1]
    list_one = countries[:mid]
    list_two = countries[mid:]

print(list_one)
print(list_two)

# 3
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_item, second_item, third_item, *scandic = countries
print(first_item)
print(second_item)
print(third_item)
print(scandic)