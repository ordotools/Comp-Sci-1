# Functions

A function is a piece of reusable code in a programming language. You have
already used some functions. `range()` is a function.

## Parts of a function

Functions are stored in a variable called the *function name*. The `range()`
function has a function name `range`. Functions follow the same naming rules as
variables.

Function names are always followed by parentheses, without a space between the
function name and the parentheses.

Functions can take *arguments*. These are always put between the parentheses,
and if there are more than one arguments they are separated by commas.

```python
range(3)  # range() takes the argument 3 and produces the numbers 0, 1, 2
range(0, 10, 2)  # range() takes three arguments and produces the numbers 0, 2, 6, 8
```

## Defining functions

In Python we can *declare a variable* just by putting the variable name and
assign a value to it. But with functions, we have to use a keyword: `def` --
this is short for "define".

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

This function `iseven()` takes an argument `n`. But what does this function do?
It returns `True` if the number is even. How can we use it?

## Using functions

```python
if iseven(4):
    print("number is even")
```

What is happening here?

1. We are passing the argument `4` into the function `iseven()`. This means that `n` in the `iseven()` function is assigned the value `4`.
2. All the code within the `iseven()` function then runs, and either there is no return (because the `if` statement has a false condition) -- and this is the same thing as returning `False` -- or `True` is returned.
3. In this case, `True` is returned, which means that "number is even" is printed in the terminal.

A note about what the `return` means. It makes the function work as a *value*.
If you use a function (let's just call it `function()`) that returns a number
and you want to use that number later, you have to store that value in a
variable.

```python
def function():
    return 5
```

`function()` here just has one job: give the value of `5`. Here are some
examples on how we can use it:

```python
x = function()
y = 4 + x  # the value of y is 9

y = 4 + function()  # the value of y is still 9

for x in range(0, function()):  # and we can use it as an argument of another function
    print(x)
```

## When to write functions

When should you use a function? The answer is disputed and there are quite a
few opinions, but a good rule of thumb is that you use it for any code that you
would have to write more than one time.

## Where to write functions

Remember that python is an interpreted language. It reads and executes from the
top of the file to the bottom. Functions have to appear *before* they are used,
otherwise python will throw an error. Using the example from earlier:

```python
def function():  # function defined
    return 5

for x in range(0, function()):  # function used
    print(x)
```

We first defined the function `function()` and then we used it.

## When functions run

A function will run only when it is **called**. The `def` keyword make the
function that you write available for calling, but nothing is actually run.
