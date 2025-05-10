guest_list = ['Drake', 'Alexstrasza', 'Varian', 'Christian', 'Spencer', 'Tristan', 'Joseph']

print("Hey guys I can only bring two people to dinner, I'm sorry.")

print(guest_list)
print(f"Sorry {guest_list.pop()}, I have to cancel your invite for tonight")
print(f"Sorry {guest_list.pop()}, I have to cancel your invite for tonight")
print(f"Sorry {guest_list.pop()}, I have to cancel your invite for tonight")
print(f"Sorry {guest_list.pop()}, I have to cancel your invite for tonight")
print(f"Sorry {guest_list.pop()}, I have to cancel your invite for tonight")


print(f"Hey, {guest_list[1]} you're still invited to dinner")
print(f"{guest_list[0]}, we're still on for dinner tonight")

del guest_list[0]
del guest_list[0]

print(guest_list)