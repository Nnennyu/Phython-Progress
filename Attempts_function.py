'''
def favorite_book(book_title):
    """To display a message about my favorite book"""
    print("One of my favorite books is ", book_title.title())
    
favorite_book("pearl in wonderland")

#exercise 1
def make_shirt(size, text):
	""" To display and any message on a shirt"""
	print("I have made a UK size " + size + "  shirt for you.")
	print("The " + text.title() + " message on it is so deep and cute")

make_shirt("14", "'hard work pays'")
print("-------------------------------")
make_shirt(size="14", text="'hard work pays'")

#exercise2
def make_shirt(size="large", text="'i love python.'"):
	print()
	print("The message on my ", size, " size T-shirt is", text.title())
	
	
make_shirt()#because the two parameters are on default
make_shirt(text="'make money work for you.'")
make_shirt(text="'make money work for you.'", size="medium")
	
'''
'''
#exercise
def make_album(artist_name, album_title, no_Of_tracks=""):
	 to display a message about an artist an/d name of their song'''
'''
	music_album = {"name": artist_name, "title": album_title}
	if no_Of_tracks:
		music_album["no_Of_tracks"] = no_Of_tracks
	return music_album
music = make_album("Simi", "Duduke", 7)
print(music)


#excercise
def make_album(artist_name, album_title, no_Of_tracks=""):
	'''# to display a message about an artist an/d name of their song'''
'''
	music_album = {"name": artist_name, "title": album_title}
	return music_album
	
while True:
	print("\nPlease enter artist name and album title")
	print("(enter \'q' at any time to quit)")
	name = input("Enter artist name : ")
	if name.lower() == "q" :
		break
	title = input("Enter album title : ")
	if title.lower() == "q" :
		break
	music = make_album(name, title)
	print(music)
	
'''
#exercise pg187
def make_sandwich(*fillings):
	'''Summarize the content of a sandwich being requested'''
	print("\nMaking a sandwich with the following filling/s:")
	for filling in fillings:
		print("-", filling.capitalize())
		
order1 = make_sandwich('cheese', 'tomatoes')
order2 = make_sandwich('tuna', 'egg', 'mayonnaise')

#excercise
def build_profile(first, last, **other_info):
	'''To build a profile of myself'''
	profile = {}
	profile['first_name'] = first.capitalize()
	profile['last_name'] = last.capitalize()
	for key, value in other_info.items():
		profile[key] = value
	return profile
	
my_info = build_profile('nnennaya', 'ihekwoaba',
						age=30,
						location='london',
						field='devops engineering')
print("My profile is as follows :", my_info)
						
#exercise
def make_car(manufacturer, model_name, **other_info):
	'''a dictionary that shows a car's information'''
	info = {}
	info['brand'] = manufacturer
	info['model'] = model_name
	for k, v in other_info.items():
		info[k] = v
	return info
car = make_car('toyota', 'v-boot', color='blue', tow_package=True)
print("\nCar :", car)
