'''#IMPORTING AN ENTIRE MODULE and functions
"""A module is a file saved in this form 'module_name.py'
To import a function in a module, you first import the module,
 before calling the function you need like ' module_name.function_name()' """
#eg
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'bacon', 'extra cheese')
'''

#IMPORTING SPECIFIC FUNCTIONS
"""we use 'from module_name import function_name' 
multiple functions can be imported and separated with a comma as follows:
'from module_name import function_0, function_1, function_2' 
finally, you only make use of the 'function_name()' in your new code """
#eg
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'bacon', 'extra cheese')

#you can import modules by giving alias
#eg : import pizza as p
# p.make_pizza(...)

#TO IMPORT ALL FUNCTIONS IN A MODULE, USE *
#eg:
#from pizza import *
#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushroom', 'bacon', 'extra cheese')
