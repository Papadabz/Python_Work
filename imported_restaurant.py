from restaurant import Restaurant

my_restaurant = Restaurant('Daddys', 'sandwiches')
my_restaurant.open()
my_restaurant.describe()
my_restaurant.set_number_served(100)
print(f"The amount we've served today is: {my_restaurant.number_served}")