#!/usr/bin/env python3\
# Created By:Kamche
# Created on: November 21, 2026
# This program asks the user to create
# a program generating RGB using
# multiple loops


def main():
    # This function uses 3 nested loops
    counter1 = 0
    counter2 = 0
    counter3 = 0

    # Using multiple nested loop to get the RGB colours
    for counter1 in range(3):
        for counter2 in range(3):
            for counter3 in range(3):

                print(
                    "\033[38;2;{};{};{}mRGB({}, {}, {})\033[0m]".format(
                        counter1, counter2, counter3, counter1, counter2, counter3
                    )
                )


if __name__ == "__main__":
    main()
