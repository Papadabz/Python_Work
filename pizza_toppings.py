prompt = ("\nWhat kind of toppings would you like on your pizza?")
prompt += ("\nLet's get that order started, just let me know when to quit: ")

active = True
while active:
    toppings = input(prompt)

    if toppings == 'quit':
        active = False
    else:
        print(f"We will add {toppings} to your pizza")

