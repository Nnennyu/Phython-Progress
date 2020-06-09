'''

#To open files stored in same folder as this current file or window
file_object = open("filename.txt")
content = file_object.read()
print(content)
file_object.close()
'''

#You can open any file in your computer by quoting the FILE PATH
#file_object = open("C:\Users\nnenn\other_files\text_files\filename.txt")

#example
file_object = open("C:/Users/nnenn/OneDrive/Documents/python_works/pearlly.txt")
#Another Example
#file_object = open("C:/Users/nnenn/PycharmProjects/Personal_trial_projects/myfile.txt")
content = file_object.read()
print(content)
file_object.close()

print("----------------------------Bye---------------------------")
#READING LINE BY LINE
#To enable python to open and close our file automatically, we use "with" syntax
#Example

filename = "C:/Users/nnenn/OneDrive/Documents/python_works/pearlly.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip()) #rstrip function removes extra blank lines/spaces


#MAKING LIST OF LINES from a File
'''When you use with, the file object returned by open() is only available inside the with block
 that contains it. If you want to retain access to a file’s contents outside the with block, 
 you can store the file’s lines in a list inside the block and then work with that list. 
 You can process parts of the file immediately and postpone some processing for later in the program.'''

filename = "C:/Users/nnenn/PycharmProjects/Personal_trial_projects/integers.txt"

with open(filename) as file_object:
    lines = file_object.readlines() #readlines() helps to store file_object in a list called "line" and can be used later

#Eg
integer_strings = ""     #Python interpretes all text in a file as string, you can convert it using int or float function
for line in lines:
    integer_strings += line.rstrip()
print(integer_strings[:50] + "...") #to print the first 50 items
print("Total number of integers :", len(integer_strings))


# iS YOUR BIRTHDAY CONTAINED IN 'integers.txt'
filename = "C:/Users/nnenn/PycharmProjects/Personal_trial_projects/integers.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

integer_strings = ""
for line in lines:
    integer_strings += line.rstrip()

#birthday = input("Enter your birthday, as dd mm yy :")
#if birthday in integer_strings:
    #print("Your birthday was found in the 500 first random integers")
#else:
    #print("Birthday not found")
print("------------------------Bye-------------------------")


#WRITING TO A FILE
'''You can open a file in read mode ('r'), write mode ('w'), 
append mode ('a'), or a mode that allows you to read and write to the file ('r+') '''

#'w' mode creates a new file if it does not exist but erases and replaces the contents of the file if it exist

filename = "programing.txt"
with open(filename, 'w') as file_object:
    file_object.write("I love programing.\n")
    file_object.write("I love creating new games.\n")

#APPENDIND A FILE,
# 'a' mode creates a new file if it does not exist. It adds to the end of the file if the file exist
# and does not erase the original content of the file

filename = "programing.txt"

with open(filename, 'a') as file_object: #Note 'r+' mode will output only the new entries.
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating Apps that can run in a browser.\n")

#READING A FILE
filename = "programing.txt"

with open(filename, 'r') as file_object:
    contents = file_object.read()
print(contents)
print("------------------Bye to files----------------------------")

