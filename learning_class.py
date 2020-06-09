#Classes are used to represent real_word situations
#CREATING A CLASS
'''eg creating a dog class that stores name and age, and each dog will have ability to
sit() and roll_over() '''

class Dog():
    """A simple attempt to model a dog."""
    def __init__(self, name, age):   #__init__ is method class uses
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self): #NB sit(self) and roll_over() are attributes of class Dog
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
'''
#eg Making an instance from a class
#To access attributes, we use '.' eg my_dog.name
my_dog = Dog("bingo", 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

#Calling methods stil uses '.'
my_dog.sit()
my_dog.roll_over()
print("-------------------end---------------------")
'''
#Creating Multiple Instances
'''You can create as many instances from a class as you need.
 Let’s create a second dog called your_dog: ''''''
my_dog = Dog("jack", 7)
your_dog = Dog("willie", 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.roll_over()

'''
#eg
class Car():
    '''A simple attempt to represent a car.'''
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year ) + " " + self.make + " " + self.model
        return long_name.title()
'''
my_new_car = Car("honda", "camry", 2013)
print(my_new_car.descriptive_name())'''

#modifying and adding a new method to the existing eg its changing milleage
class Car():
    '''A simple attempt to represent a car'''
    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriptive_name(self):
        '''Return a neatly formated descriptive name'''
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        '''Show a message displaying the car's odometer'''
        print("This car has ", str(self.odometer_reading), " miles on it")
'''
my_new_car = Car("vaulks", "chasis", 2009)
print(my_new_car.descriptive_name())
my_new_car.read_odometer()

#METHODS OF CHANGING ATTRIBUTES
#eg1 by modifying attribute value directly
my_new_car.odometer_reading = 0.56
my_new_car.read_odometer()'''

print("-------------------------------------")
#eg2 By modifying attribute value through a method
class Car():
    '''A simple attempt to represent a car'''
    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriptive_name(self):
        '''Return a neatly formated descriptive name'''
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        '''Show a message displaying the car's odometer'''
        print("This car has ", str(self.odometer_reading), " miles on it")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.        
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading :
            self.odometer_reading = mileage
        else:
            print("You can't roll it back")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
'''
my_new_car = Car("BMW", "a4", 2019)
print(my_new_car.descriptive_name())

my_new_car.update_odometer(1500)
my_new_car.read_odometer()

my_new_car.increment_odometer(52)
my_new_car.read_odometer()
'''

#INHERITANCE
# #takes up methods and attributes of an existing class example
#to model an ELECTRIC car, we take up existing car class structure and add new features
#parent class must be in thesame file as the child class and must come before it

class ElectricCar(Car):
    """To represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car'''
        super().__init__(make, model, year)
        self.battery_size = 80

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

#my_tesla = ElectricCar('tesla', 'model s', 2016)
#my_tesla.descriptive_name()
#print(my_tesla.descriptive_name())
#my_tesla.describe_battery()

#NB one can over-ride a method in child class by re defining the same method in parent class
def update_odometer(self, mileage):
    """ eg Electric cars are not usually affected by mileage"""
    print("Mileage not usually affected because its battery.")


# NOTE also:
"""For example, if we continue adding details to the ElectricCar class,
 we might notice that we’re adding many attributes and methods specific to the car’s battery. 
 When we see this happening, we can stop and move those attributes and methods to a separate class 
 called Battery. Then we can use a Battery instance as an attribute in the ElectricCar class:"""

class Battery():
    """A simple attempt to model an Electric car' s battery"""
    def __init__(self, battery_size=80):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        '''Display a message about the car's battery size'''
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 80:
            range = 240
        elif self.battery_size == 90:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

#When done give it a call back in the original class eg

class ElectricCar(Car):
    """To represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car'''
        super().__init__(make, model, year)
        self.battery = Battery()

    def update_odometer(self, mileage):#I was just attempting the changes, i made before, so not necessary
        """ eg Electric cars are not usually affected by mileage"""
        print(self.model, str(self.year),"Mileage not usually affected because of its battery.")

my_toyota = ElectricCar("toyota", "s9", 2020)
my_toyota.descriptive_name()
print("Electric car info : ", my_toyota.descriptive_name())
my_toyota.battery.describe_battery()
my_toyota.update_odometer(1600)
my_toyota.battery.get_range()


#ORDERED DICTIONARY
"""In order to keep track of how the items in a dictionary are entered, 
we use OrderedDict class from the collections module eg."""

from collections import OrderedDict

favourite_language = OrderedDict() #OrderedDict class replaces  {}

favourite_language["pearl"] = "ruby"
favourite_language["edward"] = "c#"
favourite_language["peter"] = "cobol"
favourite_language["sunny"] = "python"

print("Favourite languages :", favourite_language)

for name, language in favourite_language.items():
    print(name.title(), language.title())
