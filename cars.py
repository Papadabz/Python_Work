# # Sorting a list permanentally using the sort() method # #
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)

# # Sorting a List Temporarily with the sorted() function

#cars = ['bmw', 'audi', 'toyota', 'subaru']

# print("Here is the original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original list again:")
# print(cars)

# # Printing a List in Reverse Order

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)

# cars.reverse()
# print(cars)

# # Finding the Length of a List # #
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(len(cars))

# # Using IF statements to capitalize BMW
# cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# car = 'bmw'
# print(car == 'bmw')

# car = 'audi'
# print(car == 'bmw')

# # # functions and dictonary

def build_car(make, model, **car_info):
    """Build a dictionary containing everything we know about a user"""
    car_info['make'] = make.title()
    car_info['model'] = model.title()
    return car_info

car_profile = build_car('subaru', 'outback',
                         color='blue',
                         tow_package=True)

print(car_profile)