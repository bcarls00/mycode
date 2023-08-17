#!/usr/bin/python3
"""Alta3 Research | RZFeeser
  Conditionals - Life of Brian guessing game without a while True loop."""

round = 0
answer = " "

while round < 3 and answer != "Brian":
    round += 1     
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ').title()
    if answer == "Brian":
        print("Correct!")
    elif answer == "Shrubbery":
        print("You guessed the super secret answer!")
        break
    elif round == 3:    
        print("Sorry, the answer was Brian.")
    else:                 
        print("Sorry. Try again!")

