current_users = ['mike', 'drake', 'skyler', 'kaiden', 'admin']

new_users = ['drake', 'zaira', 'mike']

for new_user in new_users:
    if new_user in current_users:
        print("Sorry you will have to create a new username")
    else:
        print(f"{new_user}, username is available")
