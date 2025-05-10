sandwich_orders = ['tuna', 'pastrami', 'roast beef', 'pastrami', 'blt', 'turkey', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print("Sorry we're out of pastrami!")

while sandwich_orders:
    making = sandwich_orders.pop()
    finished_sandwiches.append(making)

for finished_sandwich in finished_sandwiches:
    print(f"\nYour {finished_sandwich} is done")
