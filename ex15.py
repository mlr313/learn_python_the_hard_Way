# import argv
from sys import argv

# items to be unpacked by argv
script, filename = argv

# opens text file by name typed into command line
txt = open(filename)

# here's your file (name of imported text file)
print "Here's your file %r:" % filename

# this line reads the actual text in the text file.
print txt.read()

# this line prints the text "type the filename again."
print "Type the filename again:"
# this line has an arrow prompting the direct input
file_again = raw_input ("> ")

# this line opens the file again
txt_again = open (file_again)

# this line reads the textfile again.
print txt_again.read()
