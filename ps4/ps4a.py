# this is a recursive function. the function takes a string and outputs all permutations of the chars composing it.
# the idea is to reduce the problem to a smaller and smaller strings. the seed case is when there is only 1 char
# every call reduces the string, and every return sends the permutation of the chars thus far to the scope
# with 1 extra letter
def get_permutations(sequence):
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """
    # seed case - if the string is 1 letter long, there is only 1 permutation. return list with the letter
    if len(sequence) == 1:
        return [sequence]
    # (else) call the function with the string minus the first letter - every call will cut 1 letter from the original
    # and stores it. it is called previous list to emphasise that those are all the permutations of the string with 1
    # less char than current iteration when calculations are come in to play.
    l_previous = get_permutations(sequence[1:])
    # initiate the next list of permutation, which will be sent for next iteration (the iteration with 1 more letter)
    l_next = []
    # iterate over every permutation found in the scope of previous call (meaning a string with 1 less
    # letters than current iteration
    for perm in l_previous:
        # iterates over each char in the string of current call (+1 letters than previous call)
        for index, char in enumerate(sequence):
            # insert the new letter
            s = perm[0:index] + sequence[0] + perm[index:]
            # appends the new permutation only if it is not already in the list
            if s not in l_next:
                l_next.append(s)
    return l_next


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    seq = "abc"
    exp = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    actual = get_permutations(seq)
    print('Input:', seq)
    print('Expected Output:', exp)
    print('Actual Output:', actual)
    print('Expected is same as actual:', set(exp) == set(actual))

    seq = "dodd"
    exp = ['dddo', 'ddod', 'dodd', 'oddd']
    actual = get_permutations(seq)
    print('Input:', seq)
    print('Expected Output:', exp)
    print('Actual Output:', actual)
    print('Expected is same as actual:', set(exp) == set(actual))

    seq = "bust"
    exp = ['bust', 'buts', 'bsut', 'bstu', 'btus', 'btsu',
           'ubst', 'ubts', 'utbs', 'utsb', 'usbt', 'ustb',
           'tbus', 'tbsu', 'tusb', 'tubs', 'tsub', 'tsbu',
           'sbut', 'sbtu', 'subt', 'sutb', 'stbu', 'stub']
    actual = get_permutations(seq)
    print('Input:', seq)
    print('Expected Output:', exp)
    print('Actual Output:  ', actual)
    print('Expected is same as actual:', set(exp) == set(actual))


