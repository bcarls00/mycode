#!/usr/bin/python3


def main():

    print("Hello, your name is Terry, you are anti-social and you have been given the task to survive a day at the office! answer the prompts and try to survive!")
   
    a = input("You show up late to work and you boss is mad. wyd? \n 1. Walk away awkwardly \n 2. Deny it!\n 3. Distract with shiny object and slip away \n 4. Admit mistake and move on \n 5. Quit on the spot!")
    if a == "1":
        print("Your boss finds you and fires you.")
    elif a == "2":
        print("Your boss asks 'what do you mean?")
        a1 = input("1. 'I'm not even supposed to work today but am here becuase I'm awesome and have no work life balance.'\n 2. 'Im not late, YOU are late!'")
        if a1 == "1":
            print("Your boss appologizes and thanks you for being there.")
        elif a1 == "2":
            print("Your boss says you are fired!!")
            print("aw nuts")
        else:
            print("you didn't answer correctly and were fired :( ")
            
         


