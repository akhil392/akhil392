import random
user_score=0
com_score=0

options=["rock","paper","scissors"]

while True:
    user_input=input("Enter Rock/Paper/Scissors or q to Quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("Wrong pick")
        continue

    random_num=random.randint(0,2)
    comp_pick=options[random_num]
    print("computer pickes",comp_pick,"...")

    if user_input=="rock" and comp_pick=="scissors":
        print("You won:) ")
        user_score+=1
    elif user_input=="paper" and comp_pick=="rock":
        print("You won:) ")
        user_score+=1
    elif user_input=="scissors" and comp_pick=="paper":
        print("You won:) ")
        user_score+=1
    else:
        print("You lost :( ")
        com_score+=1

print("Your score is ",user_score)
print("Computer score is",com_score)
print("GoodBye!")