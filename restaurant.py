class Restaurant:
    """Class that defines cuisine and open"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe(self):
        """Describes restaurant"""
        print(f"\n{self.restaurant}, is a {self.cuisine} style restaurant")

    def open(self):
        """Let's people know if restaurant is open"""
        print(f"{self.restaurant} is open!")

    def set_number_served(self, guests):
        """Set the number of guests served"""
        self.number_served = guests

    def increment_number_served(self, increment):
        """Add a given number to the number of guests served"""
        self.number_served += increment

class IceCreamStand(Restaurant):
    """Child class of restaurant"""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Initialize ice cream stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavor(self):
        """Display ice cream flavor"""
        print(f"the flavors are:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# ice_cream = IceCreamStand('ice cream parlor', 'ice cream', ['chocolate', 'banana'])
# ice_cream.display_flavor()

# restaurant = Restaurant('Brasserie', 'French')
# print(f"Number served: {restaurant.number_served}")

# restaurant.number_served = 200
# print(f"Number served: {restaurant.number_served}")

# restaurant.set_number_served(300)
# print(f"Number served: {restaurant.number_served}")

# restaurant.increment_number_served(100)
# print(f"Number served: {restaurant.number_served}")

