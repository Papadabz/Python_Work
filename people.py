people = {
    'christian': {
        'first_name': 'christian', 
        'last_name': 'leedom', 
        'age': 27,
        'city': 'rainier'},


    'zaira': {'first_name': 'zaira',
            'last_name': 'roybal',
            'age': 10,
            'city': 'loveland'
            },

    'zelda': {'first_name': 'zelda',
             'last_name': 'roybal',
             'age': 6,
             'city': 'loveland'
             },
}

for person, info in people.items():
    print(f"\nName: {person.title()}")
    full_name = f"{info['first_name']} {info['last_name']}"
    age = f"{info['age']}"
    city = f"{info['city']}"

    print(f"\t{full_name.title()}")
    print(f"\t{age}")
    print(f"\t{city.title()}")

