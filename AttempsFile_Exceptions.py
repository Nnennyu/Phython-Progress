'''
#Exercise 10-4 pg 232 of 'Python Crash course'
filename = "guest_book.txt"

print("Please Enter your name.")
print("Continue with the names of your crew or enter 'q' to quit")

with open(filename, 'a') as file_object:
    guests = []
    while True:
        fullname = input("\nFull Name :")
        if fullname.lower() == 'q':
            break
        else:
            guests.append(fullname.title())
            message = ", Thank you for honouring our invitation. "
            guests.append(message)

    file_object.writelines(guests)
print(guests)

print("------------------------Bye----------------------")

with open(filename, 'r') as file_object:
    for line in file_object:
        print(line)
'''
'''
#Excercise10-6 pg240
"""To catch a TypeError bug from user input"""
print("Enter any two numbers, to produce the sum.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst Number :")
    if first_number.lower() == 'q' :
        break
    second_number = input("\nSecond Number :")
    if second_number.lower() == 'q':
        break

    try:
        num_sum = int(first_number) + int(second_number)
    except ValueError:
        print("Number must be an integer")
    else:
        print("The sum = ", num_sum)
'''

#Exercise 10-10 page 241
'''Use your count() method to analyse how many times a word appeared in a file '''

f_name = "text_files/buuuk.txt"

try:
    with open(f_name) as file_object:
        contents = file_object.read()

except FileNotFoundError:
    print(f_name, " does not exist")
else:
    #To count number of times a word appears in the file
    words = contents.split()
    num_words = words.count("the")
    print(f_name + " : " + str(num_words))





