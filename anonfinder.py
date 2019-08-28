# main script

import os
import sys
from bin import env


def main():
    alive = True

    while alive:

        user_input = input("( AnonFinder ) >>> ")

        env.output(user_input)

        if user_input == "exit":
            env.output("Thank you for using AnonFinder!")
            env.exit_program()

        elif user_input == "help":
            pass

        elif user_input == "show":
            pass

        else:
            pass


if __name__ == '__main__':
    main()
