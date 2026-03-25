# ============================================================
#  LIST METHODS CHALLENGE
#  Rules:
#    - Work with 'scores' the whole time — no new lists
#    - Each step uses the result of the previous one
#    - Print your list after each step to check your work
# ============================================================

scores = [42, 7, 99, 15, 3, 88, 56, 23, 71, 4, 61, 38, 19, 90, 5, 47, 82, 12, 66, 34]

# ----------------------------------------------------------
# STEP 1: Clean the list
# Remove every score that is a single digit (less than 10).
# Then append two new scores to the end: 95 and 11.
#
# Hint: there are four single-digit values. Remove each one.
# Expected length after this step: 18
# ----------------------------------------------------------

# your code here

for score in scores:
    if score < 10:
        scores.remove(score)
    scores.append(95, 11)

print("After Step 1:", scores)

# ----------------------------------------------------------
# STEP 2: Sort and trim
# Sort the list in ascending order.
# Then remove the three lowest scores from the list.
#
# Hint: after sorting, the lowest scores are easy to find.
# Expected length after this step: 15
# ----------------------------------------------------------

# your code here

print("After Step 2:", scores)

# ----------------------------------------------------------
# STEP 3: Find and move the top score
# Find the highest score in the list.
# Remove it from wherever it currently is,
# then insert it at index 0 (the front of the list).
#
# Hint: one method finds the value, another finds its position.
# Expected length after this step: 15 (same — just reordered)
# ----------------------------------------------------------

# your code here

print("After Step 3:", scores)

# ----------------------------------------------------------
# STEP 4 (challenge): Count and reverse
# Count how many scores are above 50.
# Print that count.
# Then reverse the entire list in place.
#
# Hint: .count() won't help here — you'll need a for loop
# with an if statement and a list method you haven't used yet.
# Expected length after this step: 15 (same)
# ----------------------------------------------------------

# your code here

print("Count above 50:", ...)
print("After Step 4:", scores)
