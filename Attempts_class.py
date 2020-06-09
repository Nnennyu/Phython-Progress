#HOW TO IMPORT CLASS MODULES
from car import ElectricCar

new_car = ElectricCar("ford", "m21", 2021)
print("My new car is :", new_car.descriptive_name())
print("-----------------------------")

#Importing multiple Classes from a Module
from car import Car, ElectricCar

my_vaulks = Car("vaulks", "chasis", 2015)
print(my_vaulks.descriptive_name())

new_car = ElectricCar("ford", "m21", 2021)
print("My new car is :", new_car.descriptive_name())
print("-----------------------------")

#To import all Classes in a module(eg in car.py)
from car import *  #Though not usually recommended

#To import an Entire module(eg car.py)
import car

#page 216 - importing a module in a module eg.
from car import  Car
from pizza import make_pizza

#exercise pg 199
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize restaurant_name and cuisine_type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title(), " is an affordable nice restaurant.")
        print("It is an/a", self.cuisine_type.title(), "restaurant")

    def open_restaurant(self):
        print(self.restaurant_name.title(), " is now open for deliveries.")

    def get_number_served(self):
        '''showing number of customers served'''
        print("They serve approximately a total of ",
              str(self.number_served), " in a day.")
    def set_nunber_served(self, t_number_s):
        '''To be able to set the number of customers served'''
        self.number_served = t_number_s
    def increment_number_served(self, increment):
        '''Summarize each day with any additional orders'''
        self.number_served += increment

'''
eatery = Restaurant("nandos", "indian")
print("My family and I are eating out at ", eatery.restaurant_name.title(), "!")
eatery.describe_restaurant()
eatery.open_restaurant()


#exercise
eatery = Restaurant("fish and chips", "english")
eatery.describe_restaurant()
eatery.get_number_served()

print("--------------------------------------------")
eatery.number_served = 25
eatery.get_number_served()

print("-------------------------------------")
eatery.set_nunber_served(30)
eatery.get_number_served()

eatery.increment_number_served(7)
eatery.get_number_served()
'''

#excercise pg204
class User():
    '''Generating personal details of my website users'''
    def __init__(self, first_name, last_name):
        '''Initializing user's names'''
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        '''showing information about a user'''
        profile = self.first_name + " " + self.last_name
        return profile.title()

    def greet_user(self):
        '''send a greeting to each user'''
        print("Hi ", self.first_name.title(),
              self.last_name.title(), "Welcome!")

    def increment_login_attempts(self, increment=1):
        self.login_attempts += increment
        attempts_message = "You have made " + str(self.login_attempts) +\
                           " login attempts"
        print(attempts_message)

    def reset_login_attempts(self):
        if self.login_attempts >= 1:
            self.login_attempts = 0
            print("Login attempts resets to : ", self.login_attempts)

#web_user = User("mike", "chukwuemeka")
#web_user.describe_user()
#web_user.greet_user()

#web_user = User("pearl", "ihekwo")
#web_user.greet_user()
#web_user.increment_login_attempts()
#print("--------------------------------------")
#web_user.reset_login_attempts()

#Excercise 9-6 (pg211)
class IceCreamStand(Restaurant):
    '''This inherits the Restaurant class attributes'''

    def __init__(self, restaurant_name, cuisine_type):
        """Initializing attributes to describe an IceCreamStand. """
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = []

    def display_flavors(self, *flavours):
        """Method that displays the ice cream flavors"""
        for each_flavour in flavours:
            F = each_flavour.title()
            self.flavor.append(F)
        print("The available Ice Cream flavors are: ", self.flavor)


#my_iceOrder = IceCreamStand(restaurant_name="Taste and see", cuisine_type="italian",)
#my_iceOrder.describe_restaurant()
#my_iceOrder.display_flavors("vanilla", "strawberry", "chocolate")

#Exercise 9-7 (pg211)
class Admin(User):
    '''Information about a special form kind of User'''
    def __init__(self, first_name, last_name):
        """Initializing the attributes of the Admin"""
        super().__init__(first_name, last_name)
        self.privilege = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """To display the privileges of the Admin"""
        print("\nThe Admin has the following privileges :", self.privilege)

the_admin = Admin("nnennaya", "")
print(the_admin.describe_user())
the_admin.show_privileges()

#Exercise 9-8(pg211)
class Privileges():
    '''This is a seperate privilege class'''
    def __init__(self, *privileges):
        '''Initializing the attributes of the privileges'''
        self.privileges = privileges

    def show_privileges(self):
        '''To display the privileges of an admin'''
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        print(self.privileges)
        return self.privileges

    def update_privileges(self, *new_p):
        for privilege in new_p:
            self.privileges.append(privilege.capitalize())
        print(self.privileges)

class Admin(User):
    '''Information about a special form kind of User'''
    def __init__(self, first_name, last_name):
        """Initializing the attributes of the Admin"""
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

the_admin = Admin("pearl", "james")
print(the_admin.describe_user())
the_admin.privileges.show_privileges()
the_admin.privileges.update_privileges("can edit post", "can respond to enquiries")


