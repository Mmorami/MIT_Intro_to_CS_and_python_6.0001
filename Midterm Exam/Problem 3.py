#Examine the following code snippet:

stuff = _____
for thing in stuff:
    if thing == 'iQ':
        print("Found it")

# Select all the values of the variable "stuff" that will make the 
# code print "Found it".


# ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"] [X] - thing iterate over the elements of the list.
# ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad") [X] - thing iterate over the elements of the tuple.
# [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]  XXXX - thing will be assigned as a tuple
# ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], ) XXXX - thing will be assigned as a list
# ["iQ"] [X] - thing iterate over the elements of the list.
# "iQ" XXXX - thing will iterate over the chars

# The following Python code is supposed to compute the square of an integer 
# by using successive additions.

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

# Not considering recursion depth limitations, what is wrong with this 
# implementation of procedure Square? Check all that apply.


# It is going to return a wrong value. [X] a correct implementation would've return 1 when n==0 and the recursive call multiply by x: SquareHelper(n-1, x) * x
# The term Square is a reserved Python keyword. XXXX - square is not a reserved keyword
# Function names cannot start with a capital letter. XXXX - the standard writing expects lowercase, but an uppercase is valid
# The function is never going to return anything. XXXX - the return structure will apply for every integer
# Python has arbitrary precision arithmetic. XXXX - the arithmetic precision is consistent and determined by the data type
# This function will not work for negative numbers. XXXX - any negative number sent to square will be conberted to positive
# The call SquareHelper(abs(x), abs(x)) won't work because you can't have abs(x) as both parameters. XXXX - it is possible
# Nothing is wrong; the code is fine as-is.