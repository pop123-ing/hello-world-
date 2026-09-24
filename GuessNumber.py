import random

#generate a random number to be guessed
number_to_guess = random.randint(0, 100)

print("Guess the number between 0 and 100!")

guess = -1
while guess != number_to_guess:
    #prompt the user toguess the number
    guess = int(input("Enter your guess: "))
    if guess == number_to_guess:
        print("Congratulations! You guessed the number.")
    elif guess > number_to_guess:
        print("Too high")
    else:
        print("Too low")