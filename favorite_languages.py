# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }
# # for name, language in favorite_languages.items():
# #     print(f"{name.title()}'s favorite language is {language.title()}")

# for name in favorite_languages.keys():
#     print(name.title())

# # # Looping through keys in a dictionary

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll")

# # # Looping through a dictionaries keys in a particular order

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll!")

# # # Looping through all values in a dictionary

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }

# print("The following langauges have been mentioned:")
# for language in set(sorted(favorite_languages.values())):
#     print(language.title())

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }
# need_to_poll = (
#     'drake',
#     'skyler',
#     'mike',
#     'vicki'
#     )

# for polled in favorite_languages.keys():
#     print(f"Thank you for taking our poll, {polled.title()}")

# for poll in need_to_poll:
#     print(f"{poll.title()}, please take the poll so we can get more data!")

# # # A List in a dictionary

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")