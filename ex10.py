# this command tabbed this line to the right.
tabby_cat = "\tI'm tabbed in."
# this command split the sentence between two lines after the word "split"
persian_cat = "I'm split\non a line."
# this command spaced these three words with a space and a backslash
backslash_cat = "I'm \\ a \\ cat."

# the three """ encased the text; the list is split onto new lines and tabbed into the right
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# these lines executed the commands as written above.
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" %i, 
