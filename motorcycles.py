# # Modifying elements on a list
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# # This line replaces what was originally at position 0
# motorcycles[0] = 'ducati'
# print(motorcycles)

# # Appending elements to a list # #

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles.append('ducati')
# print(motorcycles)

# motorcycles = []

# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

# # Removing Items using the Delete Statement # #
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# del motorcycles[1]
# print(motorcycles)

## Removing an item using the pop() method

# motorcycles = ['honda', 'yahama', 'suzuki']
# print(motorcycles)

# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# motorcycles = ['honda', 'yamaha', 'suzuki']

# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}")

## Removing an item by Value ##

# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
# print(motorcycles)

# motorcycles.remove('ducati')
# print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")