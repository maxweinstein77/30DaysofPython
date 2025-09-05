### Day 5

## Level 1

# 1
list = []

# 2
fruits = ["Apple", "Banana", "Orange", "Cantaloupe", "Kiwi", "Plum", "Orange"]

# 3
print(len(fruits))

# 4
print(fruits[::3])

# 5
mixed_data_types = ["Max", 20, 70, "Single", "USA"]

# 6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7
print(it_companies)

# 8
print(len(it_companies))

# 9
print(it_companies[::3])

# 10
it_companies[0] = "Meta"
print(it_companies)

# 11
it_companies.append("Instagram"))

# 12
it_companies.insert(4, "Aviato")

# 13
it_companies[1] = it_companies[1].upper 

# 14
joined = "#; ".join(it_companies)
print(joined)

# 15
print("Facebook" in it_companies)

# 16
it_companies.sort()

# 17
it_companies.reverse()

# 18
print(it_companies[:3])

# 19
print(it_companies[-3:])

# 20
n = len(it_companies)

if n % 2 == 0:
    mid1, mid2 = n // 2 - 1, n // 2
    mid = it_companies[mid1:mid2+1]
else:
    mid = it_companies[n // 2]
    
print(mid)

# 21
it_companies.pop(0)
print(it_companies)

# 22 
n = len(it_companies)

if n % 2 == 0:
    mid1, mid2 = n // 2 - 1, n // 2
    del it_companies[mid1:mid2+1]
else:
    it_companies.pop(n // 2)

# 23
it_companies.pop(-1)
print(it_companies)

# 24
it_companies.clear()
print(it_companies)

# 25
del it_companies

# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined = front_end + back_end

# 27
full_stack = joined
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)

## Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min = ages[0]
max = ages[-1]
print(min, max)

ages.insert(0, 19)
ages.insert(-1, 26)

n = len(it_companies)

if n % 2 == 0:
    mid1, mid2 = n // 2 - 1, n // 2
    median = ages[mid1], ages[mid2]
else:
    median = ages[n // 2]
print(median)

average = sum(ages) / len(ages)
print(average)

range = ages[-1] - ages[0]
print(range)

min_sub_avg = abs(ages[0] - average)
max_sub_avg = abs(ages[-1] - average)
print(min_sub_avg, max_sub_avg)

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
n = len(countries) 

if n % 2 == 0:
    mid1, mid2 = n // 2 - 1, n // 2
    mid = countries[mid1:mid2+1]
else:
    mid = countries[n // 2]

print(mid)

# 2
n = len(countries)

if n % 2 == 0:
    mid = n // 2 
    list_one = countries[:mid]
    list_two = countries[mid:]
else:
    mid = n // 2 + 1
    list_one = countries[:mid]
    list_two = countries[mid:]

print(list_one)
print(list_two)

# 3
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
cn, ru, usa, *scandic = countries
print(cn)
print(ru)
print(usa)
print(scandic)