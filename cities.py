# cities = {
#     'denver': {
#         'country': 'united states',
#         'population': 716_000,
#         'fact': "Denver is known as the Mile High city"
#     },
    
#     'barcelona': {
#         'country': 'spain',
#         'population': 1_600_000,
#         'fact': 'Some people believe Barcelona was founded by Hercules'
#     },

#     'kyoto': {
#         'country': 'japan',
#         'population': 1_450_000,
#         'fact': 'Kyoto was the capital of Japan for over 1000 years'
#     },
# }

# for city, facts in cities.items():
#     print(f"\n{city.title()}")
#     for fact in facts:
#         country = f"{facts['country']}"
#         pop = f"{facts['population']}"
#         city_fact = f"{facts['fact']}"
#     print(f"Country: {country.title()}")
#     print(f"Population: {pop}")
#     print(f"Fun fact: {city_fact}")

# # # 
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}")

# # # Cities Try It Yourself

def describe_city (city, country='united states'):
    """Cities in US"""
    print(f"{city.title()} is a city in the country {country.title()}")

describe_city(city='colorado')
describe_city(city='austin')
describe_city(city='tokyo', country='japan')