"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
from sys import argv

script, input_file = argv
'''the with keyword automatically closes after command finishes'''
with open(input_file) as f:
    print(f.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
print("make new file bar.txt with three lines from you")
line1 = input('line 1: ')
line2 = input('line 2: ')
line3 = input('line 3: ')

new_file = open('bar.txt', 'w')
new_file.write(line1)
new_file.write("\n")
new_file.write(line2)
new_file.write("\n")
new_file.write(line3)
new_file.write("\n")

new_file.close()

with open('bar.txt') as f:
    print(f.read())
