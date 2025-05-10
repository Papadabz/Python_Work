# # # My Solution
# prompt = ("\nHow old are you, so I can get you your ticket? ")
# prompt += ("\nType 'quit' to stop. ")

# while True:

#     age = input(prompt)
#     age = int(age)

#     if age == 'quit':
#         break

#     elif age <= 2:
#         print("\nYour ticket is free!")
#     elif age <= 11:
#         print("\nYour ticket will be $10")
#     elif age >= 12:
#         print("\nYour ticket will be $15")
        
# # # Better solution
prompt = ("\nHow old are you?")
prompt += ("\nType 'quit' to stop. ")

while True:
    age = input(prompt)
    
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age < 13:
            price = 10
        elif age >= 13:
            price = 15
    print(f"Your ticket price will be ${price}.")