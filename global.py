#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This Program global and local variable

# global variable
variable_x = 25


def local_variable():
    # This function calculate about local variable

    variable_x = 10
    variable_y = 30
    variable_z = variable_x + variable_y

    print(
        "Local variable_x, variable_y, variable_z: {0} + {1} = {2}".format(
            variable_x, variable_y, variable_z
        )
    )


def global_variable():
    # This function calculate about global variable

    global variable_x
    variable_x = variable_x + 1
    variable_y = 30
    variable_z = variable_x + variable_y

    print(
        "Global variable_x, variable_y, variable_z: {0} + {1} = {2}".format(
            variable_x, variable_y, variable_z
        )
    )


def main():
    local_variable()
    global_variable()
    print("\nDone")


if __name__ == "__main__":
    main()
