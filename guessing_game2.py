#!/usr/bin/env python3

# Created by Noah McCaskill
# Created May 2022
# This program is a number guessing game that contains while/break components.


import random


def main():
    # this function checks if a guess is correct, prompts the
    # the user to try again if it isn't, and counts tries.
    counter = 1

    # input
    answer = random.randint(0, 9) 
    answer = 4
    guess_string = input("Guess a number from 0 to 9: ")

    # process & output
    while True:
        try:
            guess = int(guess_string)
            if guess == answer:
                break
            elif guess > answer:
                print("\nThat number is too high!")
            elif guess < answer:
                print("\nThat number is too low!")
            else:
                print("\nSomething went wrong.")

        except Exception:
            print("\nSorry, that is not a valid integer.")

        guess_string = input("Try again: ")
        counter += 1

    # End of game output
    print("\nYou guessed Correctly! It took {0} tries.".format(counter))
    print("\nDone.")


if __name__ == "__main__":
    main()
