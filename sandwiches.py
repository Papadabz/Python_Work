import sandwich_functions

sandwich_functions.make_sandwich('ham', 'salami', 'pepperjack cheese')
sandwich_functions.make_sandwich('turkey', 'mayo', 'cheddar cheese')
sandwich_functions.make_sandwich('cheddar cheese', 'mozzarella cheese', 'provolone cheese')
# # # 
from sandwich_functions import make_sandwich

make_sandwich('ham', 'salami', 'pepperjack cheese')
make_sandwich('turkey', 'mayo', 'cheddar cheese')
make_sandwich('cheddar cheese', 'mozzarella cheese', 'provolone cheese')
# # # 
from sandwich_functions import make_sandwich as ms

ms('ham', 'salami', 'pepperjack cheese')
ms('turkey', 'mayo', 'cheddar cheese')
ms('cheddar cheese', 'mozzarella cheese', 'provolone cheese')
# # # 
import sandwich_functions as sf

sf.make_sandwich('ham', 'salami', 'pepperjack cheese')
sf.make_sandwich('turkey', 'mayo', 'cheddar cheese')
sf.make_sandwich('cheddar cheese', 'mozzarella cheese', 'provolone cheese')
# # # 
from sandwich_functions import *

make_sandwich('ham', 'salami', 'pepperjack cheese')
make_sandwich('turkey', 'mayo', 'cheddar cheese')
make_sandwich('cheddar cheese', 'mozzarella cheese', 'provolone cheese')