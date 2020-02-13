"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

with open('foo.txt', 'r') as f:
    for line in f:
        #f_contents = f.readline()
        print(line, end='\n')


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.txt', 'w') as bar:
    bar.write('\n')
    bar.write("this is line one \n")
    bar.write("this is line two \n")
    bar.write("this is the third line \n")
    bar.close()

with open('bar.txt', 'r') as bar:
    read_it = bar.read()
    print(read_it)
    bar.close()


with open('snarf.txt', 'w') as snarf:
    snarf.write('\n')
    snarf.write('this is one line \n')
    snarf.write('this is another line to look at\n')
    snarf.write('you might like where this is going.... maybe\n')
    snarf.write('really, Josh... again?\n')
    snarf.write('alright, that is enough already!')
    snarf.close()

with open('snarf.txt', 'r') as snarf:
    read_it = snarf.read()
    print("from snarf:", read_it)
    snarf.close()
