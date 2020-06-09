#calling a fucction, you do not put any thing in the parenthesis
'''def greet_user():
    """Display a simple greeting"""
    print("Hello! Dearest")

greet_user()

#passing information to fuction
def greet_user(username):
    """Display a simple greeting"""
    print("Hello! Dearest", username.title())

greet_user('emerald')

#Positional arguments
def describe_pet(animal_type, pet_name):
    """To display information about a pet"""
    print("\nI have a ", animal_type, " as my pet")
    print("My " + animal_type + "'s name is ", pet_name.title())
describe_pet("parrot", "henry")
describe_pet("dog", "big jack")

#Keyword arguments helps one not to misplace parameters :example
describe_pet(animal_type="cat", pet_name="storm")
describe_pet(animal_type="dog", pet_name="duduke")

#Default values(you can set one parameter of the function to a default, such that
# when a defined function calls and that particular parameter is empty, it automatically
# picks the the default value assigned to it.)

def describe_pet(pet_name, animal_type="dog"): #The default parameter should not be at the begining
    """To display information about a pet"""
    print("\nI have a ", animal_type, " as my pet")
    print("My " + animal_type + "'s name is ", pet_name.title())

describe_pet(pet_name="willie")
describe_pet(animal_type="sheep", pet_name="bingo")
'''
'''
#Returning a function
def paste_name(first_name, last_name):
    """Return a function full_name"""
    full_name = first_name + " " + last_name
    return full_name.title()
pupil_1 = paste_name("nnenny", "sky")
print(pupil_1)

#making an argument optional, you assign an empty string to it
def paste_name(first_name, last_name, middle_name=""):
    """Return a function full_name"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()
pupil_1 = paste_name("nnenny", "uka", "sky")
print(pupil_1)

#returning a Dictionary
def build_person(first_name, last_name, age="", occupation=""):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    elif occupation:
        person['occupation'] = occupation
    return person
survivor = build_person("Emerald", "Ihekwoaba", occupation="Doctor")
print(survivor)
print("Bye")
'''
'''
#using a function in a while loop
def get_name(first_name, last_name):
    """Return full_name"""
    full_name = first_name + " " + last_name
    return full_name.title()
while True:
    print("\nPlease enter your full name")
    print("(enter \'q' at any time to quit.)")
    f_name = input("First Name : ")
    if f_name.lower() == "q":
        break
    l_name = input("Last Name : ")
    if l_name.lower() == "q" :
        break
    name = get_name(f_name, l_name)
    print("\nHello " + name + "!")
'''

#Passing a list to a function
def greet_user(names):
    '''display a simple greeting to every user'''
    for name in names:
        msg = "Hello " + name.title() + "!"
        print(msg)

usernames = ["ruby", "cosmas", "fire", "nneny", ]
greet_user(usernames)


#modifying a list
'''Consider a company that creates 3D printed models of designs that \
users submit. Designs that need to be printed are stored in a list, 
and after being printed they’re moved to a separate list'''
'''
unprinted_designs = ['iphone case', 'robot pendant', 'leggo bricks',]
completed_models = []
while unprinted_designs:
    current_designs = unprinted_designs.pop()
    print("Printing model : ", current_designs)
    completed_models.append(current_designs)

print("\nThe following models have been printed :")
for each_model in completed_models:
    print(each_model)
'''
'''
#The above code can be reorganized using 2 functions
def printing_models(unprinted_designs, completed_models):
    """    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.    """
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print("Printing model : ", current_designs)
        completed_models.append(current_designs)

def show_completed_models(completed_models):
    print("\nThe following models have been printed :")
    for each_model in completed_models:
        print(each_model.capitalize())

#example of how to use the above
unprinted_designs = ["android battery", "school bags", "zoom sign-post",]
completed_models = []
printing_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#eg2
project1 = ['white board', 'souvenir', 'book cover', 'suit case']
finished_projects1 = []
printing_models(unprinted_designs=project1, completed_models=finished_projects1)
show_completed_models(finished_projects1)
'''
'''
#NOTE: one can pass a copy of the list(using [:]) while creating a function
def printing_models(unprinted_designs[:], completed_models): '''

'''
#PASSING AN ARBITRARY NUMBER OF ARGUMENTS using (*)
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("Your pizza is ready wity the following topping/s : ", toppings)

make_pizza('pepperoni')
make_pizza('mushroom', 'bacon', 'extra cheese')
'''
'''
#eg2
def make_pizza(*toppings):
    """ Summarize the pizza we are to make."""
    print("\nMaking a pizza with the following toppings :")
    for topping in toppings:
        print("- ", topping)

make_pizza('pepperoni')
make_pizza('mushroom', 'bacon', 'extra cheese')
'''
#eg3
def make_pizza(size, *toppings):
    """ Summarize the pizza we are to make."""
    print("\nMaking a " + str(size) + "-inch size pizza with the following toppings :")
    for topping in toppings:
        print("-", topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'bacon', 'extra cheese')

#USING ARBITRARYN KEY WORD ARGUMEBTS such as (**) allows any no of key:value pairs in a dictionary  eg
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('nnennaya', 'ihekwoaba',
                             location='london',
                             field='software engineer')
print(user_profile)

#IMPORTING AN ENTIRE MODULE and functions
"""A module is a file saved in this form 'module_name.py'
To import a function in a module is ' module_name.function_name()' """
