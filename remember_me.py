"""A program to remember a user's username"""
"""We want to retrieve their username from memory if possible; therefore, we’ll start 
with a try block that attempts to recover the username"""
'''
#Load the username if it has been stored previously.
#otherwise, prompt for username and store it.
import json

filename = "username.json"
try:
    with open(filename) as file_object:
        username = json.load(file_object)

except FileNotFoundError:
    username = input("Enter your Name :")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
        print("Welcome back " + username.title() + "!")
else:
    print("W'll remember you when you come back", username)
'''

#REFACTORING
"""This is a way of making our codes look cleaner and smart."""
import json

def greet_user():
    """Greet user by name."""
    filename = "username.json"
    try:
        with open(filename) as file_object:
            username = json.load(file_object)

    except FileNotFoundError:
        username = input("Enter your Name :")
        with open(filename, 'w') as file_object:
            json.dump(username, file_object)
            print("Welcome back " + username.title() + "!")
    else:
        print("W'll remember you when you come back", username)
greet_user()
print("-------------------End----------------------------")

#Refactoring greet_user() function above into three functions, we have
import json

def get_stored_name():
    """Get stored username if available."""
    filename = "username.json"
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_user():
    """Prompt for a new user"""
    username = input("Enter your Name :")
    filename = "username.json"
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username


def greet_user():
    """Greet the user by name."""
    print("Is this your username? Answer 'y/n' ")
    username = get_stored_name()
    print(username)

    while True:
        prompts = input("Enter yes or No as 'y/n' :")
        if prompts.lower() == 'y':
            print("Welcome back " + username + "!")
            break

        if prompts.lower() == 'n':
            username = get_new_user()
            print("W'll remember you when you come back", username)
            break

greet_user()

