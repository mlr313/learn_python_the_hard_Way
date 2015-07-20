
#this line defines x as text (string)
x = "There are %d types of people." % 10
#this line defines binary as "binary"
binary = "binary"
#this line defines do_not as "don't"
do_not = "don't"
#this line defines y as text (string)
y = "Those who know %s and those who %s." % (binary, do_not)

#this line commands the text string defined by x be printed.
print x
#this line commands the text string defined by y be printed
print y

#this line inserts the text string x into "I said:"
print "I said: %r." % x
#this line inserts the text string y into "I also said:"
print "I also said: '%s'." % y

#this line equates the descriptor "hilarious" with the condition "false"
hilarious = False
#this line defines joke_evaluation as "isn't that joke so funny?"
joke_evaluation = "Isn't that joke so funny?! %r"

#this answers the joke evaluation as "hilarous", which has been equated with "false"
print joke_evaluation % hilarious
#this line defines w as text
w = "This is the left side of..."
#this line defines e with text
e = "a string with a right side"

#this prints the text defined by w in addition to the text defined by e
print w + e
