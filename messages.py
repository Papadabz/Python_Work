def show_messages(unprinted_messages):
    """Print unprinted messages"""
    while unprinted_messages:
        current_message = unprinted_messages.pop()
        print(f"{current_message}")
    

unprinted_messages = ['I love you', "You're doing great", 'Python is cool']
show_messages(unprinted_messages)

