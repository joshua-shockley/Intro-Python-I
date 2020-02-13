"""
Python tuples are sort of like lists, except they're immutable and
are usually used to hold heterogenous data, as opposed to lists
which are typically used to hold homogenous data. Tuples use
parens instead of square brackets.

More specifically, tuples are faster than lists. If you're looking
to just define a constant set of values and that set of values
never needs to be mutated, use a tuple instead of a list.

Additionally, your code will be safer if you opt to "write-protect"
data that does not need to be changed. Tuples enforce immutability
automatically.
"""

# Example:

import math


def dist(a, b):
    """Compute the distance between two x,y points."""
    x0, y0 = a  # Destructuring assignment
    x1, y1 = b

    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)


a = (2, 7)   # <-- x,y coordinates stored in tuples
b = (-14, 72)

# Prints "Distance is 66.94"
print("Distance is: {:.2f}".format(dist(a, b)))


# Write a function `print_tuple` that prints all the values in a tuple
def print_tuple(f):
    print(f)
# YOUR CODE HERE
    for value in f:
        print(value)


t = (1, 2, 5, 7, 99)
print_tuple(t)  # Prints 1 2 5 7 99, one per line

# Declare a tuple of 1 element then print it
u = (1,)  # What needs to be added to make this work?  had to add the comma; tuples need a comma if only one item in the tuple
print_tuple(u)
# no way to actually adjust or modify a tuple.. Immutable list basically. you can however make a new one or replace entire tuple with same name.
u = (33, 1, 0)
print_tuple(u)

print(u[1])
for index in u:
    print("in for each loop", index)

# can't really manipulate a tuple but can take it's values and append them into a list


def manipulate_tuple(tuple):
    list = []
    # for index in tuple:
    #     list.append(index*3)
    #     # print(list)
    list = [index*3 for index in tuple]
    # print(tuple(list))
    return list


print(manipulate_tuple(u))

stuff = ['stuff', 1, "helo"]

print(tuple(stuff))

tup_stuff = tuple(stuff)
print("tup_stuff:", tup_stuff)
