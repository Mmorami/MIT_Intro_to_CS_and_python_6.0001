# Write a Python function that takes in two lists and calculates whether they
# are permutations of each other. The lists can contain both integers and
# strings. We define a permutation as follows:

# 1) the lists have the same number of elements
# 2) list elements appear the same number of times in both lists
# If the lists are not permutations of each other,
# the function returns False.
# If they are permutations of each other, the
# function returns a tuple consisting of the following elements:

# a) the element occuring the most times
# b) how many times that element occurs
# c) the type of the element that occurs the most times
# If both lists are empty return
# the tuple (None, None, None). If more than one element occurs the most number
# of times, you can return any of them.

# def is_list_permutation(L1, L2):
#     """
#     L1 and L2: lists containing integers and strings
#     Returns False if L1 and L2 are not permutations of each other. 
#             If they are permutations of each other, returns a 
#             tuple of 3 items in this order: 
#             the element occurring most, how many times it occurs, and its type
#     """
#     # Your code here
# For example,

# if L1 = ['a', 'a', 'b'] and L2 = ['a', 'b'] then is_list_permutation returns
# False if L1 = [1, 'b', 1, 'c', 'c', 1] and L2 = ['c', 1, 'b', 1, 1, 'c'] then
# is_list_permutation returns (1, 3, <class 'int'>) because the integer 1 occurs
# the most, 3 times, and the type of 1 is an integer (note that the third
# element in the tuple is not a string). Paste your entire function, including
# the definition, in the box below. Do not leave any debugging print statements.

from collections import Counter


def is_list_permutation(L1, L2):
    """
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    """
    # Using built-in counter function

    # c1 = Counter(L1)
    # c2 = Counter(L2)
    # if c1 != c2:
    #     return False
    # if not c1:
    #     return None, None, None
    # # most_common gives a list of the (n) most common instances in counter
    # occurences = c1.most_common(1)[0]
    # return occurences[0], occurences[1], type(occurences[0])

    # A more basic approach

    if len(L1) != len(L2):
        return False
    l1_count_dict = {}
    l2_count_dict = {}
    for index in range(len(L1)):
        l1_count_dict[L1[index]] = l1_count_dict.get(L1[index], 0)
        l2_count_dict[L2[index]] = l2_count_dict.get(L2[index], 0)
        l1_count_dict[L1[index]] += 1
        l2_count_dict[L2[index]] += 1
    if l1_count_dict != l2_count_dict:
        return False
    if not l1_count_dict:
        return None, None, None

    max = 0
    best_key = None
    for key, val in l1_count_dict.items():
        if val > max:
            max = val
            best_key = key
    return best_key, max, type(best_key)

L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']
print(is_list_permutation(L1, L2))