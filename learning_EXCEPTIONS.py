
#Using Try-Except Blocks
"""You tell Python to try running some code, and you tell it what to do
if the code results in a particular kind of exception. """

#Eg
#print(5/0)
#Note it will raise a 'ZeroDivisionError' because python cannot process any division by zero
#Using try-Except block we have

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")

print("-------------------Bye-------------------------")
#Using Exceptions to prevent a program from crashing Eg a simple calculator
'''
print("Give me two numbers, i will divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number :")
    if first_number.lower() == 'q':
        break
    second_number = input("\nSecond number :")
    if second_number.lower() == 'q':
        break
    answer = int(first_number) / int(second_number)
    print("Answer = ", answer)
print("---------------------------End-------------------------------")
'''

"""The above calculator will work until the user inputs 0, which will crash.
The 'ZeroDivisionError' trace back it raises exposes your program to hacker.
 To rectify the above, we use ELSE BLOCK"""

#ELSE BLOCK
#You put try- except commmand on the line of code likely to raise an error.
'''
print("Give me two numbers, i will divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number :")
    if first_number.lower() == 'q':
        break
    second_number = input("\nSecond number :")
    if second_number.lower() == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError :
        print("You can't divide by '0'")
    else:
        print("Answer = ", answer)
print("---------------------------End-------------------------------")
'''

#HANDLING THE FileNotFoundError EXCEPTIONS page 236
filename = "alice.txt"
try:
    with open(filename) as f_obj:
        contents = f_obj.read()

except FileNotFoundError:
    msg = "Sorry the file " + filename + " does not exist."
    print(msg)
else:
    #else will run only when the file is stored in same folder as this
    #count the approximate number of words in a file
    words = contents.split() #split() slices each word in string and stores them in a list
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
print("-------------------------Bye--------------------------")


#ANALYSING A FILE
#Example to count how many words are in a file.

filename = "text_files/zuuuk.txt"

try:
    with open(filename) as file_object:
        contents = file_object.read()

except FileNotFoundError:
    print("Sorry the file " + filename + " does not exist.")
else:#count approximate number of words in a file
    eachword = contents.split()
    num_words = len(eachword)
    print("The file " + filename + " has about " + str(num_words) + " words.")
print("------------------------End------------------------------")



#WORKING WITH MULTIPLE FILES
"""Its best to create a function that analysis one file and use it to analyse multiple files"""

def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        print("Sorry the file " + filename + " does not exist.")
    else:  # count approximate number of words in a file
        eachword = contents.split()
        num_words = len(eachword)
        print("The file '" + filename + "' has about " + str(num_words) + " words.")

filename = "text_files/zuuuk.txt"
count_words(filename)

#Eg2
myBooks = ["text_files/muuk.txt", "text_files/buuuk.txt", "alice.txt", "text_files/guuuk.txt"]
for eachBook in myBooks:
    count_words(eachBook)
print("-----------------------------------------------------")

#FAILING SLIGHTLY( using 'pass' command, the user does not get a feedback.)


def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        pass

    else:  # count approximate number of words in a file
        eachword = contents.split()
        num_words = len(eachword)
        print("The file '" + filename + "' has about " + str(num_words) + " words.")
#eg
myBooks = ["text_files/muuk.txt", "text_files/buuuk.txt", "alice.txt",
           "text_files/guuuk.txt", "integers.txt"]
for eachBook in myBooks:
    count_words(eachBook)
