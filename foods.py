# my_foods = ['pizza', 'falafel', 'carrot cake']
# friends_foods = my_foods[:]

# my_foods.append('cannoli')
# friends_foods.append('ice cream')

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friends_foods)

my_food = ['pizza', 'falafel', 'carrot cake']
friends_food = my_food[:]

my_food.append('cannoli')
friends_food.append('ice cream')

for food in my_food:
    print(f"My favorite food is {food}")

for foods in friends_food:
    print(f"My friends favorite foods are {foods}")
