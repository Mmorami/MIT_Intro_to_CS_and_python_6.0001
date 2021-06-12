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
    seq = sequence
    for index, letter in enumerate(sequence):
        if len(seq) == 1:
            return seq
        l_perm_red = get_permutations(seq[:index]+seq[index+1:])
        l_perm_final = []
        for perm in l_perm_red:
            for char in perm:
                l_perm_final.append(perm.replace(char, letter+char))
            l_perm_final.append(perm+letter)
        return l_perm_final


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
    print('Input:', seq)
    print('Expected Output:', exp)
    print('Actual Output:', get_permutations(seq))

    seq = "dodd"
    exp = ['dod', 'ddo', 'odd', 'odd', 'dod', 'ddo']
    print('Input:', seq)
    print('Expected Output:', exp)
    print('Actual Output:', get_permutations(seq))

    seq = "bust"
    exp = ['bust', 'buts', 'bsut', 'bstu', 'btus', 'btsu',
           'ubst', 'ubts', 'utbs', 'utsb', 'utbs', 'utsb',
           'tbus', 'tbsu', 'tusb', 'tubs', 'tsub', 'tsbu',
           'sbut', 'sbtu', 'subt', 'sutb', 'stbu', 'stub']
    print('Input:', seq)
    print('Expected Output:', exp)
    print('Actual Output:', get_permutations(seq))

