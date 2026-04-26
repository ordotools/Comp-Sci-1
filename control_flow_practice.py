"""
Python Control Flow Practice: 100 Exercises
Focus: if, elif, else, while, for, and list.append()
Instructions: Write the code under each prompt to match the Expected Output.
"""

# ==========================================
# PART 1: IF, ELIF, ELSE (Problems 1-25)
# ==========================================

# 1. Check if x is greater than 5. (Use x = 10)
# Expected Output: 10 is greater
x = 10


# 2. Check if 3 is less than 1.
# Expected Output: (No output)


# 3. Check if a number is even or odd. (Use num = 8)
# Expected Output: Even
num = 8


# 4. STARTER CODE: Complete to check if age is 18 or older.
# Expected Output: Adult
age = 20
if age >= 18:
    # Your code here
    pass


# 5. Check if a number is positive, negative, or zero. (Use val = 15)
# Expected Output: Positive
val = 15


# 6. Check if 50 is between 40 and 60.
# Expected Output: In range
n = 50


# 7. Check if a number is divisible by 5. (Use num = 25)
# Expected Output: Divisible by 5


# 8. STARTER CODE: Check if a number is exactly 100.
# Expected Output: Century
score = 100


# 9. Determine the larger of two numbers and print it. (Use a=7, b=12)
# Expected Output: 12


# 10. Check if a number is a multiple of 3 and 2. (Use n = 12)
# Expected Output: Multiple of 6


# 11-20: Comparison Practice
# 11. x = 5, y = 5. Print "Equal" if they match.
# 12. x = 10, y = 2. Print "x is bigger" if x > y.
# 13. x = -5. Print "Negative" if x < 0.
# 14. x = 0. Print "Zero" if x is 0.
# 15. x = 101. Print "High" if x > 100.
# 16. x = 9. Print "Odd" if x % 2 != 0.
# 17. x = 20. Print "Threshold met" if x >= 20.
# 18. x = 15. Print "Divisible by 3" if x % 3 == 0.
# 19. x = 7, y = 7. Print "True" if x <= y.
# 20. x = 4. Print "Within bounds" if 1 < x < 5.


# 21. STARTER CODE: If price is over 50, apply 25% discount.
# Expected Output: 45.0
price = 60


# 22. Check if number is NOT 13. (Use n = 7)
# Expected Output: Safe


# 23. Check if a number is a single digit (0-9). (Use n = 4)
# Expected Output: Single digit


# 24. Compare three numbers to find if the first (a) is the smallest. (Use a=1, b=5, c=10)
# Expected Output: Smallest


# 25. Check if sum of 5 and 5 is 10.
# Expected Output: Correct


# ==========================================
# PART 2: FOR LOOPS & RANGE (Problems 26-50)
# ==========================================

# 26. Print numbers 0 to 4 using range.
# Expected Output: 0 1 2 3 4


# 27. Print numbers 1 to 5 using range.
# Expected Output: 1 2 3 4 5


# 28. Print even numbers from 0 to 10.
# Expected Output: 0 2 4 6 8 10


# 29. STARTER CODE: Print multiples of 5 up to 25.
# Expected Output: 5 10 15 20 25
for i in range(5, 26, 5):
    pass


# 30. Sum numbers from 1 to 3 and print the total.
# Expected Output: 6


# 31. Print "Hello" 3 times.
# Expected Output: Hello Hello Hello


# 32. Print numbers from 10 down to 8.
# Expected Output: 10 9 8


# 33. STARTER CODE: Loop through 1 to 4 and print the square of each.
# Expected Output: 1 4 9 16


# 34. Count how many numbers are in range(10) and print the count.
# Expected Output: 10


# 35. Multiply all numbers from 1 to 4 and print the product.
# Expected Output: 24


# 36-45: Write the range() function that produces these results:
# 36. Results: 2 3 4
# 37. Results: 0 3 6 9
# 38. Results: 100 101 102
# 39. Results: 5 4 3 2 1
# 40. Results: 10 12 14 16 18
# 41. Results: 0
# 42. Results: 3
# 43. Results: 0 -1 -2
# 44. Results: 10
# 45. Results: 2 6


# 46. STARTER CODE: Print "Python" for each number in range(2).
# Expected Output: Python Python


# 47. Loop through range(3) and print the index doubled.
# Expected Output: 0 2 4


# 48. Sum the first 5 even numbers (0,2,4,6,8) and print it.
# Expected Output: 20


# 49. Print 1.0, 2.0, 3.0 using range and a float conversion.
# Expected Output: 1.0 2.0 3.0


# 50. Loop 4 times, print "Looping".
# Expected Output: Looping Looping Looping Looping


# ==========================================
# PART 3: WHILE LOOPS (Problems 51-75)
# ==========================================

# 51. Count up from 1 to 3 using a while loop.
# Expected Output: 1 2 3


