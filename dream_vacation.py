dream_vacations = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    vacation = input("What is your dream vacation? ")

    dream_vacations[name] = vacation

    repeat = input("Would anyone else like to take the poll? (yes/ no) ")

    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, vacation in dream_vacations.items():
    print(f"{name.title()}'s dream vacation is {vacation.title()}")