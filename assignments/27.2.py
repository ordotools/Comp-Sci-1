#################
#  While Loops  #
#################

# while loops work like for loops, except they continue until a certain condition is false

# EXAMPLE 1
while 1 == 1:
    pass  # this means "do nothing, and don't throw an error"

# the code above does nothing, but it will run forever, because 1 will always be equal to 1.


# EXAMPLE 2
i = 10
while i > 0:
    i = i - 1

# this code runs exactly 10 times, but each time it runs, i becomes smaller and smaller.


# EXAMPLE 3
# this is a little more advanced. run the code and see what it does:
answer = 25
user = int(input("Enter a number: "))
while user != answer:
    if user > answer:
        print("Too high!")
    elif user < answer:
        print("Too low!")
        break  # this is a keyword which stops the while loop -- this works in for loops as well.
    else:
        print("Congratulations!!")

# input() asks the user for input. Putting input() into int() ensures that the input is an integer.


# Your ASSIGNMENT:
# Use a while loop to build a list. Use the following code to generate a random number between 10 and 20:
import random  # this MUST be put before random.randint() -- otherwise you will get an error.

random_number = random.randint(10, 20)

# Your task is this: have the user enter a number, and tell him it has to be greater than 0. If the number
# that is entered is too large (if it is larger than random_number) tell the user to enter another number.
# If the number that is entered is less than 0, tell the user to enter another number.
#
# For every number that is entered, add it to a new list if the number is between 0 and random_number,
# inclusive. If the sum of the numbers in that list is greater than 30, or if there are more than 3 even
# numbers in the list, print the list and break out of the loop. Then tell the user "task complete".

