# Functions

A function is a piece of reusable code in a programming language. You have
already used some functions. `range()` is a function.

## Parts of a function

Functions are stored in a variable called the *function name*. The `range()` function has a function name `range`. Functions follow the same naming rules as variables.

Function names are always followed by parentheses, without a space between the function name and the parentheses.

Functions can take *arguments*. These are always put between the parentheses, and if there are more than one arguments they are separated by commas.

```python
range(3)  # range() takes the argument 3 and produces the numbers 0, 1, 2
range(0, 10, 2)  # range() takes three arguments and produces the numbers 0, 2, 6, 8
```

## Defining functions

In Python we can *declare a variable* just by putting the variable name and assign a value to it. But with functions, we have to use a keyword: `def` -- this is short for "define".

```python
def myfunction():
    return True
```

In the example above, we define a function with the function name "my
function". `myfunction()` does not take any arguments, and returns `True`.
`return` is a keyword that allows a function to have output. Not every function
needs to have a `return`, but most of the functions you write will `return`
something. In this case, if we were to make a variable `value` and assign it
`value = myfunction()`, it is the exact same thing as writing `value = True`,
because that is what `myfunction()` returns. Not too useful, but what if we
make the function do some work?

```python
def iseven(n):
    if not n%2:
        return True
```

This function `iseven()` takes an argument `n`. But what does this function do? It returns `True` if the number is even. How can we use it?

```python
if iseven(4):
    print("number is even")
```

What is happening here?

1. We are passing the argument `4` into the function `iseven()`. This means that `n` in the `iseven()` function is assigned the value `4`.
2. All the code within the `iseven()` function then runs, and either there is no return (because the `if` statement has a false condition) -- and this is the same thing as returning `False` -- or `True` is returned.
3. In this case, `True` is returned, which means that "number is even" is printed in the terminal.


