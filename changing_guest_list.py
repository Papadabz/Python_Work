guest_list = ['Thrall', 'Alexstrasza', 'Varian', 'Christian']
print(f"Hey {guest_list[1]}, I would like to invite you to dinner")
print(f"Hey {guest_list[0]}, I would like to invite you to dinner")
print(f"Hey {guest_list[2]}, I would like to invite you to dinner")
print(f"Hey {guest_list[3]}, I would like to invite you to dinner")

print(f"Hey guys, {guest_list[0].title()} can't make it so I'm going to invite Drake")
guest_list.append('Drake')

print(f"Hey guys here's the new guest list.")
print(guest_list)