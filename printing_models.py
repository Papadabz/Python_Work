# # # The following code does not use functions

# #Start with some designs that need to be printed
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# #Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing Model: {current_design}")
#     completed_models.append(current_design)

# #Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# # # Reorganizing with functions

from printing_functions import *

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)