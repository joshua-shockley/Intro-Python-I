"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

with open('src/foo.txt', 'r') as f:
    for line in f:
        #f_contents = f.readline()
        print(line, end='\n')


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('src/bar.txt', 'w') as bar:
    bar.write('\n')
    bar.write("this is line one \n")
    bar.write("this is line two \n")
    bar.write("this is the third line \n")
    bar.close()

with open('src/bar.txt', 'r') as bar:
    read_it = bar.read()
    print(read_it)
    bar.close()