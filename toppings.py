# # Inequality operator != practice. Google more.
# requested_toppings = 'mushrooms'

# if requested_toppings != 'anchovies':
#     print("Hold the anchovies!")

# # If statements on toppings
# requested_toppings = ['Mushrooms', 'Extra Cheese']

# if 'Mushrooms' in requested_toppings:
#     print("Adding mushrooms")
# if 'Pepperoni' in requested_toppings:
#     print("Adding pepperoni")
# if 'Extra Cheese' in requested_toppings:
#     print("Adding Extra Cheese")
# print("\nFinished making your pizza")

# #  #Proving elif doesn't work # # #
# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms")
# elif 'pepperoni' in requested_toppings:
#     print("Adding pepperoni")
# elif 'extra heese' in requested_toppings:
#     print("Adding Extra Cheese")
# print("\nFinished making your pizza")

# # # Using for loop with if-else statement # # # 
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now")
#     else:
#         print(f"Adding {requested_topping}")

# print("\nFinished making your pizza!")

# # # Checking that a list is not empty # # # 
# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}")
#     print("\nFinished making your pizza")
# else:
#     print("Are you sure you want a plain pizza?")

# # # Using multiple lists # # #

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else: 
        print(f"Sorry we don't have {requested_topping}")

print("\nFinished making your pizza")