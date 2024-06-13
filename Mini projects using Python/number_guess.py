import random

top_of_range = input("Enter a positive number: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
else:
    print("Please enter a number")
    quit()

random_num = random.randint(0,top_of_range)

guesses = 0
while True:
    guesses+=1
    num_guess = input("Guess a number ")
    if num_guess.isdigit():
        num_guess=int(num_guess)
    else:
        print("Please enter a number")
        continue

    if num_guess == random_num:
        print("You guess it right")
        break
    elif num_guess < random_num:
        print("Your guess should be bigger")
    else:
        print("Your guess should be smaller")

print("You guessed in",guesses, "guesses")