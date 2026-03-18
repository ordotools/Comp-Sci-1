"""
PYTHON ASSIGNMENT: THE LOGIC BUFFET
Instructions: 
1. Choose any 5 tasks from the 10 listed below. 
2. Each solution MUST use a 'for' loop, an 'if' statement, and at least one 'list method'.
"""

# ----------------------------------------------------------------             
# TASK 1: The VIP Filter
# DATA: names = ["Alice", "Bob", "Zane", "Charlie", "Anna", "Dave"]
# PROMPT: Create a new empty list called 'vips'. Loop through 'names'. 
# If a name starts with "A" or "Z", add it to the 'vips' list. 
# Finally, sort the 'vips' list alphabetically and print it.
# EXPECTED OUTPUT: ['Alice', 'Anna', 'Zane']
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# TASK 2: Price Inflation
# DATA: prices = [120, 50, 200, 80, 10]
# PROMPT: Create an empty list called 'updated_prices'. Loop through 'prices'.
# If a price is over 100, give it a 10% discount (multiply by 0.9). 
# If it is 100 or less, add a 5 dollar service fee. 
# Use .append() to add these new prices to 'updated_prices' and print it.
# EXPECTED OUTPUT: [108.0, 55, 180.0, 85, 15]
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# TASK 3: The Even Squares
# DATA: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# PROMPT: Create an empty list called 'squares'. Loop through 'numbers'.
# If a number is even, square it (** 2) and append it to 'squares'.
# After the loop, if the length of 'squares' is greater than 3, 
# use .pop() to remove the very last item. Print the final list.
# EXPECTED OUTPUT: [4, 16, 36, 64]
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# TASK 4: Email Cleaner
# DATA: emails = ["pro@gmail.com", "study@uni.edu", "help@tech.com", "research@mit.edu"]
# PROMPT: Create an empty list called 'student_emails'. Loop through 'emails'.
# If an email ends with ".edu", add it to 'student_emails'. 
# After the loop, use .insert() to add the string "URGENT" to the 
# start (index 0) of the list. Print the list.
# EXPECTED OUTPUT: ['URGENT', 'study@uni.edu', 'research@mit.edu']
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# TASK 5: Deduplication Station
# DATA: raw_data = ["Apple", "Banana", "Apple", "Orange", "Banana", "Apple"]
# PROMPT: Create an empty list called 'unique_items'. Loop through 'raw_data'.
# If the item is NOT already in 'unique_items', append it.
# After the loop, print the unique list AND use .count() to print 
# how many times "Apple" appeared in the original 'raw_data'.
# EXPECTED OUTPUT: 
# Unique: ['Apple', 'Banana', 'Orange']
# Apple count: 3
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# TASK 6: Score Booster
# DATA: scores = [55, 90, 45, 72, 88]
# PROMPT: Create an empty list 'final_grades'. Loop through 'scores'.
# If a score is below 60, add 10 points. If it is 60 or above, add 2 points.
# Append the new scores to 'final_grades'. After the loop, use the 
# .reverse() method on the list and print it.
# EXPECTED OUTPUT: [90, 74, 55, 92, 65]
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# TASK 7: Word Length Filter
# DATA: words = ["Elephant", "Cat", "Monitor", "Key", "Python"]
# PROMPT: Create an empty list 'long_words'. Loop through 'words'.
# If a word has more than 5 characters, append it to 'long_words'.
# After the loop, check IF "Cat" is in 'long_words'. If it is, 
# use .clear() to empty the whole list. Print 'long_words'.
# EXPECTED OUTPUT: ['Elephant', 'Monitor', 'Python']
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# TASK 8: The "Red" Search
# DATA: colors = ["Blue", "Green", "Yellow", "Red", "Purple"]
# PROMPT: Loop through 'colors'. If the color is "Red", use the .index() 
# method to find its position and print "Found Red at index" followed 
# by the index number. If "Orange" is not in the list, .append() it.
# EXPECTED OUTPUT: 
# Found Red at index 3
# ['Blue', 'Green', 'Yellow', 'Red', 'Purple', 'Orange']
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# TASK 9: Negative Removal
# DATA: nums = [50, -10, 60, -5, 20]
# PROMPT: Create an empty list 'positives'. Loop through 'nums' and 
# append the number to 'positives' only if it is greater than 0.
# After the loop, if the sum of 'positives' is greater than 100, 
# use .remove() to take out the number 60. Print the list.
# EXPECTED OUTPUT: [50, 20]
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# TASK 10: Secret Code
# DATA: secret_phrase = ["h", "e", "l", "l", "o", "i", "t", "s", "m", "e"]
# PROMPT: Create an empty list 'coded'. Loop through 'secret_phrase'. 
# If the character is a vowel (a, e, i, o, u), append "X" to 'coded'.
# Otherwise, append the original character. After the loop, 
# use .extend() to add ["!", "!"] to the end. Print the list.
# EXPECTED OUTPUT: ['h', 'X', 'l', 'l', 'X', 'X', 't', 's', 'm', 'X', '!', '!']
# ----------------------------------------------------------------
