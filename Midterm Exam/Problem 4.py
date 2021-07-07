# Write a function is_triangular that meets the specification below. 
# A triangular number is a number obtained by the continued summation 
# of integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc.,
#  corresponding to 1, 3, 6, 10, etc., are triangular numbers.

# def is_triangular(k):
#     """
#     k, a positive integer
#     returns True if k is triangular and False if not
#     """
#     #YOUR CODE HERE

# Paste your entire function, including the definition, in the box below. 
# Do not leave any debugging print statements.

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    # Naive method

    # res = k
    # if res == 1:
    #     return True
    # for i in range(1, k):
    #     res -= i
    #     if res == 0:
    #         return True
    #     elif res < 0:
    #         return False
    # return False


    # Triangular number is a sum of an arithmetic sequence, hence we can use the closed formula:
    # S_n = n*(2*a_1 + (n-1)*d)/2
    # simplifying it we get: 2*S_n = n^2*d + n * (-d + 2*a_1) =
    # if we plug in: d=1, a_1=1 we get: 2*S_n = n^2 + n = n*(n+1) now this is a simple quadratic equation
    # n^2 + n - 2S_n  = 0    ------->    [-1 +- sqrt(1^2 - 4*1*(-2*S_n))]/2*1 = [-1 +- sqrt(1+8*S_n)]/2
    # from that quadratic we get the value of n. if n is a whole number (an integer) the number is triangular, if not, it is not.

    # a more efficient method
    n = (-1 + (1 + 8*k)**0.5)/2
    # note that I chose only the + branch in the quadratic equation as n should be positive
    if n.is_integer():
        return True
    return False


print(is_triangular(95))