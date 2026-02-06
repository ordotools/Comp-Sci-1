# =============================================================================
# FOR LOOPS AND IF STATEMENTS -- just the basics
# =============================================================================
# Complete each exercise by writing code below the instructions.
# Run the file to check your work - correct output is shown in comments.
# =============================================================================

# -----------------------------------------------------------------------------
# EXERCISE 1: Basic For Loop with a List of Strings
# -----------------------------------------------------------------------------
# Create a list called `fruits` containing: "apple", "banana", "cherry"
# Use a for loop to print each fruit on its own line.
#
# Expected output:
# apple
# banana
# cherry
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# EXERCISE 2: For Loop with a List of Integers
# -----------------------------------------------------------------------------
# Create a list called `numbers` containing: 0, 1, 2, 3, 4
# Use a for loop to print each number on its own line.
#
# Expected output:
# 0
# 1
# 2
# 3
# 4
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# EXERCISE 3: Basic If Statement
# -----------------------------------------------------------------------------
# Create a float variable called `temperature` and set it to 72.5
# Write an if statement:
#   - If temperature is greater than 70, print "It's warm outside"
#
# Expected output:
# It's warm outside
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# EXERCISE 4: Two Separate If Statements
# -----------------------------------------------------------------------------
# Create an integer variable called `score` and set it to 85
# Write two separate if statements:
#   - If score is greater than or equal to 80, print "You passed!"
#   - If score is less than 80, print "Keep practicing."
#
# Expected output:
# You passed!
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# EXERCISE 5: Looping Through a String
# -----------------------------------------------------------------------------
# Create a string variable called `word` and set it to "Python"
# Use a for loop to print each character on its own line.
# (Strings can be looped through just like lists!)
#
# Expected output:
# P
# y
# t
# h
# o
# n
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# EXERCISE 6: If Statement Inside a For Loop
# -----------------------------------------------------------------------------
# Create a list of integers called `numbers` containing: 1, 2, 3, 4, 5, 6
# Loop through the list and print only the even numbers.
# Hint: a number is even if number % 2 == 0
#
# Expected output:
# 2
# 4
# 6
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# EXERCISE 7: Multiple If Statements Inside a For Loop
# -----------------------------------------------------------------------------
# Create a list of integers called `values` containing: 5, 12, 8, 20, 3
# Loop through the list:
#   - If the value is greater than 10, print "X is big" (replace X with value)
#   - If the value is less than or equal to 10, print "X is small"
#
# Expected output:
# 5 is small
# 12 is big
# 8 is small
# 20 is big
# 3 is small
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# EXERCISE 8: Accumulator Pattern with If
# -----------------------------------------------------------------------------
# Create a list of floats called `prices` containing: 10.50, 25.00, 5.75, 30.25
# Create a float variable called `total` set to 0.0
# Loop through prices and add only prices greater than 10.0 to the total.
# After the loop, print the total.
#
# Expected output:
# 65.75
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# EXERCISE 9: For Loop Inside an If Statement
# -----------------------------------------------------------------------------
# Create a string variable called `mode` and set it to "go"
# Create a list of integers called `countdown` containing: 5, 4, 3, 2, 1
#
# If mode equals "go":
#     Use a for loop to print each number in countdown
#     After the loop (but still inside the if), print "Liftoff!"
#
# Expected output:
# 5
# 4
# 3
# 2
# 1
# Liftoff!
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# EXERCISE 10: Categorizing with Multiple If Statements in a Loop
# -----------------------------------------------------------------------------
# Create a list of integers called `ages` containing: 12, 18, 25, 8, 65, 45
# Loop through the list and categorize each age using separate if statements:
#   - If age is less than 13, print "X is a child"
#   - If age is greater than or equal to 13 and less than 20, print "X is a teenager"
#   - If age is greater than or equal to 20 and less than 65, print "X is an adult"
#   - If age is greater than or equal to 65, print "X is a senior"
# Replace X with the actual age.
#
# Expected output:
# 12 is a child
# 18 is a teenager
# 25 is an adult
# 8 is a child
# 65 is a senior
# 45 is an adult
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# EXERCISE 11: Nested For Loops (Loop in a Loop)
# -----------------------------------------------------------------------------
# Create a list called `rows` containing: 1, 2, 3, 4
#
# Use nested for loops to print a right triangle of stars:
#   - Outer loop: go through each number in rows (call it `count`)
#   - Inner loop: go through rows again (call it `star`)
#       - If star is less than or equal to count, print "*" with end=""
#   - After inner loop, use print() to move to the next line
#
# Expected output:
# *
# **
# ***
# ****
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# EXERCISE 12: Nested Loops with a List of Strings
# -----------------------------------------------------------------------------
# Create a list of strings called `words` containing: "hi", "bye"
# For each word:
#   - First print the word itself
#   - Then loop through each character and print it with two spaces in front
#
# Expected output:
# hi
#   h
#   i
# bye
#   b
#   y
#   e
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# EXERCISE 13: Multiplication Table (Putting It All Together)
# -----------------------------------------------------------------------------
# Create a list called `nums` containing: 1, 2, 3
# Use nested for loops to print a multiplication table.
#
# Outer loop: go through each number (call it `a`)
# Inner loop: go through each number again (call it `b`)
# Print in format: "A x B = C" where C is a * b
#
# Expected output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# -----------------------------------------------------------------------------



# =============================================================================
# BONUS CHALLENGE
# =============================================================================
# Create a list of strings called `names` containing: "Alice", "Bob", "Charlie"
# Create a list of integers called `scores` containing: 95, 78, 88
# Create a list of integers called `indexes` containing: 0, 1, 2
#
# Loop through indexes. For each index:
#   - Get the name at that index: names[index]
#   - Get the score at that index: scores[index]
#   - If score >= 80, print "NAME scored SCORE - Passed!"
#   - If score < 80, print "NAME scored SCORE - Failed"
#
# Expected output:
# Alice scored 95 - Passed!
# Bob scored 78 - Failed
# Charlie scored 88 - Passed!
# =============================================================================
