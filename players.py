# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[1:4])

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[:3])

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[2:])

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[-3:])

# # Can include a third value in the brackets, this will tell pythonhow many items
# # to skip in between items in the specified range

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]: 
    print(player.title())