# Suppose x = "pi" and y = "pie". The line of code x, y = y, x will 
# swap the values of x and y, resulting in x = "pie" and y = "pi".
# True [X] - this is the python way to make a swap
# False

# Suppose x is an integer in the following code:
def f(x):
    while x > 3:
        f(x+1)

# For any value of x, all calls to f are guaranteed to never terminate.
# True
# False [X] - for x<3 the while loop will not be triggered and the f function will be terminated immediately

# A Python program always executes every line of code written at least once.
# True
# False [X] - a method is never being read unless it's being called. if it never gets called then only the signature
#             is assessed

# Suppose you have two different functions that each assign a variable called x.
#  Modifying x in one function means you always modify x in the other function
#  for any x.
# True
# False [X] - for each function in the code a new scope is being created which allows separation of variables

# The following code will enter an infinite loop for all values of i and j.
while i >= 0:
    while j >= 0:
        print(i, j)

# True
# False [X] - if i<0 then the code will not step into the loops

# It is always possible and feasible for a programmer to come up with test cases 
# that run through every possible path in a program.
# True
# False [X] - the previous question gives a good example. i can take any rational value, or even a boolean/string value.
#             as known, there are infinite rational numbers so test every case is impossible in finite time.

# Assume f() is defined. In the statement a = f(), a is always a function.
# True
# False [X] - it depends what f returns. for example f() can return a boolean, an integer, a string, a list, etc.

# A program that keeps running and does not stop is an example of a syntax error.
# True
# False [X] - a syntax error occurs when an operation is unfamiliar by the compiler. an infinite loop happens either on
#             purpose or due to logic failure.

# Consider the following function.
def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x-1)

# A new object of type list is created for each recursive invocation of f.
# True [X] - a is created for each function call in a new scope. the function does not return anything though...
# False

# A tuple can contain a list as an element.
# True [X]
# False