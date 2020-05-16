"""
Author: TheRealDarkCoder
Date: 17th May, 2020
"""


import random


def high_or_low(number, target):
    number = int(number)
    if number > target:
        return "high"
    elif number < target:
        return "low"
    else:
        return "win"

def config_difficulty(minimum, maximum, guesses, mode):
    config = [minimum, maximum, guesses, mode]
    return config

try:
    difficulty = int(input("Please enter the difficulty options:\n"
                   "[1]Easy Mode\n"
                   "[2]Medium Mode\n"
                   "[3]Hard Mode\n"
                   "[4]Custom\n"))
except:
    print("I didn't understand, please launch the game again.")
    exit()


if difficulty == 1:
    config = config_difficulty(0, 100, 7, "Easy")
elif difficulty == 2:
    config = config_difficulty(0, 100, 5, "Medium")
elif difficulty == 3:
    config = config_difficulty(0, 500, 6, "Hard")
elif difficulty == 4:
    try:
        custom_minimum = int(input("Please enter the minimum number:"))
        custom_maximum = int(input("Please enter the maximum number:"))
        custom_guesses = int(input("Please enter the number of guesses available to you:"))


        if custom_maximum <= custom_minimum:
            print("How can maximum be greater than minimum? Try again fool.")
            exit()

        if custom_maximum == 0 or custom_minimum < 0 or custom_guesses == 0:
            print("Your values don't make sense, try again!")
            exit()

        config = config_difficulty(custom_minimum, custom_maximum, custom_guesses, "Custom")
    except:
        print("You entered weird stuff, try again.")
        exit()
else:
    print("Please enter a value between 1 and 4 and try again!")
    exit()

minimum = config[0]
maximum = config[1]
guesses_left = config[2]


target = random.randint(minimum, maximum)

print("Playing in " + config[3] + " difficulty...\n\n")
print("Welcome to the game of High Low! We have guessed a number between " + str(minimum) + " and " + str(maximum) + ". Your job is to guess the number in " + str(guesses_left) + " chances! We'll give you hints in the way don't worry!")


while guesses_left > 0:
    guess = input("Guess the number! (Chances left: " + str(guesses_left) + ")")
    try:
        result = high_or_low(guess, target)
    except:
        print("You entered garbage, please guess a valid number")
        continue

    if result == 'high':
        print("Your guess is higher than our number! Try again!")
    elif result == 'low':
        print("Your guess is lower than our number! Try again!")
    else:
        print("The number is indeed " + str(target) + "! Congratz! You won!")
        exit()
    guesses_left = guesses_left - 1

print("Oops! Too bad you could'nt guess it! The number was " + str(target))
print("You were close by " + str(abs(int(target) - int(guess))))
