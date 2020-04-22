import requests, json

def format_country_name(country):
    switcher = {
        'Afghanistan': 'Afghanistan',
        'United States of America': 'United States',
        'Cabo Verde': 'Cape Verde',
        'Iran (Islamic Republic of)': 'Iran',
        'Macedonia (the former Yugoslav Republic of)': 'Macedonia',
        'Moldova (Republic of)': 'Moldova',
        'Saint Martin (French part)': 'Saint Martin',
        'Sint Maarten (Dutch part)': 'Sint Maarten',
        "Korea (Democratic People's Republic of)": 'North Korea',
        "Korea (Republic of)": 'South Korea',
        'Venezuela (Bolivarian Republic of)': 'Venezuela',
    }
    return switcher.get(country, country)


hipo_json_data = requests.get('http://universities.hipolabs.com/search?').json()

school_data = []

## country

pk = 1
country_data = []
country_dict = {}

for item in hipo_json_data:
    country_name = format_country_name(item['country'])
    
    if not country_dict.get(country_name, None):
        country_data.append(
            {
                'model': 'accounts.country',
                'pk': pk,
                'fields': {
                    'name': country_name
                }
            }
        )
        country_dict[country_name] = pk
        pk += 1

with open('../accounts/fixtures/country.json', 'w') as outfile:
    json.dump(country_data, outfile)

## school

pk = 1
for item in hipo_json_data:
    country = format_country_name(item['country'])
    
    school_data.append(
        {
            'model': 'accounts.school',
            'pk': pk,
            'fields': {
                'name': item['name'],
                'country': country_dict[country]
            }
        }
    )
    pk += 1

with open('../accounts/fixtures/university.json', 'w') as outfile:
    json.dump(school_data, outfile)


## major

import csv

major_data = []

with open('major.csv', 'r') as csvfile:

    reader = csv.reader(csvfile)
    pk = 1
    for row in reader:
        major_name = row[1].lower().title()
        major_data.append(
            {
                'model': 'accounts.major',
                'pk': pk,
                'fields': {
                    'name': major_name
                }
            }
        )
        pk += 1

with open('../accounts/fixtures/major.json', 'w') as outfile:
    json.dump(major_data, outfile)