# 52. Count down from 3 to 1 using a while loop.
# Expected Output: 3 2 1


# 53. STARTER CODE: Double a number (starting at 2) while it is 32 or less.
# Expected Output: 2 4 8 16 32
n = 2


# 54. Keep adding 5 to a total until total hits 20. Print each step.
# Expected Output: 5 10 15 20


# 55. While a number is positive, subtract 2 and print it. (Start at 5)
# Expected Output: 5 3 1


# 56-65: Predicting and Writing logic
# 56. while x < 5: print(x); x += 1 (Start x=2)
# 57. while x != 0: print(x); x -= 1 (Start x=3)
# 58. while x < 100: x += 50 (Start x=0). Print final x.
# 59. while x > 10: x -= 5 (Start x=12). Print final x.
# 60. while x <= 3: x += 1 (Start x=1). Print final x.
# 61. Write a loop that never runs (while False).
# 62. i = 0; while i < 2: print("A"); i += 1.
# 63. n = 10; while n > 7: n -= 1. Print final n.
# 64. n = 1; while n < 4: n += n. Print final n.
# 65. i = 5; while i < 5: print(i).


# 66. STARTER CODE: Print "Wait" until timer reaches 3. Print timer value.
# Expected Output: 0 1 2
timer = 0


# 67. Divide 100 by 2 repeatedly until it is less than 10. Print each result.
# Expected Output: 100 50 25 12.5


# 68. Sum numbers (1, 2, 3...) while the sum is under 10. Print final sum.
# Expected Output: Final sum: 10


# 69. Use while loop to print "Z" 2 times.
# Expected Output: Z Z


# 70. Subtract 1 from 10 until it hits 7.
# Expected Output: 10 9 8


# 71-75: More While logic
# 71. x = 1; while x < 10: x *= 3. Print final x.
# 72. x = 5; while x > 0: x -= 1. Print final x.
# 73. x = 0; while x < 1: x += 0.5. Print final x.
# 74. x = 10; while x > 5: x -= 2. Print final x.
# 75. x = 2; while x < 10: x += 4. Print final x.


# ==========================================
# PART 4: LOOPS + LIST APPEND + IF (Problems 76-100)
# ==========================================

# 76. Add numbers 1 to 3 to a list called 'nums'.
# Expected Output: [1, 2, 3]


# 77. Add only even numbers from 0 to 6 to a list called 'evens'.
# Expected Output: [0, 2, 4, 6]


# 78. STARTER CODE: Add squares of 1, 2, 3 to a list called 'sqs'.
# Expected Output: [1, 4, 9]
sqs = []


# 79. Filter a list: loop through 'data' and only add numbers > 10 to 'filtered'.
# Expected Output: [15, 20]
data = [5, 15, 2, 20]


# 80. Create a list of 5 zeros using a loop and .append().
# Expected Output: [0, 0, 0, 0, 0]


# 81. Loop 1 to 5: if number is 3, print "Found", else print the number.
# Expected Output: 1 2 Found 4 5


# 82. STARTER CODE: Count how many 7s are in the list 'vals'.
# Expected Output: 2
vals = [7, 2, 7, 8]
count = 0


# 83. Append the boolean value True to a list 3 times using a while loop.
# Expected Output: [True, True, True]


# 84. Add numbers 10, 20, 30 to a list using a for loop with a step.
# Expected Output: [10, 20, 30]


# 85. Loop through a list and print "Negative found" if a number is < 0.
# Expected Output: Negative found
nums = [1, 2, -3, 4]


# 86-95: Mixed logic
# 86. For i in range(5): if i > 2: append to list. Print list.
# 87. While list length < 2: append 1. Print list.
# 88. For i in range(3): if i == 1: print("skip") else: print(i).
# 89. If 10 is in [1, 10, 100]: print "Yes".
# 90. n = 1; while n < 10: if n % 5 == 0: print(n); n += 1.
# 91. Take [1, 2, 3], multiply each by 10 and append to a new list.
# 92. For i in range(10): if i % 3 == 0: append to list.
# 93. x = [1, 2]; append 3 to x; print x.
# 94. Nested Loop: For i in range(2), For j in range(2): print i.
# 95. If length of [1, 2] is 2: print "Size 2".


# 96. STARTER CODE: Double every number in 'orig' and store in 'new_list'.
# Expected Output: [2, 4, 6]
orig = [1, 2, 3]
new_list = []


# 97. Use a while loop to append numbers (1, 2, 3...) to a list until the sum of the list is 6.
# Expected Output: [1, 2, 3]


# 98. Use a loop to find the smallest number in [5, 2, 8] and print it.
# Expected Output: 2


# 99. STARTER CODE: Check if list 'L' is empty using len().
# Expected Output: Empty
L = []


# 100. Print "Done" after a for loop (range 2) finishes.
# Expected Output: 0 1 Done
