#List
'''
cars = ["honda", "toyota", "vaulks", "ferrari", "BMW"]
print("List of Cars = ", cars, end=" ")
print("\n-------cars varriables; usage in a statement------")
print("\nI wish i can drive the latest", cars[-2].title(), "car in town")
print("but i already own one" + " " + cars[1] + " " + "sports car")


#To add elements to an empty list
myKids = []
myKids.append("Pearl")
myKids.append("emerald")
myKids.append("Ruby" )
print(myKids)
print(myKids.insert(-1, "John"), myKids)
kids = ['Pearl', 'emerald', 'Ruby']
print(kids.insert(0, "Golden"), kids)
print()
x = kids.pop(2)
y = kids.remove("Golden")
print(kids)

money = ["naira", "euro", "british pound", "dollar"]
print(money.sort(), money)# sort() function re-arranges the contents permanently
print(money.sort(reverse=True), money)#Or use reverse
#print(money.reverse(), money)
print()
print("This is the new permanent list :", money)
print("\nThis is a sorted list :", sorted(money))


#working with list in a loop
cars = ["honda", "toyota", "vaulks", "ferrari", "BMW"]
for car in cars:
    print("Welcome! " + car.title() + " is available")
    print("\nHello, ", car.title(), "is such a delight to buy.")

print(cars[0].title(), " : This is the only brand we have in store \
with \'Zero milleage' ")


digits = []
for value in range(2, 21, 2):  #To get only even numbers from 1 to 20,
    digits.append(value**2)
print(digits)
print(max(digits))
print(list(range(1, 10, 2)))  #prints odd numbers between 1 and 10

#To slice through a certain number in a loop e.g
players = ['charles', 'martina', 'michael', 'florence', 'eli']

for player in players[:3]:# This loop only runs through the first three elements
    print(player.title())

#Other example:
#Generate a list for the first 10 cubes . also output the values of last 4 cubes, NB: cube of 4 = 4 ** 3

cubes = []
for eachnumber in range(10):
    cubes.append(eachnumber ** 3)
print(cubes)

for cube in cubes[-4:]:
    print(cube, end=" ,")
print("\nBye")

#To copy a list while maintaining the old list. we use only index([:]). eg
food_menus = ["eba", "Egusi", "fufu", "bitter leaf", "pepper soup"]
my_foods = food_menus[:]

print("My food menus = ", food_menus)
print()
print("My favourite foods are : ", my_foods)
print(my_foods.append('Rice'), my_foods)

'''
'''
#If conditional statement
players = ['charles', 'martina', 'michael', 'florence', 'eli']
player = "Uzoma"
play_list = ["joy", "ronado"]
if player in players:
    print(player.title(), "Welcome!, you are already one of us")
else:
    print(player.title(), ",you are not among our players")

if play_list not in players:
    print(play_list[0].title(), "and", play_list[1].title(),
          "welcome! both of can join our team")'''
'''
#example
favourite_fruits = ["banana", "apple", "pear"]
if 'banana' in favourite_fruits:
    print("You really like \'Banana'")
if 'berries' in favourite_fruits:
    print("You really like \'Berries'")
if 'apple' in favourite_fruits:
    print("You really like \'Apple'")

#To print all the contents in a list
for each_fruit in favourite_fruits:
    print(each_fruit, "is available")


#To confirm an empty list
fruits = []
if fruits:
    for each_fruit in fruits:
        print(each_fruit, "is available")
else:
    print("No fruit is available")

'''

'''
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list,
such as 1st or 2nd . Most ordinal numbers end in th, except 1, 2, and 3 .
store and loop through a list of numbers 1 to 9 '''

numbers = []
for digit in range(1, 10):
    if digit == 1:
        term = "st"
    elif digit == 2:
        term = "nd"
    elif digit == 3:
        term = "rd"
    else:
        term = "th"
    numbers.append(str(digit) + term)
print(numbers)

#To print out the elements of a list and its position
players = ['charles', 'martina', 'michael', 'florence', 'eli']

for index, player in enumerate(players, start=1):
    print(index, player.title())

#To compare two list at thesame time

players = ['charles', 'martina', 'michael', 'florence', 'eli']
cars = ["honda", "toyota", "vaulks", "ferrari", "BMW"]

for player, car in zip(players, cars):
    print(player.casefold(), car.upper())