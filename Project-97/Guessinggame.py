import random
randomNumber = random.randint(1,9)
#print(randomNumber)
chance = 5
while chance>0:
    Guessnumber = int(input("Enter your guess"))
    if Guessnumber == randomNumber:
        print("You won the game")
        break
    if Guessnumber < randomNumber:
        print("Your Guess is low Guess a higher number")  
    else :
        print("your Guess is high Guess a lower number")
    chance = chance-1
    if chance == 0:
        print(You lose the game)