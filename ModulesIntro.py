#Learning Modules
import random

for value in range(5):
    print(random.randint(1,10))

#Guessing game using random function

correct = random.randint(1,100)
while True:
    guess_number = int(input('Enter your guess: '))
    if guess_number < correct:
        print("You guessed lower!")
    elif guess_number > correct:
        print("You guessed higher!")
    else:
        print("You won! Bye")
        break
    continue