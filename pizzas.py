pizzas = ['Pepperoni', 'Cheese', 'Sausage', 'Spinach']
for pizza in pizzas:
    print(f"I like {pizza} pizza")
print("\nI really love pizza")

friends_pizza = pizzas[:]

pizzas.append('Supreme')
friends_pizza.append('Broccoli')

print(f"My favorite pizzas are:\n{pizzas}")
print(f"My friends favorite pizzas are:\n{friends_pizza}")