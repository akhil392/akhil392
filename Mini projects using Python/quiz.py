print("Welcome to  computer Quiz")

playing= input("Do you want to play: ")
if playing.lower() == "yes":
    print("Lets play")
    print("NOTE: Spelling Mistakes are considered")
else:
    quit()

score = 0

answer = input("What is CPU stands for ? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer = input("Who is the father of computer ? ")
if answer.lower() == "charles babbage":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer = input("What is the full form of RAM ? ")
if answer.lower() == "random access memory":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer = input("In which year computer was invented ? ")
if answer.lower() == "1822":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer = input("What is ROM stands for ? ")
if answer.lower() == "read only memory":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer = input("What is PSU stands for ? ")
if answer.lower() == "power supply unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer = input("Computer understand only ______ language ")
if answer.lower() == "binary":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer = input("What is brain of computer ? ")
if answer.lower() == "central processing unit":
    print("Correct")
elif answer.lower() == "cpu":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer = input("USB stands for ")
if answer.lower() == "universal serial bus":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer = input("The third generation computer was made with____? ")
if answer.lower() == "integrated circuits":
    print("Correct")
    score+=1
else:
    print("Incorrect")

print("Your total score is " + str(score))