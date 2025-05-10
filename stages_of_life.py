age = 65
if age <= 2:
    person = 'baby'
elif age <= 3:
    person = 'toddler'
elif age <= 12:
    person = 'kid'
elif age <= 19:
    person = 'teenager'
elif age <= 64:
    person = 'adult'
elif age >= 65:
    person = 'elder'

print(f"You are a {person}")