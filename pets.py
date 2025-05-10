# pets = {
#     'navi': {
#         'animal': 'dog',
#         'owner': 'danny',
#         },

#     'majora': {
#         'animal': 'cat',
#         'owner': 'zaira',
#     },

#     'cheese': {
#         'animal': 'cat',
#         'owner': 'tasha',
#     }
# }

# for pet, info in pets.items():
#     print(f"\n{pet.title()}:")
#     breed = f"{info['animal']}"
#     owner = f"{info['owner']}"
#     print(f"{pet.title()} is a {breed.title()}\nTheir owner is {owner.title()}")

# # # Using While loops to take multiple copies of an item out of a list

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# # # Positional Arguments with functions

# def describe_pet(animal_type, pet_name):
    # """Display information about a pet"""
    # print(f"\nI have a {animal_type}.")
    # print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# # # Keyword arguments with Functions 

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type='hamster', pet_name='harry')

# # # Default Values
# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet('willie')


