name = "emerald ihekwoaba"
print(name.title())
'''

food_menu = {'main_meal':'stew_rice', 'dessert':'ice_cream'}
print(food_menu["dessert"])

food_menu['appetizer'] = 'lentil_soup'
food_menu["snack"] = "pop_corn"
print(food_menu)


#ADDING TO AN EMPTY DICTIONARY
food_menu = {}
food_menu['appetizer'] = 'lentil_soup'
food_menu["snack"] = "pop_corn"
food_menu['main_meal'] = 'stew_rice'
food_menu['dessert'] = 'ice_cream'
print(food_menu)

for food in food_menu:
    print(food)

#TO USE ONE ELEMENT OF A DICTIONARY TO MODIFY ANOTHER ELEMENT
invader = {'colour' : 'yellow', 'x_position' : 0, 'y_position' : 25, 
    'speed' : 'medium', 'mass_kg' : 32}

if invader['speed'] == 'slow':
    x_increment = 1
elif invader['speed'] == 'medium':  
    x_increment = 2
elif invader['speed'] == 'fast':
    x_increment = 3
invader['x_position'] += x_increment

print("New x-position is = ", str(invader['x_position']))


person = {
    'first_name' : 'pearl', 
    'last_name' : 'Ihekwoaba', 
    'age' : 4,
    'city' : 'london',
    'colour' : 'brown'
    }
print(person)
del person['colour']
print("\nNew person", person)

#TO ACCESS EVERY INFORMATION ABOUT A USER IN A WEBSITE
for key, value in person.items():
    print("\nKey : ", key, "\nValue : ", value)
    
#TO LOOP THROUGH ONLY THE KEY ELEMENTS, WE USE 'key()'
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for k in favorite_languages.keys():
	print("\nThe Key elements are : ", k.title())
'''
'''
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	'peal': 'c',
	}

friends = ["edward", "phil"]

for name in favorite_languages.keys():
	print( name.title())
	if name in friends:
		print("Hi", name.title(),
		 " I am so glad to know that your favourite language is", 
		 favorite_languages[name])

if "john" not in favorite_languages.keys():
	print("John, please state your preffered language")
	
#SORTING THE DICTIONARY
for k in sorted(favorite_languages.keys()):
	print(k.title(), " : in ascending order")
	
#TO PRINT ONLY THE VALUES OF KEY ELEMENTS
#for v in favorite_languages.values():
for v in set(favorite_languages.values()): # set prevents repition of values
	print("My specialty is : ", v.title())
'''
'''
#NESTING THROUGH A SET OF THREE DICTIONARIES example
alien_0 = {'colour': 'green', 'points': 5}
alien_1 =  {'colour': 'yellow', 'points': 10}
alien_2 =  {'colour': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)
print("-------------Bye----------------")

	
#generating informations about so many aleins example 30 aliens and outputing only 5

aliens = []
for no_of_aliens in range(30):
	each_alien = {'colour': 'red', 'points': 5, 'speed': 'slow'}
	aliens.append(each_alien)
	
# to show only the first five aliens
for alien in aliens[:5]:
	print(alien)
print()
print("The total no of aliens created = ", str(len(aliens)))
	
#to modify the first three aliens
for alien in aliens[:3]:
	if alien['colour'] == 'red':
		alien['colour'] = 'green'
		alien['points'] = 10
		alien['speed'] = 'medium'
	elif alien['colour'] == 'green': # further moderations (not included)
		alien['colour'] = 'blue'
		alien['points'] = 15
		alien['speed'] = 'fast'
#to show the first five aliens
for alien in aliens[:5]:
	print(alien)
print("--------Above is the updated first five aliens -----------")
'''
	
#LIST INSIDE A DICTIONARY eg
pizza = {
	'crust': 'thick',
	'toppings': ['mushroom', 'extra cheese'],
	}
print("You ordered a " + pizza['crust'] + "-crust pizza " + " with the following toppings")
for topping in pizza['toppings']:
	print(topping) 
	
pizza['toppings'].append('bacon')#to add more elements to the list 'toppings'
print(pizza)

#Another example
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'c#'],
	'phil': ['python', 'java'],
	}
for k, L in favorite_languages.items():
	print("\n", k.title(), " favorite languages  :")
	#for language in L:
		#print("\t", language.title())
	for language in L:
		if len(language) == 1:
			print("is", language.title())
		else:
			print("are", language.title())	

#DICTIONARY IN A DICTIONARY
users = {
	'nenyu':{
		'first_name': 'nnenna',
		'last_name': 'uka',
		'location': 'aba',
		},
	'Pearly': {
		'first_name': 'pearl',
		'last_name': 'ihekwoaba',
		'location': 'london',
		},
	}

for username, user_info in users.items():
	print("\nUsername : ", username)
	full_name = user_info['first_name'] + " " + user_info['last_name']
	location = user_info['location']
	print("\tFull name :", full_name.title())
	print("\tLocation : ", location.title())
	


	
