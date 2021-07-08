# Write a function called general_poly, that meets the specifications below. For
# example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 
# 1*10^3+2*10^2+3*10^1+4*10^0.

# def general_poly (L): """ L, a list of numbers (n0, n1, n2, ... nk) Returns a
#     function, which when applied to a value x, returns the value n0 * x^k + n1
#     * x^(k-1) + ... nk * x^0 """ #YOUR CODE HERE

def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    # an inner function as expected in the question
    def to_apply(x):
        power = len(L) - 1
        res = 0
        for n_i in L:
            res += n_i*x**power
            power -= 1
        return res
    # this is the way to call an inner function from a parent function (without the parentheses ())
    return to_apply

# this is a mean to call inner function. the question implies that an inner function has to be defined to get x.
# we deliver the list to the general_poly function, but we also send the int x for the inner function separately
pol = general_poly([1,2,3,4,5,6])(2)
print(pol)