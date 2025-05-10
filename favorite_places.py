favorite_places = {
    'christian': ['home', 'azeroth', 'work'],
    'zaira': ['home', 'school'],
    'zelda': ['school', 'outside']
}

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are:")
    for place in places:
        print(f"{place.title()}")