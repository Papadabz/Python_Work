# christian = {'first_name': 'christian', 
#              'last_name': 'leedom', 
#              'age': 27,
#              'city': 'rainier'}

# print(christian['first_name'].title())
# print(christian['last_name'].title())
# print(christian['age'])
# print(christian['city'].title())

# # # Returning a dictionary

# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person"""
#     person = {'first': first_name, 'last': last_name}
#     return person

# musician = build_person('jimi', 'hendrix')
# print(musician)

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician) 