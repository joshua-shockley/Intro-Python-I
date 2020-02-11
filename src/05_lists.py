# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
print(x)
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print(x)
x.extend(y)  # adds y list to the end of the x list as one list.. like it eats it
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print(x)
x.remove(8)
print(x)
# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
print(x)
x.insert(5, int("99"))
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE

for thing in x:
    print(int(thing)*1000)


x = [4, 3, 45, 2, 1]
total = 0
for number in x:
    print(number, total)
    total += number

print("total", total)

print("sum fn", sum(x))


theList = [4, 3, 45, 2, 1]


def check(list, arg):
    total = list.count(arg)
    if total > 0:
        print('true')
        return True
    else:
        print('false')
        return False


check(theList, 14)
