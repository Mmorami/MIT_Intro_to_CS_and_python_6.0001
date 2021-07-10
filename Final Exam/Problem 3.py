# Implement a function that meets the specifications below.

# def sum_digits(s):
#     """ assumes s a string
#         Returns an int that is the sum of all of the digits in s.
#           If there are no digits in s it raises a ValueError exception. """
#     # Your code here
# For example, sum_digits("a;35d4") returns 12.

# Paste your entire function, including the definition, in the box below. 
# Do not leave any debugging print statements.

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
        If there are no digits in s it raises a ValueError exception. """
    digits = "0123456789"
    res = 0
    for char in s:
        if char in digits:
            res += int(char)
    if res == 0:
        raise ValueError("Value error amigo")
    return res

print(sum_digits("a;fqdp"))