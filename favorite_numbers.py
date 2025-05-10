favorite_numbers = {'res': [4, 7],
                    'freedle': [69, 68],
                    'mesc': [9, 8], 
                    'christian': [64, 12],
                    'me': [7, 9],
                    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")
