# here are three bits of code that you have to rewrite using functions

# The code calculates the average of three different lists. The logic for
# summing the numbers and dividing by the length is repeated three times.
#
# TASK 1: write a calculate_average(number_list) function.

list1 = [10, 20, 30, 40]
list2 = [5, 15, 25]
list3 = [100, 200, 300, 400, 500]

# Calculate average for list1
total1 = 0
for num in list1:
    total1 += num
avg1 = total1 / len(list1)
print("Average of list 1:", avg1)

# Calculate average for list2
total2 = 0
for num in list2:
    total2 += num
avg2 = total2 / len(list2)
print("Average of list 2:", avg2)

# Calculate average for list3
total3 = 0
for num in list3:
    total3 += num
avg3 = total3 / len(list3)
print("Average of list 3:", avg3)

###############################################################################

# This program searches through two different lists of grades to find the
# highest score. (You are not allowed to use the built-in max() function)
#
# TASK 2: write a find_highest_score(score_list) function.

test_scores = [85, 92, 78, 99, 88]
project_scores = [90, 95, 80, 85, 100]

# Find max test score
highest_test = test_scores[0]
for score in test_scores:
    if score > highest_test:
        highest_test = score
print("Highest test score:", highest_test)

# Find max project score
highest_project = project_scores[0]
for score in project_scores:
    if score > highest_project:
        highest_project = score
print("Highest project score:", highest_project)

###############################################################################

# This program looks through two lists and creates new lists containing only
# the even numbers.
#
# TASK 3: srite a get_even_numbers(numbers) function that returns a new list.

batch_a = [12, 7, 19, 24, 6, 11]
batch_b = [33, 44, 55, 66, 77, 88]

# Get even numbers from batch A
evens_a = []
for num in batch_a:
    if num % 2 == 0:
        evens_a.append(num)
print("Even numbers in Batch A:", evens_a)

# Get even numbers from batch B
evens_b = []
for num in batch_b:
    if num % 2 == 0:
        evens_b.append(num)
print("Even numbers in Batch B:", evens_b)
