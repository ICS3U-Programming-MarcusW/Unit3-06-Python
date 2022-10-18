#!/usr/bin/env python3
# Created By: Marcus Wehbi
# Date: Oct 17th, 2022
# This program asks the user for a number 0 and 9
# It then displays if they guessed the correct number
# It also uses a try catch for any errors
import random


def main():
    # declare variable
    correct_guess = random.randint(0, 9)  # random number between 0 and 9
    # get the users input (users guessed number)
    guessed_number_string = input("Choose a number between 0 and 9 : ")
    # use a try catch to ensure user properly enters an integer
    try:
        guessed_number_int = int(guessed_number_string)
        # check if the user selected the correct number
        if guessed_number_int == correct_guess:
            # if the user guessed correctly, tell them
            print("You guessed correctly.")
        # make sure the users input is within parameters
        if guessed_number_int > 9 or guessed_number_int < 0:
            print("You did not enter an integer within the given parameters.")
        elif (
            guessed_number_int != correct_guess
        ):  # check if the user selected the incorrect number
            # if the user guessed incorrectly, tell them
            print("You guessed wrong, the correct answer was: {}".format(correct_guess))
    # tell the user they incorrectly inputted an integer
    except Exception:
        print("You did not properly enter an integer.")
    finally:
        # display following regardless of error or not
        print("Thank you for playing.")


if __name__ == "__main__":
    main()
