# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)
# [1, 2, 3, 4]

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
'''x.append(y)
expect this to be answer but got: [1, 2, 3, 4, [8, 9, 10]]
'''
x = x + y
#this should join two lists and update x with the values
print(x)
# [1, 2, 3, 4, 8, 9, 10]

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
del x[4]
print(x)
#[1, 2, 3, 4, 9, 10]

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))
#the above line printed out x 100 times. it did not mult each value in list and print a new array with produtcts
# Print all the values in x multiplied by 1000
# YOUR CODE HERE
#the line printed out x 100 times. it did not mult each value in list and print a new array with produtcts
#print(x*100)
z = [c*100 for c in x]
print(z)
