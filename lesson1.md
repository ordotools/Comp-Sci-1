# Basic programming structures and scope

---
## if statements
---

``` IF condition THEN ``` If the condition is true, then do the indented code
that follows. There can be only one IF.

``` ELSE IF condition THEN ``` If the above condition(s) is(are) not true, and
the current condition is true, then do the indented code that follows. There
can be an infinite number of ELSE IFs. ELSE IF is optional.

``` ELSE ``` If the above condition(s) is(are) not true, then do the indented code that
follows. If the conditions above are not true, then the code after the ELSE
will always be executed. ELSE does not itself take a condition. There is only
one ELSE. ELSE is optional only if there are no ELSE IFs.

``` END IF ``` This is a required part that always accompanies an IF statement.
It lets the interpreter or compiler know that the IF statement is complete. It
does not take a condition, and does not have any code after it to execute.

### pseudocode example
```
IF x > 0 THEN
    OUTPUT "x is greater than 0"
ELSE IF x == 0 THEN
    OUTPUT "x is equal to 0"
ELSE
    OUTPUT "x is less than 0"
END IF
```

### use
Use IF statements when you have to do something based off something else.

---
## while loops
---

```WHILE condition``` As long as the condition is true, the statements
following will be executed.

```END WHILE``` Lets the interpreter or compiler know that there are no more
statements within the **WHILE** loop.

### pseudocode example
```
SET x = 0
WHILE x == 0
    OUTPUT "x is not equal to 0"
END WHILE
```

### use
Use WHILE loops when you need to run some statements many times, and do
not know when you will have to stop running them.

### WARNING!!
There is something known as an *infinite loop* that can crash your program. You
can get an infinite loop whenever you have a condition in a WHILE loop that
never changes. For instance, if you say ```WHILE 1 == 1```, then you have a
condition that can never not be true, which means that your loop will run over
and over and over again until your program crashes.

---
## for loops
---

```FOR iterator = startValue to endValue``` While the *iterator* has not yet
reached the end of its list of values, do the statements within the loop. Each
time the code runs, the iterator increases its value by exactly 1. Once it's
value is equal to the `endValue`, the loop ends. The `iterator` can be accessed
and used like any other variable.

```END FOR``` Lets the interpreter or compiler know that there are no more
statements within the **FOR** loop.

```
FOR x = 1 to 10
    OUTPUT = x
END FOR 
```

















