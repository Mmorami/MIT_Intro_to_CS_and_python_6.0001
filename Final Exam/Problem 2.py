# You have the following class hierarchy:

class A(object):
    def foo(self):
        print('hi')


class B(A):
    def foo(self):
        print('bye')
          

# Which of the following is correct?
# When a = A() we say that a is an instance of A [X] - B is a subclass of A anyway.
# When b = B() we say that b is a subclass of A
# Both of the above
# Neither of the above

# Consider the function f below. What is its Big O complexity?

def f(n):
    # 1 + 2
    def g(m):
        m = 0
        # the loop never fires, an assignment of i then a check of i<m
        for i in range(m):
            print(m)
    for i in range(n):
        # executing g() n times
        g(n)

# g() itself execute 3 operations with each call while f() call g() n times, hence the order of growth is O(n)

# A dictionary is an immutable object because its keys are immutable.
# True 
# False because its keys can be mutable
# False because a dictionary is mutable [X] - the value of a key can be changed by simple assignment.

# Consider the following two functions and select the correct choice below:

def foo_one(n):
    """ Assume n is an int >= 0 """
    answer = 1.0
    while n > 1:
        answer *= n
        n -= 1
    return answer

def foo_two(n):
    """ Assume n is an int >= 0 """
    if n <= 1: 
        return 1.0
    else: 
        return n*foo_two(n-1)


# The worst case Big Oh time complexity of foo_one is worse than the worst case Big Oh time complexity of foo_two.
# The worst case Big Oh time complexity of foo_two is worse than the worst case Big Oh time complexity of foo_one.
# The worst case Big Oh time complexity of foo_one and foo_two are the same. [x] - both functions' complexity is O(n)
# Impossible to compare the worst case Big Oh time complexities of the two functions.

# The complexity of 1^n + n^4 + 4n + 4 is
# constant
# logarithmic
# linear
# polynomial [X] - exponential (c^n) is more dominant than polynomial (n^c), but in the special case of 1^n the result is 1 for every n so it does not dominate
# exponential