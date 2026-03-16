# ==========================================
# FILE 4: THE GAUNTLET
# Focus: Combining Loops, Conditionals, and List Methods
# ==========================================

# 1. Prompt: Loop through 'numbers'. If a number is even, append it to 'even_nums'. Print 'even_nums'.
numbers = [15, 22, 8, 99, 104, 33, 42]
even_nums = []
# Expected Output: [22, 8, 104, 42]


# 2. Prompt: Loop through 'words'. If a word starts with "A" or "a", append it to 'a_words'. Print 'a_words'.
words = ["apple", "Banana", "avocado", "cherry", "Apricot"]
a_words = []
# Expected Output: ['apple', 'avocado', 'Apricot']


# 3. Prompt: Sort the 'grades' list. Then loop through it. If the grade is 70 or higher, append it to 'passing'. Print 'passing'.
grades = [55, 92, 68, 85, 100, 42, 75]
passing = []
# Expected Output: [75, 85, 92, 100]


# 4. Prompt: Loop through 'mixed_numbers'. If the number is positive, append to 'positives'. If negative, append to 'negatives'. Print both lists.
mixed_numbers = [10, -5, 3, -1, 0, -8, 20]
positives = []
negatives = []
# Expected Output: Positives: [10, 3, 20] | Negatives: [-5, -1, -8]


# 5. Prompt: Loop through 'emails' using range(len(emails)). If the email does NOT contain "@", change that specific item in the list to "INVALID". Print the list.
emails = ["user@gmail.com", "bad_email.com", "admin@yahoo.com", "no_at_symbol"]
# Expected Output: ['user@gmail.com', 'INVALID', 'admin@yahoo.com', 'INVALID']


# 6. Prompt: Loop through a copy of 'inbox'. If the message is "spam", remove() it from the original 'inbox' list. Print 'inbox'. 
# (Hint: use inbox.copy() in your for loop!)
inbox = ["email", "spam", "update", "spam", "receipt"]
# Expected Output: ['email', 'update', 'receipt']


# 7. Prompt: Loop 3 times using range(). Inside the loop, check if 'deck' has items. If it does, pop() the last card and append it to 'hand'. Print 'hand'.
deck = ["Goblin", "Elf", "Orc", "Dragon", "Troll"]
hand = []
# Expected Output: ['Troll', 'Dragon', 'Orc']


# 8. Prompt: Loop through 'usernames'. If the length of the username is less than 5, count how many times "Guest" is in the 'banned' list. (Just a wacky combo!)
usernames = ["Alex", "SuperCoder99", "Bo", "Sniper", "Jo"]
banned = ["Guest", "Troll", "Guest", "Hacker"]
# Expected Output: Print the number 2, three separate times (since 3 names are under 5 characters).


# 9. Prompt: Extend 'team_a' with 'team_b'. Then loop through 'team_a'. If the name is "Spy", clear() the entire team_a list and break the loop. Print 'team_a'.
team_a = ["Knight", "Archer"]
team_b = ["Doctor", "Spy", "Scholar"]
# Expected Output: []


# 10. Prompt: Loop through 'prices'. If the price is greater than 100, calculate a 10% discount and insert() the new discounted price at the beginning (index 0) of 'discounted_items'. Print 'discounted_items'.
prices = [50, 150, 20, 200]
discounted_items = []
# Expected Output: [180.0, 135.0] (200 becomes 180, inserted at 0. Then 150 becomes 135, inserted at 0).
