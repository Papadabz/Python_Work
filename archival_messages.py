def show_messages(unprinted_messages, sent_messages):
    """Print unprinted messages"""
    while unprinted_messages:
        current_message = unprinted_messages.pop()
        print(f"{current_message}")
        sent_messages.append(current_message)
    

unprinted_messages = ['I love you', "You're doing great", 'Python is cool']
sent_messages = []
show_messages(unprinted_messages[:], sent_messages)

print(unprinted_messages)
print(sent_messages)