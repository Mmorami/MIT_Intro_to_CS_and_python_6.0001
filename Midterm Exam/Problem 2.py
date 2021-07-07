# Consider the statement: L = {'1':1, '2':2, '3':3}. Which is correct?
# L is a list
# L is immutable
# L contains 6 elements
# L has integer keys
# L maps strings to integers [X] - L is a dictionary which is mutable. it contains 3 elements with string as keys

# Assume a break statement is executed inside a loop and that the loop 
# is inside a function. Which of the following is correct?
# The program might immediately terminate.
# The function might immediately terminate.
# The loop will always immediately terminate. [X] - a break statement inside a loop will always shoot out of that loop
# All of the above.
# None of the above.

# In Python, which of the following is a mutable object?
# a string
# a tuple
# a list [X] - a string and a tuple are immutable (can't make a direct change of element a[2] = 'a'). a list is mutable
# all of the above
# none of the above

# Assume the statement s[1024] = 3 does not produce an error message. 
# This implies:
# type(s) can be str
# type(s) can be tuple
# type(s) can be list [X] - in direct continuation to the previous question, strings and tuples are immutable, hence such command should've prompt an error.
# All of the above

# Consider the code:

L = [1,2,3]
d = {'a': 'b'}
def f(x):
    return 3

# Which of the following does NOT cause an exception (error) to be thrown?
# print(L[3])
# print(d['b'])
# for i in range(100001, -1, -2):
#     print(f) [X] - L[3],d['b'] does not exist so an error will be fired. a alphabetic string cannot be converted to integer, however the loop runs from 100001 to -1 in steps of -2 and prints f. this is a valid program
# print(int('abc'))
# None of the above