
---

# The Need for Rules and a Language

There has to be some standard whenever you write code.

We call this *syntax*. A set of rules that you follow when writing a specific
language.

Even though we have these standards, all langauges follow some basic
principles.

---

# Basic Syntax Rules

1. Each statement should be written on a new line
2. Indentation shows nesting (use consistent spacing)
3. Use UPPERCASE for keywords (IF, WHILE, FOR, etc.)
4. Use meaningful variable names in camelCase (firstName, totalSum) or
   snake_case (first_name, total_sum)

```python
for x in range(0,1):
    print("Hello World!")
    # indentation of 4 spaces
```

# Style Guidelines

These are not all dictated by the rules of the language, but are standards that
allow for easy maintainence and reading.

1. Comments start with `//` and explain complex logic
2. One statement per line
3. Blank lines between logical sections
4. Consistent indentation (recommend 4 spaces)
5. Clear, descriptive variable names (avoid x, y, z)

---

## A Pseudocode Standard
```
// This is a comment. It is not executed. Just something for you to read.
// Input and Output
INPUT variableName    // Get input from user
OUTPUT message        // Display output

// Variables
SET variableName = value   // Variable assignment

// Conditionals
IF condition THEN
    statements
ELSE IF condition THEN
    statements
ELSE
    statements
END IF

// Loops
FOR i = startValue TO endValue
    statements
END FOR

//------------------------------------------------
// don't worry about the below
//------------------------------------------------

WHILE condition
    statements
END WHILE

// Functions
FUNCTION functionName(parameter1, parameter2)
    statements
    RETURN value
END FUNCTION

// Arrays
ARRAY numbers[size]   // Array declaration
SET numbers[0] = 5    // Array assignment
```

---

Here's a simple example that finds the maximum number in an array:
```
FUNCTION findMax(numbers, size)
    SET max = numbers[0]
    
    FOR i = 1 TO size - 1
        IF numbers[i] > max THEN
            SET max = numbers[i]
        END IF
    END FOR
    
    RETURN max
END FUNCTION

// Main program
SET numbers = ARRAY[5]
READ numbers[0]
READ numbers[1]
READ numbers[2]
READ numbers[3]
READ numbers[4]

SET result = findMax(numbers, 5)
PRINT "The maximum number is: " + result
```

---

## Some common algorithms implemented in this pseudocode standard, with clear explanations of how they work.

1. **Binary Search** - Efficiently finds an element in a sorted array

```
FUNCTION binarySearch(array, target, low, high)
    WHILE low <= high
        SET mid = (low + high) / 2
        
        IF array[mid] == target THEN
            RETURN mid
        ELSE IF array[mid] < target THEN
            SET low = mid + 1
        ELSE
            SET high = mid - 1
        END IF
    END WHILE
    
    RETURN -1  // Element not found
END FUNCTION
```

How it works:
- Divides the sorted array in half repeatedly
- If middle element is target, we're done
- If target is higher, search upper half
- If target is lower, search lower half
- Continues until element is found or search space is empty
- Much faster than linear search: O(log n) vs O(n)

2. **Bubble Sort** - Simple sorting algorithm

```
FUNCTION bubbleSort(array, size)
    FOR i = 0 TO size - 1
        FOR j = 0 TO size - i - 1
            IF array[j] > array[j + 1] THEN
                // Swap elements
                SET temp = array[j]
                SET array[j] = array[j + 1]
                SET array[j + 1] = temp
            END IF
        END FOR
    END FOR
END FUNCTION
```

How it works:
- Repeatedly steps through the array
- Compares adjacent elements
- Swaps them if they're in the wrong order
- Larger elements "bubble up" to the end
- After each pass, one more element is in final position
- Simple but inefficient: O(n²) time complexity

3. **Finding Factorial** - Demonstrates recursion

```
FUNCTION factorial(n)
    IF n <= 1 THEN
        RETURN 1
    END IF
    
    RETURN n * factorial(n - 1)
END FUNCTION
```

How it works:
- Uses recursion to calculate n!
- Base case: if n ≤ 1, return 1
- Recursive case: n * factorial(n-1)
- Example for n=4:
  - 4 * factorial(3)
  - 4 * (3 * factorial(2))
  - 4 * (3 * (2 * factorial(1)))
  - 4 * (3 * (2 * 1)) = 24

4. **Finding GCD** - Greatest Common Divisor using Euclidean algorithm

```
FUNCTION findGCD(a, b)
    WHILE b != 0
        SET temp = b
        SET b = a MOD b
        SET a = temp
    END WHILE
    
    RETURN a
END FUNCTION
```

How it works:
- Uses Euclidean algorithm: GCD(a,b) = GCD(b, a MOD b)
- Repeatedly divides larger number by smaller
- Takes remainder and continues until remainder is 0
- Example for GCD(48,18):
  - 48 = 2 * 18 + 12
  - 18 = 1 * 12 + 6
  - 12 = 2 * 6 + 0
  - Therefore, GCD is 6

5. **Linear Search with Counter** - Simple search with extra functionality

```
FUNCTION linearSearch(array, size, target)
    SET count = 0
    
    FOR i = 0 TO size - 1
        IF array[i] == target THEN
            SET count = count + 1
        END IF
    END FOR
    
    PRINT "Found " + count + " occurrences"
    RETURN count
END FUNCTION
```

How it works:
- Scans through entire array sequentially
- Counts how many times target appears
- Simple but thorough: checks every element
- Useful when you need to find all occurrences
- Time complexity is O(n)
- Best for unsorted arrays or when you need all matches

---
