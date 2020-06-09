'''
count = 0
total_score = 0
test_score = 0

while test_score != 999:
    test_score = int(input("Enter test score : "))
    if test_score >=0 and test_score <= 100:
        total_score += test_score
        count += 1
        average_score = round(total_score / count)
        print("Total Score: " + str(total_score)
            + "\nAverage Score: " + str(average_score))
        #one can continue the line of codes in another line after ),},} or any sign like +, - etc
        # OR use \ to divide anywhere on the line


#A program to find the average of 3 test scores from the user
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("==========================================")

total_score = 0
total_score += int(input("Enter test score :\t\t"))
total_score += int(input("Enter test score :\t\t"))
total_score += int(input("Enter test score :\t\t"))

average_score = round(total_score / 3)
print("============================================")
print("Total Score: ", total_score,
      "\nAverage Score: ", average_score)
print()
print("Bye")
'''

#A nested loops that calculates the total of 3 valid test scores
total_score = 0
for i in range(3):
    while True:
        score = int(input("Enter test score :\t"))
        if score >=0 and score <=100:
            total_score += score
            break
        else:
            print("Test score must be from 0 to 100")
print("Total score:\t", total_score)

