users = ['mike', 'drake', 'skyler', 'kaiden', 'admin']
if users:
    for user in users:
        if user == 'admin':
            print(f"Hello, would you like to see a status report, admin?")
        else:
            print(f"Hello {user.title()}, welcome back.")
else:
    print("We need users!")