import random
playing=True
number = str(random.randint(10,20))
print("Lets play a game i generate a random number from 1 to 10 and you have to guess it")
print("The game ends when you get 1 hero")
guess=input("give me your best guess/n")
if guess==number:
    print("You won the game")
else:
    print("OPPS!try again")