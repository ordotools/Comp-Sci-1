# ==========================================
# FILE 3: GAME INVENTORY & LOGIC
# Focus: Video Game Mechanics, State Tracking
# ==========================================

# --- IF STATEMENTS ---
player_health = 0
player_gold = 150
rations_cost = 50
has_key = True

# 1. Prompt: Check if player_health is less than or equal to 0. If so, print "Game Over".
# Expected Output: Game Over

# 2. Prompt: Check if the player has enough gold to buy rations. If so, print "Purchase successful".
# Expected Output: Purchase successful

# 3. Prompt: Check if player has the key (has_key == True). If so, print "Door unlocked".
# Expected Output: Door unlocked

# 4. Prompt: Check if player_gold is exactly 100. Print "Perfect century" if true.
# Expected Output: (Nothing prints, because it is 150)

# 5. Prompt: Check if player_health > 0 AND player_gold > 0. Print "Ready for adventure".
# Expected Output: (Nothing prints, health is 0)

# 6. Prompt: Write an if/elif/else block. If gold > 200 print "Rich", elif gold > 100 print "Comfortable", else print "Poor".
# Expected Output: Comfortable

# 7. Prompt: Check if NOT has_key. Print "You need a key".
# Expected Output: (Nothing prints)

# 8. Prompt: Change player_health to 100. Check if player_health is 100. Print "Full health!".
# Expected Output: Full health!


# --- FOR LOOPS ---
inventory = ["sword", "shield", "rations", "map"]
enemy_healths = [50, 60, 45]

# 9. Prompt: Loop through the inventory and print each item.
# Expected Output: sword \n shield \n rations \n map

# 10. Prompt: Loop through enemy_healths. Subtract 10 from each (simulating a sweeping attack) and print the new health.
# Expected Output: 40 \n 50 \n 35

# 11. Prompt: Loop through inventory. If you find "rations", print "Food supply found!".
# Expected Output: Food supply found!

# 12. Prompt: Loop 3 times using range() and print "Swing sword!".
# Expected Output: Swing sword! \n Swing sword! \n Swing sword!

# 13. Prompt: Loop through enemy_healths. Sum them up to find the total boss health. Print the sum.
# Expected Output: 155

# 14. Prompt: Loop through inventory. Print the item AND its length (e.g., "sword is 5 characters").
# Expected Output: sword is 5 characters \n shield is 6 characters...

# 15. Prompt: Loop through enemy_healths. If health is < 50, print "Enemy is weak!".
# Expected Output: Enemy is weak! (prints once for the 45)

# 16. Prompt: Use enumerate() in a for loop to print the inventory with numbers (e.g., "0: sword").
# Expected Output: 0: sword \n 1: shield \n 2: rations \n 3: map


# --- LIST METHODS ---
chest_loot = ["gold coin", "ruby", "iron boots"]

# 17. Prompt: Append "compass" to the chest_loot list. Print the list.
# Expected Output: ['gold coin', 'ruby', 'iron boots', 'compass']

# 18. Prompt: Remove "ruby" from chest_loot. Print the list.
# Expected Output: ['gold coin', 'iron boots', 'compass']

# 19. Prompt: Insert "torch" at index 1 in chest_loot. Print the list.
# Expected Output: ['gold coin', 'torch', 'iron boots', 'compass']

# 20. Prompt: Count how many "gold coin" items are in chest_loot. Print the count.
# Expected Output: 1

# 21. Prompt: Extend the 'inventory' list (from the for-loop section) with the 'chest_loot' list. Print 'inventory'.
# Expected Output: ['sword', 'shield', 'rations', 'map', 'gold coin', 'torch', 'iron boots', 'compass']

# 22. Prompt: Sort the new 'inventory' list alphabetically. Print the list.
# Expected Output: ['compass', 'gold coin', 'iron boots', 'map', 'rations', 'shield', 'sword', 'torch']

# 23. Prompt: Pop the last item off the 'inventory' list (the torch). Print the list.
# Expected Output: ['compass', 'gold coin', 'iron boots', 'map', 'rations', 'shield', 'sword']

# 24. Prompt: Find the index of "map" in the sorted inventory. Print the index.
# Expected Output: 3

# 25. Prompt: Clear the 'chest_loot' list to simulate an empty chest. Print the list.
# Expected Output: []
