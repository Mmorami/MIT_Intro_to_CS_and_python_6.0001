# Write a function that satisfies the following docstring:

# def largest_odd_times(L):
#     """ Assumes L is a non-empty list of ints
#         Returns the largest element of L that occurs an odd number 
#         of times in L. If no such element exists, returns None """
#     # Your code here
# For example, if

# largest_odd_times([2,2,4,4]) returns None
# largest_odd_times([3,9,5,3,5,3]) returns 9
# Paste your entire function, including the definition, in the box below. 
# Do not leave any debugging print statements.

from collections import Counter

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Using a built-in function counter

    # count_dict = Counter(L)

    # Using fundamental functions only
    count_dict = {}
    for element in L:
        if element not in count_dict.keys():
            count_dict[element] = 0
        count_dict[element] += 1
    count_list_odd = [num for num in count_dict.keys() if count_dict[num] % 2 == 1]
    if not count_list_odd:
        return None
    return max(count_list_odd)


print(largest_odd_times([2,12,12,12,12,11,11,9,9,9,9,9,9,9,3,3,9,5,3,5,3]))