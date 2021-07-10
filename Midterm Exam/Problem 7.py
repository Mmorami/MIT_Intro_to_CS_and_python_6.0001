# Write a function called dict_invert that takes in a dictionary with immutable
# values and returns the inverse of the dictionary. The inverse of a dictionary
# d is another dictionary whose keys are the unique dictionary values in d. The
# value for a key in the inverse dictionary is a sorted list (increasing order)
# of all keys in d that have the same value in d.

# Here are two examples:

# If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30:
# [3]} If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20:
# [2], 30: [3, 4]} If d = {4:True, 2:True, 0:True} then dict_invert(d) returns
# {True: [0, 2, 4]} def dict_invert(d):
#     '''
#     d: dict
#     Returns an inverted dictionary according to the instructions above
#     '''
#     #YOUR CODE HERE
# Paste your entire function, including the definition, in the box below. Do not
# leave any debugging print statements.

# Paste your function here
def dict_invert(d):
    """
    d: dict
    Returns an inverted dictionary according to the instructions above
    """
    # silly way

    # d_invert = {}
    # for key in d.keys():
    #     val = d[key]
    #     if val not in d_invert.keys():
    #         d_invert[val] = []
    #     d_invert[val].append(key)
    #
    # for key in d_invert.keys():
    #     d_invert[key].sort()
    # return d_invert

    # a better way using .item()

    d_invert = {}
    for key, val in d.items():
        # the get function returns the value of the key specified. 2nd argument specifies what to return if not found
        # this assures that if the value in d is not already registered as key in d_invert it will create it with an empty list
        # this is a different approach to the if statement in the previous solution
        d_invert[val] = d_invert.get(val, [])
        d_invert[val].append(key)

    for key in d_invert.keys():
        d_invert[key].sort()
    return d_invert


print(dict_invert({1:10, 2:20, 5:20, 3:30, 4:30, -1:10}))