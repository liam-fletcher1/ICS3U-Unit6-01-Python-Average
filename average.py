#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Oct 2021
# This gets random numbers then finds the average using an array

import random


def main():
    # This function gets random numbers then finds the average using an array

    # Array
    number_array = []

    # Process
    for number_of_times in range(10):
        random_number = random.randint(1, 100)
        print("The random number is: " + str(random_number))
        number_array.append(random_number)

    average_numbers = sum(number_array) / 10 + 1

    # Output
    print("")
    print("The average is " + str(average_numbers))


if __name__ == "__main__":
    main()
