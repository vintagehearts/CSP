import sys
import random
from art import logo
from art import bye 
from art import congratulations
from art import uhoh

def play():
    print("\033c")
    print(logo)
    play = str(input("Would you like to play? Type (y/n): "))
    if play == "y":
        guessNumber()
    else:
        print(bye)
        sys.exit(0)

def guessNumber():
    min_num = "1"
    max_num = int(input("Enter the maximum number: "))
    
    if 1 >= max_num:
        print("The maximum number must be greater than the minimum number . Please put a number greater than 1")
    answer = max_num

    secret_number =random.randint(1, max_num)
    attempts = 0

    while  True:
        print("Guess the secret number between 1 and", answer,":")
        guess = int(input(" "))
        attempts += 1
        if attempts == 5:
            print(uhoh)
            print("the secret number was", secret_number)
            again = str(input("Do you want to play again? Type: (y/n): "))
            if again == "y":
                guessNumber()
            else:
                sys.exit(0)
        elif guess < secret_number:
            print("Guess higher!") 

        elif guess> secret_number:
            print("Guess lower!")

        else: 
            print(congratulations)
            again = str(input("Do you want to play again? Type: (y/n): "))
            if again == "y":
                guessNumber()
            else:
                sys.exit(0)
play()


            
           
    




