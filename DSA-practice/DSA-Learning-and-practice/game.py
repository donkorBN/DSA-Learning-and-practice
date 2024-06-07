# asks for an input
# generates random value
# compares input to generated value
import random

initialQuery = input("Can you guess the number I'm thinking of?")

response = initialQuery.lower()

if response == 'y' or response == 'yes':
    print("Okay then, let's see if you're smart")


else:
    print("Get out of here, sucker!!!!!")
    
secret_number = random.randint(1, 100)

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("You guessed it right!")
else:
    print(f"Nope, the number was {secret_number}")

tryAgain = input("Do you want to try again?  Yes/No")

def guessFunction():
    secret_number = random.randint(1, 20)
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("You guessed it right!")
    else:
        print(f"Nope, the number was {secret_number}")

if tryAgain.lower() == 'yes' or tryAgain.lower() == 'y':
    guessFunction()

else:
    print("END !")    