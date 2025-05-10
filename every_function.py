family = ['dad', 'vicki', 'drake', 'skyler', 'kaiden']
print(family)
print(sorted(family))
print(sorted(family, reverse=True))
family.sort()
print(family)
family.sort(reverse=True)
print(family)
print(f"The oldest of my brothers is, {family[2].title()}")

youngest = 'kaiden'
family.remove(youngest)
print(f"I removed {youngest.title()}, because he was the youngest on the list")
family[3] = 'mike'
print(family)
family.append('zaira')
print(family) 
del family[4]
print("\n\t", family)

popped_family = family.pop()

print(family)
family.reverse()
print(family)
print(len(family))