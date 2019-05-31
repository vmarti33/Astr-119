#!/usr/bin/env python
# coding: utf-8

# # Python Exercises
# 
# The following exercises range in difficulty, with some taking more time and thought than others.  For most of these exercises, you'll be asked to fill in the body of a function.  This function will then be tested in the code cell below the function definition using python's `assert` statement.  If running the test cell produces any errors, see which test case has broken your code and see if you can fix it.

# ## Absolute Value
# 
# Python already implements the absolute value function as a builtin function, `abs()`.  Let's write our own version!

# In[ ]:


def my_abs(x):
    """
    Calculates the absolute value of the input.
    
    Parameters
    ----------
    x : float
    
    Returns
    -------
    a : float, absolute value of x
    """
    # fill in your code here


# In[ ]:


x = 1
assert abs(x) == my_abs(x)

x = -1
assert abs(x) == my_abs(x)

x = 1.2
assert abs(x) == my_abs(x)

x = -124.3245
assert abs(x) == my_abs(x)


# ## Remainder
# 
# Write a program that calculates the remainder of the division of one number by another.  This is already done with the builtin modulo operator, `%`, but you should implement your own version!

# In[7]:


def remainder(dividend, divisor):
    """
    Calculate the remainder of the division of dividend by divisor.
    
    Parameters
    ----------
    dividend : int, the numerator
    divisor : int, the denominator
    
    Returns
    -------
    rem : int, the remainder
    """
    # fill in your code here
    x=divisor
    while x + divisor < dividend
        x = x + divisor
    rem = dividend - x


# In[ ]:


# remainder test cases

a = 5
b = 3
assert remainder(a, b) == a % b

a = 12
b = 6
assert remainder(a, b) == a % b

a = 23
b = 15
assert remainder(a, b) == a % b


# ## Project Euler \# 1
# 
# [Project Euler](https://projecteuler.net/about) provides a series of computational programming challenges.  Let's look at the first one.
# 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.  The answer should be 233168.

# In[ ]:





# ## List of lists
# 
# Suppose you have a list of lists of numbers.  Write a program that returns the list that contains the largest number.  For example, suppose the list of lists is
# 
# \[ \[0, 1, -25, 3\], \[1, 1, 4\], \[-2, 1\] \]
# 
# Then your program should return the second list, \[1, 1, 4\].

# In[20]:


def largest_list(list_of_lists):
    """
    Find the largest element in a list of lists, and return the inner list.
    
    Parameters
    ----------
    list_of_lists : a list containing lists of floats
    
    Returns
    -------
    max_list : a list of floats
    """
    # fill in your code here
def largest_list(list_of_list)


# In[1]:


a = [[1, 2, 3], [2, 3, 4]]
assert largest_list(a) == a[1]

b = [[7,2,7,8], [5,7,8,9,0,3,6], [3,2,5,2,6]]
assert largest_list(b) == b[1]

c = [[2345, 43, 3245], [21,4,6,-8,6], [0]]
assert largest_list(c) == c[0]

d = [[1], [-2345, 43], [76453, 345, 76]]
assert largest_list(d) == d[2]


# ## Fibonacci Sequence
# 
# The Fibonacci sequence (1, 1, 2, 3, 5, 8, 13...) satisfy the property that the $n$-th entry in the sequence is equal to the sum of the previous two entries in the sequence.  Fill in the function below which takes as input the index into the sequence and returns as output the value of that entry.  
# 
# If what you write is correct, then `fib(0) = 1`, `fib(1) = 1`, and `fib(6) = 13`.

# In[ ]:


def fib(n):
    """
    Calculate the Fibonacci sequence at index n.
    
    Parameters
    ----------
    n : int, index into the sequence
    
    Returns
    -------
    x : int, value of the sequence at index n
    """
    # fill in your code here


# In[ ]:


# fibonacci test cases
assert fib(2) == 2
assert fib(4) == 5
assert fib(5) == 8
assert fib(6) == 13


# ## Close enough
# 
# Write a function that takes as input a number and a list of numbers, then returns the index of the list for which the entry of the list is closest to that number.  For example, if the number is `4` and the list is `[1, 2, 5]`, the function should return `2`, since the entry at index 2 (with value 5) is closest to 4.
# 
# You may find it useful to use the built-in function, `abs()`, which calculates the absolute value of a number.

# In[ ]:


def index_of_closest(x, values):
    """
    Find the index (into the list, values) of the entry which is closest to x.
    
    Parameters
    ----------
    x : float
    values : list of floats
    
    Returns
    -------
    i : int, index into values
    """
    # fill in your code here


# In[ ]:


# index_of_closest test cases

values = [0, 1, 2, 3, 4, 5]

assert index_of_closest(1.1, values) == 1
assert index_of_closest(7, values) == 5
assert index_of_closest(2.9, values) == 3

