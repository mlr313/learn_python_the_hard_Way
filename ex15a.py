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
