dad = 'Michael'
print(dad.lower() == 'michael')
##################################3
age = 21
print(age >= 18)
##############################
pizza = 'Pepperoni'
if pizza != 'Mushroom':
    print("No fungi please!")
############################
age_0 = 21
age_1 = 22

if age_0 and age_1 >= 18:
    print("You can vote!")
###################################
age_0 = 17
age_1 = 16
if age_0 or age_1 <= 21:
    print("We cannot let you into the pub")
####################################
pizzas = ['Pepperoni', 'Mushroom', 'Spinach']
print('Pepperoni' in pizzas)
print('Sausage' in pizzas)