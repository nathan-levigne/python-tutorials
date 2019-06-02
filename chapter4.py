# 4. More Control Flow Tools
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]: # Loop over a slice copy of the entire list.
        if len(w) > 6:
            words.insert(0,w)

## 4.3. The range() function
# Allows the user to generate an arithmetic progession
for i in range(5):
    print(i)

# The start and end points can be changed, also the step can be changed
range(0, 10, 3)

# To iterate over the indices of a sequence you can combine range and len as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

## 4.4. break and continue Statements, and else Clauses on Loops
# The break statement is the same as in C, it will break out of the innermost enclosing for or while loop.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# Continue is also the same as in C
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

## 4.5. pass Statements
# The pass statement does nothing and is there only when requred syntactically.
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)

# Commonly used for creating minimal classes
class MyEmptyClass:
    pass

# Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level.
def initlog(*args):
    pass   # Remember to implement this!

## 4.6. Defining Functions
# We can create a function that writes the Fibonacci series to an arbitrary boundary:
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

# The keyword def introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters.
# The first statement of the function body can optionally be a string literal; this string literal is the function's documentation string, or docstring
# You can also rename the functions by assigning it to another variable.
f = fib
f(100)
# Every function in python returns a value. If one is not specified by return then None will be outputted
fib(0)
print(fib(0))

# Functions can return a list of objects 
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result

## 4.7. More on Defining Functions
# It is also possible to define functions with a variable number of arguments. There are three forms, which can be combined.

## 4.7.1. Default Argument Values
# The most useful form is to specify a default value for one or more arguments.
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'): # "in" tests for whether an element is in a list
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# The defualt value is evaluated only once.
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# To prevent this you can write the function like this:
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

