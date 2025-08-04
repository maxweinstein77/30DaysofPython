## Day 4: 30 Days of Python Programming

# Exercises: Level 1

# 1
empty_list = []

# 2
list = ["one", "two", "three", "four", "five", "six", "seven"]

# 3
print(len(list))

# 4
print(list[::3])

# 5
mixed_data_types = ["Max", 18, 71, "Single", "7071"]

# 6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7
print(it_companies)

# 8
print(len(it_companies))

# 9
print(it_companies[::3])

# 10
it_companies[0] = "Instagram"
print(it_companies)

# 11
it_companies.append("Meta")

# 12
it_companies.insert(4, "X")
print(it_companies)

# 13
it_companies[0] = "FACEBOOK"
print(it_companies)

# 14
result = "#; ".join(it_companies)
print(result)

# 15
does_exist = "X" in it_companies 
print(does_exist)

# 16
it_companies.sort()
print(it_companies)

# 17 
it_companies.sort(reverse=True)
print(it_companies)

# 18
print(it_companies[0:2])

# 19
print(it_companies[6:])

# 20
print(it_companies[5])

# 21
it_companies.remove("X")
print(it_companies)

# 22
del it_companies[3:5]
print(it_companies)

# 23
del it_companies[-1]
print(it_companies)

# 24
it_companies = ['Oracle', 'Microsoft', 'Meta', 'FACEBOOK', 'Apple']
it_companies.clear()
print(it_companies)

# 25
del it_companies

# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)

# 27
full_stack = front_end + back_end
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)

# Exercises: Level 2

# 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min_age = min(ages)
max_age = max(ages)

ages.append(min_age)
ages.append(max_age)
print(ages)

ages.sort()
mid1 = ages[len(ages)//2 - 1]
mid2 = ages[len(ages)//2]
median = (mid1 + mid2) / 2
print(median)

average = sum(ages) / len(ages)
print(average)

range = max_age - min_age
print(range)

print(abs(min_age - average) > abs(max_age - average))

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

mid1 = countries[len(countries)//2 - 1]
mid2 = countries[len(countries)//2]
print(mid1, mid2)

# 2
mid = len(countries) // 2
first_half = countries[:mid]
second_half = countries[mid:]

print(first_half)
print(second_half)

# 3
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
cn, ru, usa, *scandic = countries
print(cn)
print(ru)
print(usa)
print(scandic)