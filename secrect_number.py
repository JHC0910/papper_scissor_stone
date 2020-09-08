print('Hello!!')
print('What is your name?\n')
name = input()
import random
SNumber = random.randint(1,100)
SNumber = int(SNumber)
guessesTaken = 0
limit = 6
limits = str(limit)
print('\nHi, ' + name + '!')
print('I am thinking a number between 1 to 100.\n')
print('You have ' + limits + ' chances to guess it.\n')

while guessesTaken < limit:
    print("Let's have a guess.")
    guess = input()
    guess = int(guess)
 
    guessesTaken += 1
    if guess < SNumber:
        print("Your guess is too low, " + name + ".")
    if guess > SNumber: 
        print("Your guess is too high, " + name + ".")
    if guess == SNumber: 
       break 

if guess == SNumber:
    guessesTaken = str(guessesTaken)
    print("Congratulations!! " + name + "!!")
    print("You've done it in your " + guessesTaken + "-th try.\n")

else:
    SNumber = str(SNumber)
    print("You failed!! " + name + ".")
    print("The answer is " + SNumber + ".\n")
    print("Please try it again.\n")	
