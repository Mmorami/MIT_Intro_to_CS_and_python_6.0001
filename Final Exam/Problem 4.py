# Implement a function that meets the specifications below.

# def max_val(t): 
#     """ t, tuple or list
#         Each element of t is either an int, a tuple, or a list
#         No tuple or list is empty
#         Returns the maximum int in t or (recursively) in an element of t """ 
#     # Your code here
# For example,

# max_val((5, (1,2), [[1],[2]])) returns 5.
# max_val((5, (1,2), [[1],[9]])) returns 9.

# Paste your entire function, including the definition, in the box below. Do not leave any 
# debugging print statements.

def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """

    tot_list = []
    if type(t) == int:
        return t

    # the curr assignment is redundant, it is merely there to make the code more readable
    for item in t:
        curr = max_val(item)
        tot_list.append(curr)
    return max(tot_list)


print(max_val((-5, (-1, -2), [[-1], [-2]])))
print(max_val((-5, (-1, -2), [[-1], [9]])))
