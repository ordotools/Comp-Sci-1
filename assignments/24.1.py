############################
#  L I S T  M E T H O D S  #
############################

# Task 1. Filter evens — Iterate a number list; use .append() to build a new list of only even numbers.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print the new list


# Task 2. Remove duplicates — Loop through a list; use .append() to a result list only if item not in result.
numbers_with_duplicates = [4, 7, 2, 9, 4, 7, 2, 9, 4, 7, 2, 9, 4, 7, 2, 9, 4, 7, 2, 9]
# print the result list


# Task 3. Grade classifier — Loop through scores; .append() "pass" or "fail" to a new list based on a threshold. A passing grade is at least a 66.
grades = [72.5, 88.3, 91.0, 65.7, 78.2, 95.4, 43.1, 88.3, 76.8, 52.9, 84.6, 91.0, 67.3, 79.5, 88.3, 100.0, 55.2, 83.7, 72.5, 61.4, 94.8, 78.2, 47.6, 85.1, 70.0]
# print each grade on a new line in this exact format, e.g. "65.4 - fail"
# BONUS: what is the average grade?

# Task 4. Reverse words — Loop through a sentence list; use .insert(0, word) to reverse order without [::-1].
sentence = "To be or not to be, that is the question"
# print the reversed sentence


# Task 5. Flatten with condition — Loop through a nested list; use .extend() to flatten only sublists that have more than 2 items.
data = [
    [88.3, 91.0],
    [65.7, 78.2, 95.4],
    [43.1],
    [88.3, 76.8],
    [52.9, 84.6, 91.0, 67.3],
    [79.5],
    [88.3, 100.0, 55.2],
    [61.4, 94.8, 78.2, 47.6, 85.1],
]
# print the flattened list. An example result would be [[1, 2], 3, 4, 5, [6], 7, 8, 9, 10, 11, 12]


# Task 6. Running total cap — Loop through numbers; .append() each to a running sum list, but if the sum exceeds a cap, .append() the cap instead.
numbers_to_sum = [23, 45, 67, 12, 78, 34, 56, 81, 19, 63]
cap = 87
# print the running sum list. Example: you have a list [10, 30, 25, 20, 15, 40] with a cap of 70, your result would be [10, 40, 65, 70, 70, 70]


# Task 7. Rotate on condition — Loop through a list; if an item meets a condition, use .pop(0) and .append() to move it to the back.
numbers = [134, 287, 412, 156, 349, 223, 478, 301, 167, 392, 245, 418, 133, 267, 384, 199, 456, 312, 271, 443]
# Condition 1: the number is even
# Condition 2: the number is divisible by 3
# Condition 3: the number is less than 500
#
# return the new, sorted list
