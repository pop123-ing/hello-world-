import random

#generate a random number between 0 and 100
random = random.randint(0, 100)

print("guess a number between 0 and 100")

#prompt the user to guess a number
guess = int(input("Enter your guess: "))

if guess == random:
    print("Yes the number is " + str(random))
elif guess > random:
    print("Your guess is too high")
else:
    print("Your guess is too low")