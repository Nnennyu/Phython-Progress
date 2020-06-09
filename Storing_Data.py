
'''json means javascript object notation'''
"""The json module allows you to dump simple Python data structures into a file and load the data 
from that file the next time the program runs. You can also use json to share data between 
different Python programs. Even better, the JSON data format is not specific to Python, so you can
 share data you store in the JSON format with people who work in many other programming languages"""

#USING json.dump() and json.load()
'''json.dump() - stores the data while json.load() - saves the data to memory'''

#Eg
import json

numbers = [2, 3, 5, 6, 8, 11]

filename = "numbers.json"
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)
print("------------------End---------------------")

import json

f_name = "numbers.json"
with open(f_name) as f_object:
    numbers = json.load(f_object)
print(numbers)
#NOTE, The above is a simple way to share data between two programs


#SAVING AND READING USER-GENERATED DATA
"""If you don't store your user's data, you will loose it, when the program stops running. 
Example : lets store a user's name when the login for the first time"""

import json

username = input("Enter your Name :")
filename = "username.json"

with open(filename, 'w') as file_object:
    json.dump(username, file_object)
    print("W'll remember you when \;llomkv\you come back", username)


import json

filename = "username.json"
with open(filename) as file_object:
    username = json.load(file_object)
    print("Welcome back " + username.title() + "!")