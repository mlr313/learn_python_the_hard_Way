# again, argv is unpacked to display variables
from sys import argv

# these are the variables
script, user_name = argv

# this defines what the raw_input prompt will look like.
prompt = '> '

# this line prints the sentence with the defined variables.
print "Hi %s, I'm the %s script." % (user_name, script)
# this line prints the sentence without variation; no variables defined
print "I'd like to ask you a few questions."
# this line prints the described sentence with the defined variables
print "Do you like me %s?" % user_name
# this line prompts input for "likes"
likes = raw_input (prompt)
# this line prints the described sentence with the defined variables"
print "Where do you live %s?" % user_name
# this line prompts input for "lives"
lives = raw_input (prompt)

# this ine prints the described sentence without variation
print "What kind of computer do you have?"
# this line prompts input for "computer"
computer = raw_input (prompt)

# this line starts three lines of text with variables within it that were defined by input promted by the above code.

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
# the line above relates the raw_input prompts to the variables in the above text.
