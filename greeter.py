# prompt = "If you share your name, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"Hello, {name.title()}!")

# # # Using functions

# def greet_user(username):
#     """Display a simple greeting"""
#     print(f"Hello {username.title()}!")

# greet_user('jesse')

# # # Using a function with a while Loop

def get_formatted_name(first_name, last_name):
    """Return full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#This is an infinite loop
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name.title()}")